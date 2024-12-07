from PIL import Image, ImageDraw, ImageFont

import pandas as pd
import datetime
import qrcode
import pymysql


def project_header():
    d_date = datetime.datetime.now()
    print()
    reg_format_date = d_date.strftime(
        '  %d-%m-%Y\t\t\t\t ID CARD Generator/Viewer\t\t\t\t  %I:%M:%S %p\n\t\t\t\t\t\t\t\tBy Mohammed Aariz \t\t\t\t')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(reg_format_date)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def create_connection():
    # Establishing Connection with MySQL Server
    mydb = pymysql.connect(host='localhost', user='root', password='aazi8424')
    return mydb, mydb.cursor()


def create_database():
    # Creating Database and Table
    sql = 'create database if not exists idcard;'
    cursor.execute(sql)
    sql = 'use IdCard;'
    cursor.execute(sql)
    sql = "create table if not exists SavedCards (\
    ID INTEGER(20) AUTO_INCREMENT,\
    Org varchar(25),\
    Name varchar(25),\
    Gender varchar(10),\
    Age varchar(3),\
    DoB varchar(10),\
    BG varchar(10),\
    Mob varchar(10),\
    Address varchar(30), PRIMARY KEY (id));"
    cursor.execute(sql)


def important_information():
    print('\n\nFollow the given procedure to create New ID-Card...')
    print('\nImportant Note')
    print('\n1. All Fields are Mandatory')
    print('2. Avoid any kind of Spelling Mistakes')


def generate_uid(org, name, gender, age, dob, bg, mob, address):
    insert_sql = "INSERT INTO SavedCards (Org, Name, Gender, Age, DoB, BG, Mob, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    insert_val = (org, name, gender, age, dob, bg, mob, address)
    cursor.execute(insert_sql, insert_val)
    idcard_db.commit()
    return cursor.lastrowid


def generate_id_card(uid, org, name, gender, age, dob, bg, mob, address):
    template = Image.open('Template3.png')
    draw = ImageDraw.Draw(template)

    # Org Name
    font = ImageFont.truetype('garamond.ttf', size=85)  # font size for Org and ID
    W, _ = template.size
    w, _ = font.getsize(org)
    draw.text(((W - w) / 2, 5), str(org), font=font, fill='white')
    # Unique ID
    font = ImageFont.truetype('garamond.ttf', size=60)
    draw.text((860, 480), '#' + str(uid), font=font, fill='chocolate')
    # Other Details
    font = ImageFont.truetype('garamond.ttf', size=45)  # font size for rest inputs
    draw.text((70, 200), 'Name:   ' + str(name), font=font, fill='black')
    draw.text((70, 280), 'Gender:   ' + str(gender), font=font, fill='black')
    draw.text((490, 280), 'Age:   ' + str(age), font=font, fill='black')
    draw.text((70, 360), 'DoB:   ' + str(dob), font=font, fill='black')
    draw.text((70, 440), 'Blood Group:   ' + str(bg), font=font, fill='crimson')
    draw.text((70, 520), 'Phone No. :   ' + str(mob), font=font, fill='black')
    font = ImageFont.truetype('garamond.ttf', size=35)  # font size for Address (Smaller)
    draw.text((70, 600), 'Address:   ' + str(address), font=font, fill='navy')

    template.save('temp/' + str(name) + '.png')
    qrcode_ = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1)
    qrcode_.add_data(str(org) + '#' + str(uid) + '\n' + str(name))
    qrcode_.make(fit=True)
    img = qrcode_.make_image(fill_color="black", back_color="white")
    img.save('temp/' + str(uid) + '.svg')

    qr = Image.open('temp/' + str(uid) + '.svg').resize((236, 236))

    card = Image.open('temp/' + name + '.png')
    card.paste(qr, (856, 243, 1092, 479))
    card.save('exports/' + str.title(name) + ' #' + str(uid) + '.png')

    print('\nYour ID-Card is Successfully created with UID ' + str(uid) + ' in a PNG File  "' + str.title(
        name) + ' #' + str(uid) + '.png"')

def show_all_cards():
    show_sql = "SELECT * FROM savedcards;"
    cursor.execute(show_sql)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['ID', 'Org', 'Name', 'Gender', 'Age', 'DoB', 'BG', 'Mob', 'Address'])
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    print(df)


def id_search_with_uid(id_number):
    show_uid_sql = "SELECT * FROM savedcards WHERE ID = " + id_number + ";"
    cursor.execute(show_uid_sql)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['ID', 'Org', 'Name', 'Gender', 'Age', 'DoB', 'BG', 'Mob', 'Address'])
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    print(df)


def initial_input():
    print('\n\n>>> To Create New ID-Card, press "1"')
    print('>>> To View Saved ID-Cards, press "2"')
    print('>>> To View Saved ID-Card through UID, press "3"')
    initial_choice = str(input('\n--> Please Input: '))

    if initial_choice == '1':
        important_information()
        org, name, gender, age, dob, bg, mob, address = input_student_data()
        uid = generate_uid(org, name, gender, age, dob, bg, mob, address)
        generate_id_card(uid, org, name, gender, age, dob, bg, mob, address)

    elif initial_choice == '2':
        print('\nShowing all Saved ID-Cards...\n')
        show_all_cards()

    elif initial_choice == '3':
        uid_number = input('\n--> Please Input UID: ')
        print()
        id_search_with_uid(uid_number)

    else:
        print('\nWrong Command !! Kindly Follow the Instructions...')


def input_student_data():
    print('\n==================================================================================')
    org = input('Enter Your School Name: ')
    name = input('Enter Your Full Name: ')
    gender = input('Enter Your Gender: ')
    age = input('Enter Your Age: ')
    dob = input('Enter Your Date of Birth: ')
    bg = input('Enter Your Blood Group: ')
    mob = input('Enter Your Mobile Number: ')
    address = input('Enter Your Address: ')
    print('==================================================================================')

    return org, name, gender, age, dob, bg, mob, address


project_header()
idcard_db, cursor = create_connection()
create_database()
initial_input()

while True:
    print('\n\n>>> To Run the program again, press "R"\n>>> To Close the program, press "ENTER"')
    end_choice = input('\nPlease Input: ')
    if end_choice.lower() == 'r':
        initial_input()
    else:
        print('\n>>>>> Thanks for using ID-Card Generator <<<<<')
        break