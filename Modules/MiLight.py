from BaseModule import BaseModule
from controller import WifiController
from settings import *


class MiLight(BaseModule):

    def __init__(self):
        self.commands = {
            'lights on': self.lights_on,
            'lights off': self.light_off,
        }
        self.wifi_controller = WifiController(MILIGHT_IP, MILIGHT_PORT)

    def lights_on(self):
        self.wifi_controller.zone_on()

    def lights_off(self):
        self.wifi_controller.zone_off()