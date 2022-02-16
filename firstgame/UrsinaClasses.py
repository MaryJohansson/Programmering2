from ursina import *

class Voxel(Button):
	def __init__(self, position):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = "sky_sunset",
			color = color.cyan,
			scale = 1)