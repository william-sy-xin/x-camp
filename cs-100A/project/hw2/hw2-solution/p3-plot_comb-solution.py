import turtle as t

#starting off the comb and running once only     
t.lt(45)
t.fd(40)
t.rt(90)

# Creating the teeth of the comb
for c in range(10): 
    t.fd(10)
    t.rt(90)
    t.fd(40)
    t.bk(40)
    t.lt(90)
    
t.fd(70) # creating the handle