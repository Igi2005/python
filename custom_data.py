file = open("custom_data.txt")

skip = 1

line = file.readline()
data = {}
while line:
    user_data = line.strip().split(";")
    if skip == 1:
        skip = 0
    else:
        data[user_data[0]] = {"Name" : user_data[1] , "Surname" : user_data[2], "Grade" : user_data[3]}
    line = file.readline()
print(data)