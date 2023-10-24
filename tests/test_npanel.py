import unittest
import bpy


import sample_addon
from sample_addon.npanel.npanel import HelloWorldPopup, HelloWorldPanel

class Test01HelloWorldPanel(unittest.TestCase):
    def test01_hello_world_panel(self):
        assert HelloWorldPanel.is_registered

    def test02_hello_world_panel(self):
        # Find an existing 3D View area
        area_3d = None
        for area in bpy.context.window.screen.areas:
            if area.type == 'VIEW_3D':
                area_3d = area
                break
        
        # If no 3D View is found, it's not possible to run this test
        if area_3d is None:
            print("No 3D View found. Skipping HelloWorldPanel test.")
            return

        # Search for the HelloWorldPanel among registered panels
        found = False
        for panel in bpy.types.Panel.__subclasses__():
            if not hasattr(panel, 'bl_idname'):
                continue
            if panel.bl_idname == "VIEW3D_PT_hello_world":
                found = True
                break

        assert found, "HelloWorldPanel was not found in 3D View's UI region"


class Test02HelloWorldPopup(unittest.TestCase):
    def test01_hello_world_popup(self):
        assert HelloWorldPopup.is_registered

    def test02_hello_world_popup(self):
        result = bpy.ops.view3d.hello_world_popup()
        assert result == {'FINISHED'}, f"Expected {{'FINISHED'}}, but got {result}"
