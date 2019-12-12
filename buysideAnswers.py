def countUppercase(file):
    upper_case_count = 0

    with open(file,'r') as input_file:
        for line in input_file:
            upper_case_count += sum([char.isupper() for char in line])
    return upper_case_count


def fibonacci(n):
    if n<=2:
        return 1

    a,b = 1,1
    for i in range(3,n+1):
        c = a+b
        a = b
        b = c

    return b


def extract_ids(data):
    extracted_ids = [item["id"] for item in data]
    return sorted(extracted_ids)


def transformdata2(data):
    #extracted_ids = [item["id"] for item in data]
    extracted_ids = extract_ids(data)
    extracted_names = sorted([item["name"] for item in data],reverse=True)
    return [(extracted_ids[i],extracted_names[i]) for i in range(len(extracted_ids))]


def mergeDicts(a, b):
    temp = a.copy()
    for key,val in b.items():
        if key not in a:
            temp[key]=val

    return temp
