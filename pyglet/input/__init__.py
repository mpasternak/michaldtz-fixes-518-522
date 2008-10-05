#!/usr/bin/env python

'''
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: $'

import sys

from base import Device, Control, Button, Joystick
from base import DeviceException, DeviceOpenException, DeviceExclusiveException

_is_epydoc = hasattr(sys, 'is_epydoc') and sys.is_epydoc

if _is_epydoc:
    def get_devices(display=None):
        '''
        '''

    def get_joysticks(display=None):
        '''
        '''
else:
    if sys.platform == 'linux2':
        '''
        from x11_xinput import get_devices as xinput_get_devices
        from evdev import get_devices as evdev_get_devices
        def get_devices(display=None):
            return (evdev_get_devices(display) +
                    xinput_get_devices(display))
        '''
        from evdev import get_devices
    elif sys.platform in ('cygwin', 'win32'):
        from directinput import get_devices
    elif sys.platform == 'darwin':
        from darwin_hid import get_devices
        from darwin_hid import get_joysticks
