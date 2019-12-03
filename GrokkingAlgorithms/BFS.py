# BFS.py
# 广度优先搜索

from collections import deque		# 引入队列模块


# 测试数据
graph = {}
graph['你'] = ['爱丽丝', '鲍博', 'claire']
graph['爱丽丝'] = ['prggy']
graph['鲍博'] = ['anuj', 'prggy']
graph['claire'] = ['jonny', 'tho']
graph['prggy'] = []
graph['anuj'] = []
graph['tho'] = []
graph['jonny'] = ['你']


# 搜索你的人际关系网
def search(name):
	search_queue = deque()
	search_queue += name
	searched = []		# 检查过的记录

	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print(person + "是芒果销售商")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
		print(search_queue)
		print(searched)
	print("你的朋友里没有卖芒果的")
	return False

def person_is_seller(name):
	return name[-1] == 'm'	# 名字结尾是m的人就是卖芒果的


search('你')