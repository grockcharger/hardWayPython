# By guoshu 
# 2014/7/8 13:30

from sys import argv

script, user_name,user_nickname = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_nickname,script)
print "I'd like ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "wherer do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print '''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
''' % (likes,lives,computer)

