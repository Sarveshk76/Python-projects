import re

def personalDetails(name, dob, mobNo, emailId):
    print('Personal Details'.center(30, '-'))
    print('Name: ', name)
    if valid_date(dob):
        print('Person DOB: Invalid DOB')
    else:
        print('Person DOB: ', dob)
    print('Mob No.: ',mobNo)
    print('Email ID: ', emailId)

def valid_date(birthDate):
    try:
        mat = re.match('^(\d{2})[/.-](\d{2})[/.-](\d{4})$', birthDate)
        if bool(mat) is False:
            raise ValueError
    except ValueError:
        return 'Invalid DOB'

personalDetails("Sarvesh", "19-05-1998", "8308790289", "kulkarnisarvesh1@gmail.com")
personalDetails("Sarvesh", "19-051998", "8308790289", "kulkarnisarvesh1@gmail.com")