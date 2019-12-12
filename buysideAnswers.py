def countUppercase(file):
    input_file = open(file,'r')
    upper_case_count = 0

    for line in input_file:
        for char in line:
            if char.isupper():
                upper_case_count+=1

    input_file.close()
    return upper_case_count


def fibonacci(n):    
    a,b = 1,1

    if n<=2:
        return 1

    for i in range(3,n+1):
        c = a+b
        a = b
        b = c

    return b


def extract_ids(data):
    extracted_ids = [item["id"] for item in data]
    return sorted(extracted_ids)


def transformdata2(data):
    extracted_ids = extract_ids(data)
    extracted_names = sorted([item["name"] for item in data],reverse=True)
    return [(extracted_ids[i],extracted_names[i]) for i in range(len(extracted_ids))]


def mergeDicts(a, b):
    for key,val in b.items():
        if key not in a:
            a[key]=val
    
    return a
