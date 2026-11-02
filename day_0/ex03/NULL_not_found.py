def NULL_not_found(object: any) -> int :
    if object is None :
        print(f"Nothing: None {type(object)}")
    elif object != object :
        print(f"Cheese: nan {type(object)}")
    elif type(object) == bool and object is False :
        print(f"Fake: False {type(object)}")
    elif object == 0 :
        print(f"Zero: 0 {type(object)}")
    elif object == "" :
        print(f"Empty: {type(object)}")
    else :
        print("Type not Found")
        return 1
    return 0

