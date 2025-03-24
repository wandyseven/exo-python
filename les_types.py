my_var = 42 # entier
print(type (my_var),my_var)

my_var = "21" # string
print(type (my_var),my_var)

my_float = 3.14
my_bool = True
my_none = None

# Composes
my_list = [1,2,3,"4"] # types heterognes
print(my_list[0]) # 1
print(my_list[1:3]) # [2,3]

my_list = my_list + [5,6]
print(my_list) # [1,2,3,"4",5,6]

#help(list)

#tuples
my_tuple = (1,2,4,"5")
#my_tuple[0] = 42 # erreur

#dictionnaires 
my_dict = {"cle":"valeur","nom":"Yohan","age":34,100:42}
print("Bonjour",my_dict["nom"])
