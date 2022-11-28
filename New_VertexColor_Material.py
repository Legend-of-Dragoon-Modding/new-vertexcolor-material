bl_info = {
    "name": "New Mat for Vertex Color",
    "author": "DooMMetaL",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Category > VertexColorMAT > Vertex Color new Mat",
    "description": "Adds a new Material for each object that contains Vertex Color Data, saving some clicks in the way",
    "warning": "This addon is quite Experimental",
    "wiki_url": "",
    "category": "Add Material",
}


import bpy


class NEWVCMAT_PT_main_panel(bpy.types.Panel):

    bl_label = "Vertex Color Material"
    bl_idname = "NEWVCMAT_PT_main_panel"
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'VertexColorMAT'

    def draw(self, context):
        layout = self.layout
        layout.operator("newvcmat.vcmat_operator")

class NEWVCMAT_OT_add_vcmat(bpy.types.Operator):
    bl_label = "Vertex Color new Mat"
    bl_idname = "newvcmat.vcmat_operator"
    
    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all(action='SELECT')

        sel_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

        #number_obj = 0
        number_new = len(sel_objs)
        number_obj = int(number_new) - 1
        
        while len(sel_objs) >= 1:  
                          
            obj_in_sel = sel_objs.pop() 
            
            obj_in_sel.select_set(True) 
            
            bpy.context.view_layer.objects.active = obj_in_sel
             
            bpy.ops.object.material_slot_add()
            new_mat = bpy.data.materials.new(name = f'VC_{number_obj}')
            new_mat.use_nodes = True
            bpy.context.object.active_material = new_mat
            
            actshader_node = new_mat.node_tree.nodes.get('Principled BSDF')
            actshader_node.inputs[5].default_value = (0) # Specular
            actshader_node.inputs[7].default_value = (1) # Roughness
            actshader_node.inputs[11].default_value = (0) # Sheen Tint
            actshader_node.inputs[13].default_value = (0) # Clearcoat Roughness
            actshader_node.inputs[14].default_value = (0) # IOR
            
            attribute_node = new_mat.node_tree.nodes.new('ShaderNodeAttribute')
            attribute_node.location = (-256, 200)
            attribute_node.attribute_name = f'Col{number_obj}'
            
            link_nodes = new_mat.node_tree.links.new
            
            link_nodes(attribute_node.outputs[0], actshader_node.inputs[0])
            
            obj_in_sel.select_set(False) # deselecting the object previously selected
            print(f'New Vertex Colour Material add for Object_Number_{number_obj}\n')
            number_obj -= 1  # Counter of number of objects
            print(number_obj)
        return {'FINISHED'}

classes = [NEWVCMAT_PT_main_panel, NEWVCMAT_OT_add_vcmat]
 
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
 
 
 
if __name__ == "__main__":
    register()