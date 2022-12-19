import csv
path = "./"

csv_Cursor = open(f'{path}stores.csv', 'w', newline='',encoding='utf-8')

header = ['s_id','name','locate','products_num','password']
student1 = ['s1','용산점','용산',6,]
student2 = ['s2','강남점','강남',3,]
student3 = ['s3','강북점','강북',4,]


students = [header,
            student1,
            student2,
            student3
            ]

wr = csv.writer(csv_Cursor)
for idx in students:
    wr.writerow(idx)

csv_Cursor.close()
