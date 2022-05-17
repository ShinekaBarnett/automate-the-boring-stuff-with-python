def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    
spam()
bacon()               

def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)

def spam():
    global eggs
    eggs = 'spam' #global

def bacon():
    eggs ='bacon' #local

def ham():
    print(eggs) #global

eggs = 42   #global
spam()
print(eggs)

