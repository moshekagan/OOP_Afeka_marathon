import csv

with open('example_csv_file.csv', "r") as csvfile:
    reader = csv.reader(csvfile)

    next(reader)

    sum_grads = 0
    count = 0

    for row in reader:
        grade = int(row[1])
        sum_grads += grade
        count += 1

    print(sum_grads/count)


