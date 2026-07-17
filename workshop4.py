gang_members = []
def add_member(name,age,gang_name):
    member = {
        "name": name,
        "age": age,
        "gang_name": gang_name

    }
    gang_members.append(member)

while True:
    data=input("1.add,2.watch,3.logout : ")
    if data=="1":
        name_nong=input("ใส่ชื่อ : ")
        age_nong=int(input("ใส่อายุ : "))
        gang_name = input("ใส่ชื่อแก้ง : ")
        add_member(name_nong,age_nong,gang_name) 
        print("สำเร็จ")
    elif data=="2":
        print(gang_members)
    else:
        print("logout")
        break             
               
               