# By guoshu 
# 2014/7/18 22:06

#code=utf-8

# create a basic ste of states and some cities in them
cities = {
'CA':'San Francisco',
'MI':'Detroit',
'FL':'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found"

# OK, pay attention!
# 这里是把函数加入字典，看来字典可以加入任何东西。。
cities['_find'] = find_city

while True:
	print "State?(ENTER to quit)",
	state = raw_input(">")

	if not state: break

	#this line is the most important ever! study!
	#guoshu:这里cities['_find'](值是function)等同于def find_city
	city_found = cities['_find'](cities,state)
	print city_found