import pymysql as ps

#*********************Creating Database******************************
# 1.Comment all program and only run "Creating Database" Block.

# conn = ps.connect(host='localhost',user='root',password='omkar')
# c = conn.cursor()
# cr_database = "create database contact"
# c.execute(cr_database)
# print('Database Created!')

##*********************Creating Table******************************
# 2.Comment "Creating Database" block and uncomment "Creating Table" Block

# conn = ps.connect(host='localhost',user='root',password='omkar',database='contact')
# c = conn.cursor()
# try:
#     cr_table = 'create table contactdetails(Name varchar(20) NOT NULL,Address varchar(50) NOT NULL,Phone INT NOT NULL)'
#     c.execute(cr_table)
#     print('Table Created Succesfully')
# except:
#     print('Error while Creating Tables!')

#**********************Code************************************
#3.Now comment the "creating Database and Table" Block and Uncomment Code and run the program.

conn = ps.connect(host='localhost',user='root',password='omkar',database='contact')
c = conn.cursor()

while True:
    try:
        choice = int(input('''
                            1.Add Contact
                            2.Search Contact
                            3.Display all Contact
                            4.Modify Contact
                            5.Delete Contact
                            6.Exit : '''))
    except:
        print('----------------------------------')
        print('Warning : Enter Valid Input')
        print('----------------------------------')
        choice=''

    if choice == 1:
        try:
            name = input('Enter Name : ').upper()
            while True:
                if name == '':
                    print('----------------------------------')
                    print('Warning : Name Field Cannot be empty!')
                    print('----------------------------------')
                    name = input('Enter Name : ').upper()
                else:
                    break
                if name in contact:
                    print('----------------------------------')
                    print('Alert : Contact Name Already Exists!\n')
                    print('----------------------------------')
                    continue
            address = input('Enter Address : ').strip()
            while True:
                if address == '':
                    print('----------------------------------')
                    print('Warning : Address Field Cannot be empty!')
                    print('----------------------------------')
                    address = input('Enter Address : ').upper()
                else:
                    break
            phone_no = input('Enter Contact Number : ').strip()
            while True:
                if not phone_no.isdecimal():
                    print('----------------------------------')
                    print('Warning : Phone Number should only contain digits!')
                    print('----------------------------------')
                    phone_no = input('Enter COntact Number : ').strip()
                    continue
                if phone_no[0] != '8' and phone_no[0] != '9':
                    print('----------------------------------')
                    print('Warning : Phone Number should begin with 8 or 9!')
                    print('----------------------------------')
                    phone_no = input('Enter Contact Number : ').strip()
                    continue
                if len(phone_no) != 10:
                    print('----------------------------------')
                    print('Warning : Phone Number Should be of 10 Digits!')
                    print('----------------------------------')
                    phone_no = input('Enter Contact Number : ').strip()
                    continue
                break

            ins_data = 'INSERT into contactdetails values(%s,%s,%s)'
            tuple_data = (name,address,phone_no)
            c.execute(ins_data,tuple_data)
            conn.commit()
            print('Contact Added Successfully')

        except:
            print('Error while adding Contact')

    if choice == 2:
        try:
            name = input('Enter Name : ').upper()
            search_contact = "select * from contactdetails where Name = '"+name+"'"
            c.execute(search_contact)
            data = c.fetchall()
            if len(data) > 0:
                for i in data:
                    print("Name:{}\nAddress:{}\nPhone:{}".format(i[0],i[1],i[2]))
            else:
                print(f'Their is no Contact with name {name}')
        except:
            print('Their is some error')
            continue

    if choice == 3:
        try:
            dis_contact = "select * from contactdetails"
            c.execute(dis_contact)
            print('----------------------------------------------')
            print("{:15} {:15} {:15}".format("Name","Address","Phone No"))
            print('----------------------------------------------')
            data = c.fetchall()
            for i in data:
                print("{:15} {:15} {:15}".format(i[0],i[1],i[2]))
        except:
            print('Error While Displaying Data')
            continue

    if choice == 4:
        try:
            name = input('Enter Name : ').upper()
            search_contact = "select * from contactdetails where Name = '" + name + "'"
            c.execute(search_contact)
            data = c.fetchall()
            if len(data) > 0:
                phone_no = input('Enter New Contact Number : ').strip()
                mod_contact = "update contactdetails set Phone = %s where Name = %s"
                tuple_data = (phone_no,name)
                c.execute(mod_contact,tuple_data)
                conn.commit()
                print(f'Phone no of {name} is updated to {phone_no}')
            else:
                print(f"{name} is not in Contact")
        except:
            print('Error while Modifying Number')

    if choice == 5:
        try:
            name = input('Enter Name : ').upper()
            search_contact = "select * from contactdetails where Name = '" + name + "'"
            c.execute(search_contact)
            data = c.fetchall()
            if len(data) > 0:
                del_contact = "delete from contactdetails where Name = '"+name+"'"
                c.execute(del_contact)
                conn.commit()
                print('Deleted Contact Succesfully')
            else:
                print(f"{name} is not their in contact to delete!")
        except:
            print('Error while Deleting')
    if choice == 6:
        print('Thank You For using CONTACT BOOK')
        break