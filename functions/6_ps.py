def substring(data_list, target_word):
    new_list = []
    
    for item in data_list:
        modified_item = item.replace(target_word, "")
        new_list.append(modified_item)
        
    return new_list

data_list = ["trijal" , "fuck" , "fucker" , "et" , "entab"]

name = ["trijal", "ayush" , "prithvee"]

a = input("enter the list you wanna fuck up ")

print(substring(a,"e"))
