file = open("weather_data.txt")

skip = 1

line = file.readline()
data = {}
while line:
    user_data = line.strip().split()
    if skip == 1:
        skip = 0
    else:
        data[user_data[0]] = {"Temperature (°C)" : float(user_data[1]) , "Humidity (%)" : float(user_data[2]), "Wind Speed (km/h" : float(user_data[3])}
    line = file.readline()

suma = 0 
key = next(iter(data))
minimum = data[key]["Humidity (%)"]
for i in data:
    suma = suma +  data[i]["Temperature (°C)"]
    if data[i]["Humidity (%)"] < minimum:
        minimum = data[i]["Humidity (%)"]
print("srednia temp to ", suma / len(data))
print("min to ", minimum)
