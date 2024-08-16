import random


full_names = []
first_names=('Trình','Quân','Thức','Lĩnh','Nguyệt','Thảo','Thủy','Thuận')
last_names=('Phùng','Lý','Mạc','Nguyễn','Phan','Cao','Bế','Võ')
middle_names=('Văn','Xuân','Minh','Chí','Thị','Tấn','Bá')


i = 0
cccd = '031095'
append_string = cccd
f = open("cccd.csv", "a")
while i < 10:
    append_string +=  str(random.randint(1, 9))+str(random.randint(1, 9))+str(random.randint(1, 9))+str(random.randint(1, 9))+str(random.randint(1, 9))+str(random.randint(1, 9))+"\n"
    f.write(append_string)
    append_string = cccd
    i+=1
f.close()

