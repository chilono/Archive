# greedy.py
# 贪婪算法


# 需要覆盖的州
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# 广播台清单
stations = {
	'kone':  set(['id', 'nv', 'ut']),
	'ktwo':  set(['wa', 'id', 'mt']),
	'kthree':set(['or', 'nv', 'ca']),
	'kfour': set(['nv', 'ut']),
	'kfive': set(['ca', 'az'])
}

# 最终广播台名单
final_stations = set()

def BestStation(station, states_needed):
	best_station = None		# 当前最佳广播台
	states_covered = set()	# 当前广播台覆盖状态
	for station, states_for_station in stations.items():
		covered = states_needed & states_for_station	# 计算交集，结果为覆盖状态
		if len(covered) > len(states_covered):			# 比较覆盖状态是否比当前广播台好
			best_station = station						# 把广播台赋值给最佳广播台
			states_covered = covered					# 把覆盖状态给最佳覆盖状态
	states_needed -= states_covered						# 减去本次已覆盖的范围
	final_stations.add(best_station)
	return best_station									# 返回最佳广播台


while states_needed:
	result = BestStation(stations, states_needed)
	print(result, stations[result])