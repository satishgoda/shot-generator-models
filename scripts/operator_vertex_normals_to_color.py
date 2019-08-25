import bpy


# https://gist.github.com/Kodagrux/5b39358d812c0fd8eaf4
def remap(value, maxInput, minInput, maxOutput, minOutput):
    value = maxInput if value > maxInput else value
    value = minInput if value < minInput else value

    inputSpan = maxInput - minInput
    outputSpan = maxOutput - minOutput

    scaledThrust = float(value - minInput) / float(inputSpan)

    return minOutput + (scaledThrust * outputSpan)


class VertexNormalToVertexColorsOperator(bpy.types.Operator):
    """Convert averaged vertex normals to vertex colors"""
    bl_idname = "object.bake_vertex_normal_to_color"
    bl_label = "Bake Vertex Normal To Color"

    @classmethod
    def poll(cls, context):
        return (context.active_object is not None)

    def execute(self, context):
        aodata = context.active_object.data

        if not 'vertex_normals' in aodata.vertex_colors:
            aodata.vertex_colors.new(name='vertex_normals')

        color_layer = aodata.vertex_colors['vertex_normals']
        color_layer.active = True
        color_layer.active_render = True

        i = 0
        for poly in aodata.polygons:
            for idx in poly.vertices:
                normal = aodata.vertices[idx].normal
        
                r = remap(normal.x, 1, -1, 1, 0)
                g = remap(normal.y, 1, -1, 1, 0)
                b = remap(normal.z, 1, -1, 1, 0)
                color_layer.data[i].color = (r, g, b, 1.0)
                i += 1
        return {'FINISHED'}


def register():
    bpy.utils.register_class(VertexNormalToVertexColorsOperator)


def unregister():
    bpy.utils.unregister_class(VertexNormalToVertexColorsOperator)


if __name__ == "__main__":
    register()
