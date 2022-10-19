import os
os.environ['PYUSB_DEBUG'] = 'debug'
import usb.core
usb.core.find()

# for dev in usb.core.find(find_all=True):
#     print(dev)