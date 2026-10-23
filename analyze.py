import csv
import time

def check(csv_name):
    with open(csv_name,'r',newline='') as f:
        reader = csv.DictReader(f)
        sum_list = []
        for row in reader:
            if row['interval'] != '':
                sum_list.append(float(row['interval']))
        result = sum(sum_list) / len(sum_list)
        print('평균 interval:',result)

csv_name = input('csv 파일 이름:')
check(csv_name)