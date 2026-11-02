ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# easy for a list
ft_list[1] = "World!"

#impossible to change a tuple. so a conversion is needed
new_list = list(ft_tuple)
new_list[1] = "France!"
ft_tuple = tuple(new_list)

#delete tutu then insert the correct value
ft_set.remove("tutu!")
ft_set.add("Paris!")

# need to change de value of the key hello
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
