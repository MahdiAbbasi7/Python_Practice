#git toturial test 
#git test 
import csv 
with open('source.csv') as f:
    reader = csv.reader(f)
    for i in reader:
        print(type(i))