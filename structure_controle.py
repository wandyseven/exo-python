#Les conditions 
"""
if condiction:
    intruction 1
    intruction 2
    ...
else:
    intr 1
    ...
"""

age = 17

if age >= 18 :
    print ("yous pouvez voter")
elif age <= 16:
    print("il faut etre emancipe")
else:
    print("vous etes trop jeune")

# Les boucles (for/while)

for i in range(10):
    print('*' * i)

my_collection = [1,2,3]
for element in my_collection :
    print(element)

i = 9
while i > 0:
    print('*' * i)
    i -= 1
