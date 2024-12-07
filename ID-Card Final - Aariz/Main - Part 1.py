from PIL import Image, ImageDraw, ImageFont

# import numpy as np
import pandas as pd
import random
import datetime
import qrcode
import csv
import pymysql

d_date = datetime.datetime.now()
print()
reg_format_date = d_date.strftime('  %d-%m-%Y\t\t\t\t ID CARD Generator/Viewer\t\t\t\t  %I:%M:%S %p\n\t\t\t\t\t\t\t\t By Mohammed Aariz \t\t\t\t')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(reg_format_date)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def new_card():
    template = Image.open('Template3.png')
    draw = ImageDraw.Draw(template)

    print('==================================================================================')

    # Org Name
    font = ImageFont.truetype('garamond.ttf', size=85)  # font size for Org and ID

    org = input('Enter Your School Name: ')
    W, _ = template.size
    w, _ = font.getsize(org)
    draw.text(((W - w) / 2, 5), str(org), font=font, fill='white')

    # Unique ID
    font = ImageFont.truetype('garamond.ttf', size=60)

    id = random.randint(1000000, 9000000)
    draw.text((860, 480), '#' + str(id), font=font, fill='chocolate')

    # Other Details
    font = ImageFont.truetype('garamond.ttf', size=45)  # font size for rest inputs

    name = input('Enter Your Full Name: ')
    draw.text((70, 200), 'Name:   ' + str(name), font=font, fill='black')

    gender = input('Enter Your Gender: ')
    draw.text((70, 280), 'Gender:   ' + str(gender), font=font, fill='black')

    age = input('Enter Your Age: ')
    draw.text((490, 280), 'Age:   ' + str(age), font=font, fill='black')

    dob = input('Enter Your Date of Birth: ')
    draw.text((70, 360), 'DoB:   ' + str(dob), font=font, fill='black')

    bg = input('Enter Your Blood Group: ')
    draw.text((70, 440), 'Blood Group:   ' + str(bg), font=font, fill='crimson')

    mob = input('Enter Your Mobile Number: ')
    draw.text((70, 520), 'Phone No. :   ' + str(mob), font=font, fill='black')

    font = ImageFont.truetype('garamond.ttf', size=35) # font size for Address (Smaller)

    address = input('Enter Your Address: ')
    draw.text((70, 600), 'Address:   ' + str(address), font=font, fill='navy')

    print('==================================================================================')

    template.save('temp/' + str(name) + '.png')
    qrcode_ = qrcode.QRCode (
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1 )
    qrcode_.add_data(str(org) + '#' + str(id) + '\n' + str(name))
    qrcode_.make(fit=True)
    img = qrcode_.make_image(fill_color="black", back_color="white")
    img.save('temp/' + str(id) + '.svg')

    qr = Image.open('temp/' + str(id) + '.svg').resize((236, 236))

    card = Image.open('temp/' + name + '.png')
    card.paste(qr, (856, 243, 1092, 479))
    card.save('exports/' + str.title(name) + ' #' + str(id) + '.png')

    print('\nYour ID-Card is Successfully created in a PNG File  "' + str.title(name) + ' #' + str(id) + '.png"')

    return template

def saved_cards():
    print('\n>>> To search saved ID-Card with Unique ID, press "1"')
    print('>>> To search saved ID-Card with Name, press "2"')
    schoice = str(input('\n-->Please Input: '))
    if schoice == '1':
        print('Searching with Unique ID')
    elif schoice == '2':
        print('Searching with Person Name')
    else: print('\n\nWrong Command !! Kindly Follow the Instructions...')

def cmd1():
    print('\n\nFollow the procedure to create New ID-Card...')
    print('\nImportant Note')
    print('\n1. All Fields are Mandatory')
    print('2. Avoid any kind of Spelling Mistakes\n')

def main_choice():
    print('\n\n>>> To Create New ID-Card, press "1"')
    print('>>> To View Saved ID-Cards, press "2"')
    choice = str(input('\n--> Please Input: '))

    if choice == '1':
        cmd1()
        new_card()
    elif choice == '2':
        print('\nShowing Saved ID-Cards...')
        saved_cards()
    else:
        print('\nWrong Command !! Kindly Follow the Instructions...')

main_choice()

while True:
    print('\n\n>>> To Run the program again, press "R"\n>>> To Close the program, press "ENTER"')
    endchoice = input('\nPlease Input: ')
    if endchoice.lower() == 'r':
        main_choice()
    else:
        print('\nThanks for using ID-Card Generator')
        break