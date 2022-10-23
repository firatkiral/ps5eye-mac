# Intalling PS5 HD cam on mac

# install libs
    $ brew install libusb

# pyusb works with python38
    $ brew install python@3.8

# create env and install pyusb
    $ python3.8 -m venv env
    $ env/bin/Activate.ps1
    $ pip install --pre pyusb

# Ensure that the uninitialized camera is recognized:
    $ lsusb -d 05a9:0580
    Bus 004 Device 001: ID 05a9:0580 OmniVision Technologies, Inc. 

# Initialize the camera with the provided script:
    $ python ps5eye_init.py
    PS4 camera firmware uploaded and device reset

# The device should now be available with a new product id:
    $ lsusb -v -d 05a9:058a


# https://github.com/ps4eye/ps4eye