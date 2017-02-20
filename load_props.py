import utils

props = utils.Properties()
props.load("input.props")

for prop in props.keys():
	print prop+"\t"+props.get(prop)

list = utils.convert_float_list(props.get("list"),",")
print list