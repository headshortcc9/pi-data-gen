import random


full_names = []
first_names=('Trình','Quân','Thức','Lĩnh','Nguyệt','Thảo','Thủy','Thuận')
last_names=('Phùng','Lý','Mạc','Nguyễn','Phan','Cao','Bế','Võ')
middle_names=('Văn','Xuân','Minh','Chí','Thị','Tấn','Bá')

append_string = "Pi "
i = 0
phone_number = 2363512001
f = open("account-phone-3105.csv", "a")
while i < 1001:
    pi_name=str('{0:03}'.format(i))
    pi_code=str('{0:04}'.format(i))
    append_string += pi_name + ',+84' ',' +\
                    str(phone_number) + ',' +\
                    'Piclone2@' + pi_code + ',' +\
                    random.choice(middle_names)+" "+random.choice(first_names) + ',' +\
                    random.choice(last_names) + ',' +\
                    'Piclone2' + pi_code + ',' +\
                    'thanhnd1982' + ',' + '1' + '\n'
    f.write(append_string)


    #print(append_string)
    i+=1
    phone_number+=1
    append_string = "Pi "


f.close()
