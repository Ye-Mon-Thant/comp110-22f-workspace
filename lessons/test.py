def aap(o) -> str:
    vowel: str = "aeiou"
    new_string: str = ""
    i: int = 0
    while i < len(o):
        if (o[i] in vowel) and (i%3==0):
            pass
        elif (o[i] not in vowel) and (i%3!=0):
            pass
        else:
            new_string += o[i]
        i+=1
    return new_string

assert aap("aeiou") == "eiu"
assert aap("hello world") == "helowol"
assert aap("comp110") == "cop0"
            

def average(a: dict[str, list[int]]) -> dict[str, float]:
    new_dict = {}
    for i in a:
        total_grade = 0
        for s in a[i]:
            total_grade += s
        average_grade = total_grade / len(a[i])
        new_dict[i] = average_grade
    return new_dict

assert average({'Bill':[75, 94, 97], 'Annie': [88, 93, 99]}) == {'Bill': 88.66666666666667, "Annie": 93.33333333333333}


def best_animals(a: dict[str, list[int]]) -> list[str]:
    result: list[str] = []
    new_dict: dict[str, int] = {}
    for key in a.keys():
        total_value = 0
        i: int = 0
        while i < len(a[key]):
            total_value += a[key][i]
            i += 1
        total_value = total_value // 3
        new_dict[key] = total_value
    value_list: list[int] = []
    sorted_value_list: list[int] = []
    for keys in new_dict.keys():
        value_list.append(new_dict[keys])
    sorted_value_list.append(max(value_list))
    special_variable: int = min(value_list)
    for values in value_list:
        if values not in sorted_value_list or (values != special_variable):
            sorted_value_list.append(values)
        else:
            pass
    sorted_value_list.append(special_variable)
    s: int = 0
    if s < len(sorted_value_list):
        for final_keys in new_dict:
            if new_dict[final_keys] == sorted_value_list[s]:
                result.append(final_keys)
            else:
                pass
        s += 1
    return result
        
# assert best_animals({"bears":[2, 50, 300], "wolves": [10, 80, 400], "lions": [40, 70, 600]}) == ["lions", "wolves", "lions"]

def best_animals1(a):
    i = 0
    result = []
    while i < 3:
        a_list = []
        for keys in a:
            a_list.append(a[keys][i])
        for keys in a:
            if a[keys][i] == max(a_list):
                result.append(keys)
        i += 1
    return result

assert best_animals1({"bears":[2, 50, 300], "wolves": [10, 80, 400], "lions": [40, 70, 600]}) == ["lions", "wolves", "lions"]

dict1 = {'happy': True, 'blue': False}
dict2 = dict1
dict1 = {}
dict1['sad'] = False
print(dict1,dict2)

list1 = [1, 2, 3]
list2 = list1
list1 = []
list1.append(10)
print(list1, list2)

dict3: dict[str, list[int]] = {'happy':[1, 2, 3, 4, 10]}
for keys in dict3:
    i = 0
    while i < len(dict3[keys]):
        print(len(dict3[keys]))
        if dict3[keys][i] == max(dict3[keys]):
            print(dict3[keys][i])
        else:
            pass
        i += 1
dict1.pop('sad')
print(dict1)