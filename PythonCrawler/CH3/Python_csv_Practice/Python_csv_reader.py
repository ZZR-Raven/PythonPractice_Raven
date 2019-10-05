import csv

with open('04.csv',encoding = 'utf-8')as csv_1:
    #using reader
    csv_1_read = csv.reader(csv_1)
    time = [row[0] for row in csv_1_read]
    target_rpm = [row[1] for row in csv_1_read]
    now_current = [row[2] for row in csv_1_read]
    now_rpm = [row[3] for row in csv_1_read]
    #print(time)

with open ('wright.csv','w',encoding = 'utf-8') as csv_2:
    writer = csv.DictWriter(csv_2,fieldnames = ['time','target_rpm','current','rpm'])
    writer.writeheader()

    #学pandas包吧
    #writer.writerow(time) #只接收dict
    #writer.writerow

