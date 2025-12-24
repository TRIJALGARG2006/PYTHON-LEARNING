import csv 

with open('csv pratics/marks.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


new_student = [['Manas', '92', 'Pass'],['uday','87','pass'],['harsh','90','fail']]

with open('csv pratics/marks.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    
    # Write the new row
    writer.writerows(new_student)

print("Data added! Open marks.csv to see Manas at the bottom.")
