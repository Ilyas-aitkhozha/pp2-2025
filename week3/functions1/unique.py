def unique_list(list):
    new_list = []
    for i in list:       
        if i not in new_list:
            new_list.append(i)
    print(new_list)
list = [1, 2, 3, 3, 2, 5, 9, 10, 9]
unique_list(list)