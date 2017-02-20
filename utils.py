class Properties:
	properties = {}
	def __init__(self):
		properties = {}

	def load(self, filename):
		
		f = open(filename)
		for line in f:
			tokens = line.split("=")
			self.put(tokens[0].strip(), tokens[1].strip())

	def get(self, key):
		return self.properties[key]

	def put(self, key, value):
		self.properties[key] = value

	def keys(self):
		return self.properties.keys()

	def put_all(self, other):
		for key in other.keys():
			self.properties.put(other.get(key))

def convert_str_list(str, delim):
	return str.split(delim)

def convert_int_list(str, delim):
	return [int(x) for x in str.split(delim)]

def convert_float_list(str, delim):
	return [float(x) for x in str.split(delim)]
	