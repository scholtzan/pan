import yaml
from flask import Flask
from flask import render_template
import jinja2
from glob import glob
import os
import importlib
import imp
from flask import Markup
from tinydb import TinyDB, Query



app = Flask(__name__)
config = yaml.safe_load(open('../config.yml'))


my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('../../'),
])
app.jinja_loader = my_loader


def render_plugin(path):
    render_file_path = glob(path + '/view.py')[0]
    tmp = imp.load_source('module.name', render_file_path)
    db = TinyDB(config['database'])
    data = tmp.data(db)

    filename = 'index.html'
    return Markup(jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(data))


@app.route('/')
def index():
    plugin_directories = glob(config['plugin_path'] + '*')
    plugin_visualizations = [(plugin_path.split('/')[-1], glob(plugin_path + '/*.html')[0], render_plugin(plugin_path)) for plugin_path in plugin_directories]
    print plugin_visualizations
    return render_template('index.html', plugin_visualizations = plugin_visualizations)



