import re
def validate_all(name,phone_no,email):
    def validate_name(name):
        if name == "":
            print("Username field should be filled.")
        if len(name) > 15:
            print("Username field should contain max. 15 characters")
        if str(name).isalpha() == False:
            print("Username should contain only alphabets")
        else:
            print("Username is validated")
    validate_name(name)
    def validate_phone(phone_no):
        pattern = r'^[7-9]\d{9}$'
        mob = re.search(pattern, phone_no)
        if mob:
            print("Phone number is validated")
        else:
            print("Please enter a valid phone nuber")
    validate_phone(phone_no)
    def validate_email(email):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        e = re.search(pattern,email)
        if e:
            print("Email id is validated")
        else:
            print("Please enter a valid email id")
    validate_email(email)
print("First entry: ")
validate_all("Sarvesh","8308790289","Email@xyz.com")
print("Second entry: ")
validate_all("Sarvesh123","308790289","Emailxyz.com")