import glob

print("enter the year: ")
yr = input()
print("enter the month: ")
mon = input()
print("enter the day: ")
day = input()

file = 'C:\Battlestate Games\Logs\log_YR.MM.DD*\\YR.MM.DD*application.log'
file = file.replace('YR', yr, 4)
file = file.replace('MM', mon, 2)
file = file.replace('DD', day, 2)

#print(file)

#filename = "2021.MM.DD*application.log"
#filename = filename.replace("MM", mon)
#filename = filename.replace("DD", day)

file = glob.glob(file)

file_size = len(file)

#print(file)
#print(file_size)
i = 0
count = 0
check = 0

while i < file_size:
    with open(file[i], 'r') as input:
        for line in input:
            if check == 2:
                s = int(line[11])
                t = int(line[12])
                u = int(line[14])
                v = int(line[15])
                j = s*1000 + t*100 + u*10 + v
                total = j-j2
                if (t != t2):
                    total = total-40
                print ("game time: ", total)
                check = 0
            if check == 3:
                check = 2
            if check == 4:
                check = 3
            if check == 1:
                s2 = int(line[11])
                t2 = int(line[12])
                u2 = int(line[14])
                v2 = int(line[15])
                j2 = s2*1000 + t2*100 + u2*10 + v2
                check = 4
            if 'GameStarted:' in line:
                check = 1
                
    i +=1
            
            
