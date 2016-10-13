class Car(object):
	"""
		Car class that instantiates various vehicle types
		
		Attributes:
			type: The type of vehicle as a string
			model: The model of the car as a string
			name: String representing the name of the car
	
	"""

	speed = 0
	
	def __init__(self, name = "General", model = "GM", type = "saloon"):
		self.type = type
		self.model = model
		self.name = name
	
	@property
	def num_of_doors(self):
		if self.name == "Porshe" or self.name == "Koenigsegg":
			print 2
		print 4

	@property
	def num_of_wheels(self):
		if self.type != "trailer":
			return 4
		return 8

	def is_saloon(self):
		if self.type == "saloon":
			return True
		return False

	def drive(self, i=None):
		if self.name == "Mercedes":
			self.speed = 1000
		elif self.type == "trailer":
			self.speed = 77
		else:
			self.speed = 72
		return self
