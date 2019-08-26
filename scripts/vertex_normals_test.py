import bpy
from mathutils import Vector


aodata = bpy.context.active_object.data

# https://docs.blender.org/api/master/bpy.types.MeshVertex.html
# vtx.normal is the pre-calculated vertex normal
vertex_normals = {index: ([], vtx.normal)  for index, vtx in enumerate(aodata.vertices)}

# https://docs.blender.org/api/master/bpy.types.MeshPolygon.html
for polygon in aodata.polygons:
    for vertex_index in polygon.vertices:
        face_normals = vertex_normals[vertex_index][0]
        # We are going to sum the polygon normal vectors later and normalize to get vertex normal
        face_normals.append(polygon.normal)

for face_normals, pre_calculated_vertex_normal in vertex_normals.values():
    vertex_normal = sum(face_normals, Vector((0.0, 0.0, 0.0)))
    vertex_normal.normalize()
    print(vertex_normal)
    print(pre_calculated_vertex_normal)
    print("\n")

"""
<Vector (0.5774, 0.5774, 0.5774)>
<Vector (0.5773, 0.5773, 0.5773)>


<Vector (0.5774, 0.5774, -0.5774)>
<Vector (0.5773, 0.5773, -0.5773)>


<Vector (0.5774, -0.5774, 0.5774)>
<Vector (0.5773, -0.5773, 0.5773)>


<Vector (0.5774, -0.5774, -0.5774)>
<Vector (0.5773, -0.5773, -0.5773)>


<Vector (-0.5774, 0.5774, 0.5774)>
<Vector (-0.5773, 0.5773, 0.5773)>


<Vector (-0.5774, 0.5774, -0.5774)>
<Vector (-0.5773, 0.5773, -0.5773)>


<Vector (-0.5774, -0.5774, 0.5774)>
<Vector (-0.5773, -0.5773, 0.5773)>


<Vector (-0.5774, -0.5774, -0.5774)>
<Vector (-0.5773, -0.5773, -0.5773)>
"""
