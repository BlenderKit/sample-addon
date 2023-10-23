import unittest
import bpy


import sample_addon
from sample_addon.npanel.npanel import HelloWorldPopup, HelloWorldPanel

class Test01OperatorsAreRegistered(unittest.TestCase):
    def test01_hello_world_panel(self):
        assert HelloWorldPanel.is_registered

    def test02_hello_world_popup(self):
        assert HelloWorldPopup.is_registered




