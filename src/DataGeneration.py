import csv
import time

csvfile = "Alldatas.csv"

# Collect data from RPI and send it over to WriteData to be writen into csvfile
def DataGeneration(Temperature, Humidity, Moisture_sensor, Potentiometer, LDR):
    Time = (time.time() + 28800000) * 1000
    WriteData([Time, Temperature, Humidity, Moisture_sensor, Potentiometer, LDR])
    return [Time, Temperature, Humidity, Moisture_sensor, Potentiometer, LDR]

# Write the field names of a new csvfile
def WriteFieldNames():
    with open(csvfile,"w") as file:
        writer = csv.writer(file)
        Data = ["Time", "Temperature", "Humidity", "Moisture_sensor", "Potentiometer", "LDR"]
        writer.writerow(Data)
    return

# Write data to csvfile
def WriteData(Datas):
    # changing Moisture_sensor data from True/False to 1.0/0.0
    if Datas[3]:
        Datas[3] = 1.0
    else:
        Datas[3] = 0.0

    # Append the data from RPI into csvfile
    with open(csvfile, 'a', newline="") as Data:
        print(Datas)
        writer = csv.writer(Data)
        writer.writerow(Datas)
    return

# Read the specified line of the csvfile
def ReadLine(csvfile,line):
    data = []
    with open(csvfile, "r") as csvfile:
        reader = csv.reader(csvfile)
        for _ in range(line - 1):
            next(reader)
        for i in next(reader):
            data.append(float(i))      
    return data

# Read the LatestLine of the csvfile
def LatestLine(csvfile):
    totallines = 0
    with open(csvfile,"r") as file:
        reader = csv.reader(file)
        totallines = sum(1 for row in reader)
    print(totallines)
    if totallines > 20:
        line = totallines - 20
    else:
        line = 3
    return line

# Create a new csv file everyday with that day datas
def save_to_csv(current_date):

    filename = str(current_date) + ".csv"
    csv_file_path = "Alldatas.csv"

    # Read the CSV data from the file and directly upload it to folder "datalogs"
    with open(csv_file_path, 'r') as current:
        reader = csv.reader(current)
        with open("./datalogs/" + filename,'w',newline="") as past:
            writer = csv.writer(past)
            for row in reader:
                writer.writerow(row)

    return

#Testing data logging
def main():
    save_to_csv("2023-08-09")

if __name__ == "__main__":
    main()