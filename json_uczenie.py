import json

data = None
with open("data.json") as file:
    full_data = json.load(file)

    name = input("Podaj imie")
    age = int(input("Podaj wiek"))
    department = input("Podaj department")
    salary = int(input("Podaj salary"))

    new_row = {
        "name" : name,
        "age" : age,
        "department" : department,
        "salary" : salary
    }
    full_data.append(new_row)
    data = full_data


with open("data.json","w") as file:
    data_to_add = json.dumps(data, indent = 4)
    file.write(data_to_add)