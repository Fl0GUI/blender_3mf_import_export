# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "TODO",
    "description": "TODO",
    "author": "TODO",
    "version": (0,0), # TODO
    "blender": (2,80,0),
    "location": "File > Import-Export",
    "wiki_url": "https://github.com/solbaver/blender_3mf_import_export",
    "category": "Import-Export",
    "warning": "in progress"
}

import bpy
from bpy_extras.io_utils import (ImportHelper, ExportHelper)

class Import3MF(bpy.types.Operator, ImportHelper):
    bl_idname = "object.import"
    bl_label = "Import 3MF file"

    filename_ext = ".3mf"

    # TODO parameters

    def execute(self, context):
        #from . import import_3mf
        print("TODO: import")


    def draw(self, context):
        pass

class Export3MF(bpy.types.Operator, ExportHelper):
    bl_idname = "object.export"
    bl_label = "Export 3MF file"

    filename_ext = ".3mf"

    # TODO parameters

    def execute(self, context):
        #from . import export_3mf
        print("TODO: export")

    def draw(self, context):
        pass

def menu_func_import(self, context):
    self.layout.operator(Import3MF.bl_idname, text="3MF")

def menu_func_export(self, context):
    self.layout.operator(Export3MF.bl_idname, text="3MF")

classes = (
    Import3MF,
    Export3MF
)

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()
