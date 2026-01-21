import csv

with open("data_csv.csv","w",newline = '') as file:
    csv_writer = csv.writer(file, delimiter=';')
    header = ["Date", "Product", "Units Sold", "Price per Unit"]
    sales_data = [
        ("2023-10-01", "Laptop", 5, 1200.0),
        ("2023-10-01", "Phone", 10, 500.0),
        ("2023-10-02", "Laptop", 3, 1200.0),
        ("2023-10-02", "Phone", 7, 500.0),
        ("2023-10-03", "Laptop", 4, 1200.0),
        ("2023-10-03", "Phone", 12, 500.0),
    ]
    csv_writer.writerow(header)
    for i in sales_data:
        csv_writer.writerow(i)

with open("data_csv.csv") as file:
    suma = 0
    data = csv.reader(file, delimiter=';')
    skip = 1
    for i in data:
        if skip == 1:
            skip = 0
        else:
            suma = suma + float(i[3])
    print("suma to ", suma)