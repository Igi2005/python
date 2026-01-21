try:
    file = open("file.txt")
    line = file.readline()

    while line:
        print(line.strip())
        line = file.readline()
    file.close()
except FileNotFoundError:
    print("nie znaleziono pliku")

file = open("file.txt","a")
for i in range(0,5):
    data = input("wpisz dane")
    if data != "\n":
        file.write(data+"\n")