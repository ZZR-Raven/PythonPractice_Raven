import csv

with open('04.csv',encoding = 'utf-8')as csv_1:
    #using reader
    csv_1_read = csv.DictReader(csv_1)         
    #row0 = [row['now_ec45_current'] for row in csv_1_read]    
    #time = [row['Timestamp']for row in csv_1_read]
    #now_current = [row['now_ec45_current' ]for row in csv_1_read]
    #now_rpm = [row['now_ec45_rpm' ]for row in csv_1_read]
    #target_rpm = [row['ec45_target_rpm' ]for row in csv_1_read]




