def dataAgentSplit(json_obj):
	# Splits agents and appends only their authority ids to a list
	try:
		agent_data = []
		agents = json_obj['agent_subject_name'].split(';')
		for agent in agents:
			agent_dic = {}
			agent = agent.split('|')
			auth_id = str(agent[-1])
			name = str(agent[0])
			source = str(agent[1])
			agent_dic['name'] = name
			agent_dic['source'] = source
			agent_dic['id'] = auth_id
			agent_data.append(agent_dic)
		json_obj['agent_subject_name'] = agent_data

	except:
		pass

	return json_obj


def dataSubjectSplit(json_obj):
	# Splits subjects and appends only their authority ids to a list
	try:
		subs_topic = []
		topic_subjects = json_obj['subjects_topic'].split(';')
		for sub in topic_subjects:
			sub_dic = {}
			sub = sub.split('|')
			sub_id = str(sub[-1].strip())
			name = str(sub[0].strip())
			source = str(sub[1].strip())
			sub_dic['name'] = name
			sub_dic['source'] = source
			sub_dic['id'] = sub_id
			subs_topic.append(sub_dic)
		json_obj['subjects_topic'] = subs_topic

	except:
		pass

	try:
		subs_geo = []
		geo_subjects = json_obj['subjects_geographic'].split(';')
		for sub in geo_subjects:
			sub_dic = {}
			sub = sub.split('|')
			sub_id = str(sub[-1].strip())
			name = str(sub[0].strip())
			source = str(sub[1].strip())
			sub_dic['name'] = name
			sub_dic['source'] = source
			sub_dic['id'] = sub_id
			subs_geo.append(sub_dic)
		json_obj['subjects_geographic'] = subs_geo

	except:
		pass

	try:
		subs_genre = []
		genre_subjects = json_obj['subjects_genre'].split(';')
		for sub in genre_subjects:
			sub_dic = {}
			sub = sub.split('|')
			sub_id = str(sub[-1].strip())
			name = str(sub[0].strip())
			source = str(sub[1].strip())
			sub_dic['name'] = name
			sub_dic['source'] = source
			sub_dic['id'] = sub_id
			subs_genre.append(sub_dic)
		json_obj['subjects_genre'] = subs_genre

	except:
		pass

	return json_obj


def dataAgentSubjectSplit(json_obj):
	# Calls agent and subject split functions together
	dataAgentSplit(json_obj)
	dataSubjectSplit(json_obj)

	return json_obj