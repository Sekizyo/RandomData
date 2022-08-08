class ContainerGenerator():

    def getContainer(self):
        container = {
            "char_pk": self.charPk(),
            "serial_number": self.serialNr(),
            "check_digit": self.checkDigit(),
            "bic": self.bic(),
            "iso_code": self.isoCode(),
            "max_gross_weight_kgs": self.mGwK(),
            "max_gross_weight_lbs": self.mGwl(),
            "tare_weight_kgs": self.mGwl(),
            "tare_weight_lbs": self.mGwl(),
            "net_weight_kgs": self.mGwl(),
            "net_weight_lbs": self.mGwl(),
        }

    def charPk(self):
        return 