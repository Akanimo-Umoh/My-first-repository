person = {"dict1":{"name":"udeme"},"dict2":{"age":12},"dict3":{"complexion":"dark"}}
for key, value in person.items():
    """accessing the key in the nested dictionary"""
    print (key)
    for key in value.keys():
        """accessing the key in the values"""
	    print (key)
    for value in value.values():
        print (value)