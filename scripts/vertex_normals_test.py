import bpy
from mathutils import Vector

aodata = bpy.context.active_object.data

vertex_normals = {index: ([], vtx.normal)  for index, vtx in enumerate(aodata.vertices)}

for polygon in aodata.polygons:
    for vertex_index in polygon.vertices:
        face_normals = vertex_normals[vertex_index][0]
        face_normals.append(polygon.normal)


face_normals, pre_calculated_vertex_normal = vertex_normals[0]

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
