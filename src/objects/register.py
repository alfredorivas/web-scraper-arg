class NewRegister(object):
    def __init__(self):
        self.currency = ''
        self.price = int(0)
        self.address = ''
        self.location = ''
        self.title = ''
        self.web = ''
        self.area = int(0)
        self.ambs = int(0)
        self.price_area_ratio = int(0)

    def empty_obj(self):
        self.currency = ''
        self.price = int(0)
        self.address = ''
        self.location = ''
        self.title = ''
        self.web = ''
        self.area = int(0)
        self.ambs = int(0)
        self.price_area_ratio = int(0)

    def fill_obj(self, lst_vals):
        self.currency = str(lst_vals[0])
        try:
            self.price = int(lst_vals[1])
        except:
            self.price = int(0)
        self.address = str(lst_vals[2])
        self.location = str(lst_vals[3])
        self.title = str(lst_vals[4])
        self.web = str(lst_vals[5])
        try:
            self.area = int(lst_vals[6])
        except:
            self.area = int(0)
        try:
            self.ambs = int(lst_vals[7])
        except:
            self.ambs = int(0)
        self.price_area_ratio = int(lst_vals[8])

    def to_dict(self):
        return {
            'currency': self.currency,
            'price': self.price,
            'address': self.address,
            'location': self.location,
            'title': self.title,
            'web': self.web,
            'area': self.area,
            'ambs': self.ambs,
            'price_area_ratio': self.price_area_ratio
        }
