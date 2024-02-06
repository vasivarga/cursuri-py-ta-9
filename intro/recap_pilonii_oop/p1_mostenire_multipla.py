import time


class Device:
    is_electric = True

class Ceas:
    is_digital = True

    def arata_ceasul(self):
        print(time.time())

class CeasDigital(Device, Ceas):
    pass

ceas_digital = CeasDigital()
ceas_digital.arata_ceasul()