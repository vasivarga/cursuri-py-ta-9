class Phone:
    name = None
    year = None
    turned_on = False

    def __init__(self, name, year, turned_on):
        self.name = name
        self.year = year
        self.turned_on = turned_on

    def turn_on(self):
        if self.turned_on:
            print("Telefonul este deja pornit")
        else:
            print("Telefonul a fost pornit")
            self.turned_on = True

    def ring(self):
        print("Ring ring")

    def print_phone_properties(self):
        print(f"Name = {self.name}")
        print(f"Year = {self.year}")
        print(f"Turned on? = {self.turned_on}")


# telefon = Phone("Samsung", 2023, False)
# telefon.turn_on()
# telefon.turn_on()

class AndroidPhone(Phone):
    android_version = None

    def set_android_version(self, version):
        self.android_version = version

    def print_android_version(self):
        if self.android_version:
            print(f"Android_version: {self.android_version}")
        else:
            print("Version is not set yet!")

    def print_phone_properties(self):
        super().print_phone_properties()
        print(f"Android version: {self.android_version}")


oneplus = AndroidPhone("Oneplus 8 pro", 2020, False)
oneplus.turn_on()
oneplus.print_android_version()
oneplus.set_android_version("14.1")
oneplus.print_android_version()


class Iphone(Phone):
    ios_version = None

    def set_ios_version(self, version):
        self.ios_version = version

    def print_ios_version(self):
        if self.ios_version:
            print(f"Ios_version: {self.ios_version}")
        else:
            print("Version is not set yet!")


iphone_14 = Iphone("Iphone 14 pro", 2023, False)
iphone_14.turn_on()



