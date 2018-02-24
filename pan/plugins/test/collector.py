from tinydb import TinyDB, Query

from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper



def handler(event):
    try:
        print event
        text_file = open("/tmp/log.txt", "w")
        text_file.write("Event: %s" % event)
        text_file.close()
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()


def init(db):
    print 'Init'

    mask = NSKeyDownMask
    NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)



    print 'Init end'

