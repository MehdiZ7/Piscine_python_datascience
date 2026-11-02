def all_thing_is_obj(object: any) -> int:
	ft_type = type(object)
	if (ft_type == str):
		print(f"{object} is in the kitchen : {ft_type}")
	elif (ft_type == list) :
		print(f"List : {ft_type}")
	elif (ft_type == tuple) :
		print(f"Tuple : {ft_type}")
	elif (ft_type == set) :
		print(f"Set : {ft_type}")
	elif (ft_type == dict) :
		print(f"Dict : {ft_type}")
	else :
		print("Type not found")
	return 42

