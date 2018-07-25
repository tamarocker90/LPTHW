i = 0
numbers = []
"""
def number_print(loop, numbers):
    i = 0
    
    
    while i < int(loop):
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = i + 1
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i
    
    return numbers

number_print(6, numbers) 
"""

def second_print (i, numbers):
    print "At the top i is %d" % i
    numbers.append(i)
    print "Numbers now:", numbers
    print "At the bottom i is %d" % i
    return numbers

while i < 6:
    #print i 
    second_print(i, numbers)
    i += 1
    #print i
    #raw_input('')
    
print "The numbers: "

for num in numbers:
    print num


