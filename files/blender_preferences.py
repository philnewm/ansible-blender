import bpy

preferences = bpy.context.preferences

preferences.view.show_splash = False
preferences.view.developer_ui = False
preferences.view.show_tooltips_python = False
preferences.view.ui_line_width = "AUTO"
preferences.edit.use_negative_frames = True
preferences.themes['Default'].view_3d.vertex_size = 5
preferences.themes['Default'].view_3d.grid = (0.365, 0.447, 0.498, 0.106)
preferences.themes['Default'].view_3d.space.gradients.background_type = "RADIAL"
preferences.themes['Default'].view_3d.space.gradients.high_gradient = (0.157, 0.055, 0.231)
preferences.themes['Default'].view_3d.space.gradients.gradient = (0.031, 0.035, 0.149)