name = "merine"
print (name) #unlike javascript you dont need semicolon



'''
you use three quotes to comment out a multi line statement in python

'''


#assigning same value to multiple variables on the same line

a=b=c=7;
print (a)
print(b)
print(c)


#reasigning values for variables
color="red"
color="blue"
print (color)


#reserved keywords

'''
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 


'''
#variables formats 


firstName = "Merine"
first_name = "Merine"
firstname = "Merine"
firstname2 = "Merine"
_first_name= "Merine"


#forbidden variable formats 
#7firstName ="Merine"
#-first-Name = "Merine"


#variable types
name = "merine"
print(type(name))


number =2
print (type(number))

# =======================
# garbage collection

# pb     ----------> int 20
# score  ----------> str 'Completed'
#        ----------> int 100

pb = 20
score = 100
score = 'Completed'

print(type(score))
print(type(pb))
print(score)
print(pb)