import bpy

# https://gist.github.com/Kodagrux/5b39358d812c0fd8eaf4
def remap(value, maxInput, minInput, maxOutput, minOutput):
    value = maxInput if value > maxInput else value
    value = minInput if value < minInput else value

    inputSpan = maxInput - minInput
    outputSpan = maxOutput - minOutput

    scaledThrust = float(value - minInput) / float(inputSpan)

    return minOutput + (scaledThrust * outputSpan)

# The mesh transform 
ao = bpy.context.active_object

# The Mesh Data
aodata = ao.data

# Get the active vertex color (Add it from the UI first)
color_layer = aodata.vertex_colors.active

i = 0
for poly in aodata.polygons:
    for idx in poly.vertices:
        normal = aodata.vertices[idx].normal
        
        r = remap(normal.x, 1, -1, 1, 0)
        g = remap(normal.y, 1, -1, 1, 0)
        b = remap(normal.z, 1, -1, 1, 0)
        
        color_layer.data[i].color = (r, g, b, 1.0)
        
        i += 1
