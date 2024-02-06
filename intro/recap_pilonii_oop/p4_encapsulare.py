class User:
    __email = None
    __password = None
    __role = "Admin"

    def set_email(self, email_address):
        if "@" in email_address and ".com" in email_address:
            self.__email = email_address
            print(f"Emailul {email_address} a fost setat cu succes!")
        else:
            print("Emailul este invalid.")

    def get_email(self):
        return self.__email

    def delete_email(self):
        self.__email = None

    def set_password(self, password):
        if len(password) > 7 and self.__contains_uppercase(password):
            self.__password = password
            print("Parola a fost setata cu succes")
        else:
            print("Parola invalida! Trebuie sa contina min. 8 caractere si o litera mare")

    def __contains_uppercase(self, password):
        avem_uppercase = False
        for letter in password:
            if str(letter).isupper():
                avem_uppercase = True
                break
        return avem_uppercase


#
# user_1 = User()
# user_1.set_email("pyta9@itfactory")
# user_1.set_email("pyta9@itfactory.com")
#
# print(user_1.get_email())
#
# user_1.set_password("1234567d")
# user_1.set_password("1234567D")

# print(user_1._role)

