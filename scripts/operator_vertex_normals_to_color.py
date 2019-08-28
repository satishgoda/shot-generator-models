import bpy
from mathutils import Color


# https://gist.github.com/Kodagrux/5b39358d812c0fd8eaf4
def remap_value(value, minInput, maxInput,  minOutput, maxOutput):
    value = maxInput if value > maxInput else value
    value = minInput if value < minInput else value

    inputSpan = maxInput - minInput
    outputSpan = maxOutput - minOutput

    scaledThrust = float(value - minInput) / float(inputSpan)

    return minOutput + (scaledThrust * outputSpan)


def get_color_for_normal(normal, remap=True):
    color = Color(normal)

    if remap:
        color.r = remap_value(color.r, -1, 1, 0, 1)
        color.g = remap_value(color.g, -1, 1, 0, 1)
        color.b = remap_value(color.b, -1, 1, 0, 1)

    return color


class VertexNormalToVertexColorsOperator(bpy.types.Operator):
    """Convert vertex normals to vertex colors"""
    bl_idname = "object.bake_vertex_normal_to_color"
    bl_label = "Bake Vertex Normal To Color"

    @classmethod
    def poll(cls, context):
        active_object = context.active_object
        return (active_object is not None \
                and active_object.type == 'MESH')  

    def execute(self, context):
        mesh = context.active_object.data

        if not 'vertex_normals' in mesh.vertex_colors:
            mesh.vertex_colors.new(name='vertex_normals')

        color_layer = mesh.vertex_colors['vertex_normals']
        color_layer.active = True
        color_layer.active_render = True

        i = 0
        for polygon in mesh.polygons:
            for vertex_index in polygon.vertices:
                normal = mesh.vertices[vertex_index].normal
        
                color = get_color_for_normal(normal, remap=True)
                r, g, b = color
                
                color_layer.data[i].color = (r, g, b, 1.0)
                
                i += 1
        return {'FINISHED'}


def register():
    bpy.utils.register_class(VertexNormalToVertexColorsOperator)


def unregister():
    bpy.utils.unregister_class(VertexNormalToVertexColorsOperator)


if __name__ == "__main__":
    register()
