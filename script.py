import bpy

cube_no = 10
x = 0
for i in range(cube_no):
    x+=2
    y = 0
    for j in range(cube_no):
        y += 2
        z = 0
        for k in range(cube_no+10):
            bpy.ops.mesh.primitive_cube_add(size =2, location=((x-2), (y-2), (z+2)))
            z += 2
            bpy.ops.rigidbody.object_add()
            bpy.context.object.rigid_body.mass = 25
            bpy.context.object.rigid_body.collision_shape = 'BOX'
            bpy.context.object.rigid_body.friction = 1
            bpy.context.object.rigid_body.use_margin = True
            bpy.context.object.rigid_body.angular_damping = 0.5
            bpy.context.object.rigid_body.linear_damping = 0.3
            