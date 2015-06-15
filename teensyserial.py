# -*- coding: utf-8 -*-

import sys
import serial
from serial.tools import list_ports
import time

class TeensySerial:
    def __init__(self, baudrate):
        self.teensy_port = self.find_teensy2_linux()
        if self.teensy_port:
            self.teensy = serial.Serial(self.teensy_port[0], baudrate)
        else:
            self.teensy = None

    def find_teensy2_linux(self):
        if sys.platform.startswith("linux"):
            ports_avaiable = list(list_ports.grep("/dev/ttyACM.*"))
            teensy_ports = list()
            if ports_avaiable != []:
                for ports in ports_avaiable:
                    if ports[-1][12:21] == "16c0:0483" and ports[-1][26:31] == "12345":
                        teensy_ports.append(ports)
                if len(teensy_ports) > 1:
                    return teensy_ports[-1]
                else:
                    return teensy_ports[0]

    def get_port(self):
        try:
            return self.teensy_port[0]
        except TypeError:
            return None

    #def send(self, data):
    #    self.teensy.write(data)

    def recv(self):
        self.teensy.flushInput()
        return self.teensy.read(5)

    def finish(self):
        if self.teensy.isOpen():
            self.teensy.close()