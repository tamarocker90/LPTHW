ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

#prints string at stuff location 1
print stuff[1]
#prints last string stored in stuff
print stuff[-1]
#prints last string stored in stuff
print stuff.pop()
#prints all strings in stuff delimited by a space
print ' '.join(stuff)
#prints strings located at 3 and 5, delimited by a '#'
print '#'.join(stuff[3:5])

