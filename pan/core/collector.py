from tinydb import TinyDB, Query
import yaml
import imp
from glob import glob
import schedule
from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
import schedule
from threading import Thread
from time import sleep

config = yaml.safe_load(open('../config.yml'))
db = TinyDB(config['database'])

def handler():
    print "foo"


class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):

        for plugin_path in glob(config['plugin_path'] + '*'):
            collector_path = glob(plugin_path + '/collector.py')[0]
            collector = imp.load_source('collector', collector_path)

            collector.init(db)

def scheduled_events():
    print "foo"
    while True:
        schedule.run_pending()
        sleep(1)


def main():

    thread = Thread(target = scheduled_events)
    thread.start()

    appl = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()


if __name__ == '__main__':
    main()
