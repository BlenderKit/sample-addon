import bpy

class HelloWorldPopup(bpy.types.Operator):
    bl_idname = "view3d.hello_world_popup"
    bl_label = "Hello World Popup"
    bl_description = "Click to see a Hello popup"
    bl_options = {'REGISTER'}

    def execute(self, context):
        self.report({'INFO'}, "Hello")
        return {'FINISHED'}

class HelloWorldPanel(bpy.types.Panel):
    bl_label = "Hello World"
    bl_idname = "VIEW3D_PT_hello_world"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'HelloWorldTab'

    def draw(self, context):
        layout = self.layout
        layout.operator("view3d.hello_world_popup", text="Click Me!")

def register():
    bpy.utils.register_class(HelloWorldPopup)
    bpy.utils.register_class(HelloWorldPanel)

def unregister():
    bpy.utils.unregister_class(HelloWorldPopup)
    bpy.utils.unregister_class(HelloWorldPanel)