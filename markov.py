import utils

def dfs(prev_state, prob, tick, state_list):
	global states
	global emmissions
	global transitionMat
	global emmissionMat
	global indexOf
	if tick == -1:
		return prob
	for next_state in states:
		state_list.append(next_state)
		for emmission in emmissions:
			next_state_prob =  prob * emmissionMat[indexOf[next_state]][indexOf[emmission]] * transitionMat[indexOf[prev_state]][indexOf[next_state]]
			state_list.append(emmission)
			dfs(next_state,next_state_prob, tick-1, state_list)
			state_list.pop()
		state_list.pop()


def get_index_of(array, indexOf):
	index = 0
	for entry in array:
		indexOf[entry] = index
		index+=1

	return indexOf

props = utils.Properties()
props.load("markov.props")

prev_state = props.get("start_state")
current_prob = float(props.get("seed_prob"))

states = utils.convert_str_list(props.get("states"),",")
emmissions = utils.convert_str_list(props.get("emissions"),",")
indexOf = get_index_of(states,{})
indexOf = get_index_of(emmissions,indexOf)
transitionMat = [[float(val) for val in arr.split(" ")] for arr in utils.convert_str_list(props.get("transitionMat"),",")]
emmissionMat = [[float(val) for val in arr.split(" ")] for arr in utils.convert_str_list(props.get("emissionMat"),",")]
time = int(props.get("time"))

state_list = []
state_list.append(prev_state)
dfs(prev_state, current_prob, time, state_list)


