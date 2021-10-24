import json


def menu():
    print("*"*25)
    print("Registration system")
    print("*"*25)
    print("1. Insert Data")
    print("2. Show Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("0. Exit Program")
    print("*"*25)

def GPA(list):   #GPA per one kid
    sum = 0
    classes = 0
    grade = 0
    for score in list:
        if score >= 80:
            grade = 4.0
        elif score >=75:
            grade = 3.5
        elif score >= 70:
            grade = 3.0
        elif score >= 65:
            grade = 2.5
        elif score >= 60:
            grade =2.0
        elif score >= 55:
            grade = 1.5
        elif score>= 50:
            grade = 1.0
        elif score<50:
            grade = 0.0

        sum = sum+ grade
        classes = classes+1
    Gpa = float(sum/classes)
    return Gpa

def save_data():
    with open("db.txt","w")as f:
        w =json.dumps(database)  # or json.dump(database,f)
        f.write(w)
def load_data(): # load data from db.txt to use again in python
    with open("db.txt","r")as f:
        global database
        try:
            database=json.loads(f.read())  # or database = json.load(f)
        except:
            pass


def insert_data():
    Exit = "n"
    while Exit =="n":
        sid = input("Enter student SID: ")
        name = input("Enter student Name: ")
        email = input("Enter student Email: ")
        while True:
            try:
                math_score = float(input("Enter Math Score: "))
                break
            except:
                pass
        physics_score = float(input("Enter Physics Score: "))
        computer_score = float(input("Enter Computer Score: "))
        Total_Score = [math_score,physics_score,computer_score]
        gpa = GPA(Total_Score)
        information =[name,email,math_score,physics_score,computer_score,gpa]
        database[sid] = information       # Add data to database
        Exit = input("Press 'n' to insert next student/ else press any button")
    else:
        save_data()
        print("Exit from insert data!")
        # WHY SOME OF FUNCTION DOESN"T NEED RETURN STATEMENT

def del_data():
    sid = input("Enter the student SID that you want to delete") # so if I print SID out in function, will it bring from global? or do nothing
    if sid in database:
        del database[sid]
        print("The ", sid, "has been deleted")
    else:
        print("Not Found!")
        return # so the program doesn't save this
    save_data()

def update_data():
    sid = input("Enter the student SID that you want to update: ")
    if sid in database:
        info = database[sid]
        info[0] = input("Enter student Name: ")
        info[1] = input("Enter student Email: ")
        info[2] = float(input("Enter Math Score: "))
        info[3] = float(input("Enter Physics Score: "))
        info[4] = float(input("Enter Computer Score: "))
        Score = info[2:5] # variable[x:y] loop through
        info[5] = GPA(Score)

        #There is no way changing dictinary data
    else:
        print(sid," doesn't exist")
        return

    save_data()

def show_data():
    for sid in database:
        detail = database[sid]
        name = detail[0]
        email = detail[1]
        math = detail[2]
        physics = detail[3]
        computers = detail[4]
        gpa = detail[5]
        print(sid+":"+name+","+email+","+str(math)+","+str(physics)+","+str(computers)+","+str(gpa))




database={}

menu()

load_data() #?? before program is error because "#"split was . instead?
accept = 0
while True:
    try:
        accept = int(input("Enter your choice"))
        break
    except ValueError:
        print("Try Again")
        continue

while accept != 0: # What is this yellow highlight
    if accept == 1:
        insert_data()
    elif accept == 2:
        show_data()
    elif accept == 3:
        update_data()
    elif accept == 4:
        del_data()
    else:
        print("error")
    menu()
    while True:
        try:
            accept = int(input("Enter your choice again"))
            break
        except ValueError:
            print("Try Again")
            continue


