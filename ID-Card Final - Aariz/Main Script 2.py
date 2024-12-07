from PIL import Image, ImageDraw, ImageFont

template = Image.open('Template3.png')
draw = ImageDraw.Draw(template)

import random
import datetime
import qrcode


def new_card():
    # Org Name
    font = ImageFont.truetype('Garamond.ttf', size=90)     # font size for Org and ID

    org = input('Enter Your Organisation Name: ')
    W = 1000
    draw = ImageDraw.Draw(template)
    w,h = draw.textsize(org)
    draw.text(((W-w)/2,5), str(org), font=font, fill='white')

    # Unique ID
    font = ImageFont.truetype('Garamond.ttf', size=60)

    id = random.randint(1000000, 9000000)
    draw.text((860, 480), '#'+str(id), font=font, fill='chocolate')

    # Other Details
    font = ImageFont.truetype('Garamond.ttf', size=45)       # font size for rest inputs

    name = input('Enter Your Full Name: ')
    draw.text((70, 200), 'Name:   '+str(name), font=font, fill='black')

    gender = input('Enter Your Gender: ')
    draw.text((70, 280), 'Gender:   '+str(gender), font=font, fill='black')

    age = input('Enter Your Age: ')
    draw.text((520, 280), 'Age:   '+str(age), font=font, fill='black')

    dob = input('Enter Your Date of Birth: ')
    draw.text((70, 360), 'DoB:   '+str(dob), font=font, fill='black')

    bg = input('Enter Your Blood Group: ')
    draw.text((70, 440), 'Blood Group:   '+str(bg), font=font, fill='crimson')

    mob = input('Enter Your Mobile Number: ')
    draw.text((70, 520), 'Phone No. :   '+str(mob), font=font, fill='black')

    address = input('Enter Your Address: ')
    draw.text((70, 600), 'Address:   '+str(address), font=font, fill='navy')

    template.save('temp/' + str(name) + '.png')
    img = qrcode.make(str(org) + '#' + str(id) + '\n' + str(name))
    img.save('temp/' + str(id) + '.svg')

    qr = Image.open('temp/' + str(id) + '.svg').resize((236, 236))

    card = Image.open('temp/' + name + '.png')
    card.paste(qr, (856, 243, 1092, 479))
    card.save('Final Cards/' + name + '.png')

    print('\n\nYour ID-Card is Successfully created in a PNG File  "'+ name +'.png"')

    return template

d_date = datetime.datetime.now()
print()
reg_format_date = d_date.strftime('  %d-%m-%Y\t\t\t\t ID CARD Generator/Viewer\t\t\t\t  %I:%M:%S %p\n\t\t\t\t\t\t\t\t By Mohammed Aariz \t\t\t\t')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(reg_format_date)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

print('\n\n\nTo Create New ID-Card, press "1"')
print('To View Old ID-Card, press "2"')
cmd = str(input('\n\nPlease Input: '))

if cmd == '1':
    print('\nImportant Note')
    print('\n1. All Fields are Mandatory')
    print('2. Avoid any kind of Spelling Mistakes')
    print('3. Write Everything in UPPERCASE letters\n\n')

    new_card()
elif cmd == '2':
    print('\nShowing Saved ID-Cards...')
    print("\nOops... The Program doesn't know MySQL yet")
    print('SORRY :)')


print('\n\nTo Run the program again, press "R"\nTo Close the program, press "C"')

cmd2 = input('\nPlease Input: ')

