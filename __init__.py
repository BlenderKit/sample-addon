
bl_info = {
    "name": "Sample Addon",
    "author": "Andreas Gajdosik",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "Properties Panel > Scene Tab > Sample Addon",
    "description": "Prints hello on registration, and goodbye on unregistration",
    "warning": "Does nothing useful",
    "category": "Workspace",
}

from . import nice
from . npanel import npanel


modules =  [npanel]

def register():
    nice.hello()
    for module in modules:
        module.register()

def unregister():
    nice.goodbye()
    for module in modules:
        module.unregister()
