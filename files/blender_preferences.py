import bpy
from bpy.types import Object
from mathutils import Vector

# Create a cube
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
cube: Object | None = bpy.context.active_object  # Get the active object (the cube)

# Create a sphere
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(3, 0, 0))
sphere: Object | None = bpy.context.active_object  # Get the active object (the sphere)

# Create a monkey (Suzanne)
bpy.ops.mesh.primitive_monkey_add(size=1, location=(6, 0, 0))
monkey: Object | None = bpy.context.active_object  # Get the active object (the monkey)

# Output names and positions of the created objects
for obj in [cube, sphere, monkey]:
    name: str = obj.name
    location: Vector = obj.location
    print(f"Object Name: {name}, Position: {location}")

print(bpy.context.preferences.themes['Default'].view_3d.vertex_size)

# bpy.context.preferences.view.show_developer_ui = False
# bpy.context.preferences.view.show_tooltips_python = False
# bpy.context.preferences.view.ui_line_width = "AUTO"
# bpy.context.preferences.edit.use_negative_frames = True
# bpy.context.preferences.themes['Default'].view_3d.vertex_size = 5
# bpy.context.preferences.themes['Default'].view_3d.grid = Color((0.365, 0.447, 0.498, 0.106))
# bpy.context.preferences.themes['Default'].view_3d.space.gradients.background_type = "RADIAL"
# bpy.context.preferences.themes['Default'].view_3d.space.gradients.high_gradient = Color((0.157, 0.055, 0.231))
# bpy.context.preferences.themes['Default'].view_3d.space.gradients.gradient = Color((0.110, 0.110, 0.1))
# bpy.context.preferences.edit.undo_steps = 512
# bpy.context.preferences.filepaths.save_version = 10

# bpy.data.scenes["Scene"].tool_settings.lock_object_mode = False
# bpy.ops.preferences.addon_enable(module="node_wrangler")
