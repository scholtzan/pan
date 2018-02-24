
# timer

from tinydb import TinyDB, Query

from Cocoa import NSEvent, NSKeyDownMask, NSTimer
from PyObjCTools import AppHelper
from AppKit import NSWorkspace
import schedule 

def handler():
    print "foo"
    activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    print activeAppName




def init(db):
    print 'Init Timer'
    schedule.every(1).seconds.do(handler)
    print 'End'

