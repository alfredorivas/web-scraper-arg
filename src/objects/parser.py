import logging


logging.getLogger().setLevel(logging.DEBUG)


class NewParser(object):
    def __init__(self, name, profile, register):
        self.name = name
        self.profile = profile
        self.register = register

    def parse(self):
        tmp_lst_parsed_reg = []
        try:
            # :: currency
            currency = self.register.find(self.profile['currency-data']['type'], {self.profile['currency-data']['class']: self.profile['currency-data']['value']})
            if currency:
                tmp_x = currency.text.strip()
                if self.name in ['zonaprop']:
                    tmp_x = tmp_x.split(' ')
                    tmp_x = tmp_x[0]
                tmp_lst_parsed_reg.append(tmp_x)
            else:
                tmp_lst_parsed_reg.append('')
            # :: price
            price = self.register.find(self.profile['price-data']['type'], {self.profile['price-data']['class']: self.profile['price-data']['value']})
            if price:
                tmp_x = price.text.strip()
                if self.name in ['argenprop', 'zonaprop']:
                    tmp_x = tmp_x.split(' ')
                    tmp_x = tmp_x[1].replace('.', '')
                if self.name == 'meli':
                    tmp_x = tmp_x.replace('.', '')
                tmp_lst_parsed_reg.append(tmp_x)
            else:
                tmp_lst_parsed_reg.append(0)
            # :: address
            address = self.register.find(self.profile['address-data']['type'], {self.profile['address-data']['class']: self.profile['address-data']['value']})
            if address:
                tmp_x = address.text.strip()
                if self.name == 'meli':
                    tmp_x = tmp_x.split(', ')[0]
                tmp_lst_parsed_reg.append(tmp_x)
            else:
                tmp_lst_parsed_reg.append('')
            # :: location
            location = self.register.find(self.profile['location-data']['type'], {self.profile['location-data']['class']: self.profile['location-data']['value']})
            if location:
                tmp_x = location.text.strip()
                if self.name == 'meli':
                    tmp_x = tmp_x.split(', ')
                    tmp_x = tmp_x[1] + ', ' + tmp_x[2]
                tmp_lst_parsed_reg.append(tmp_x)
            else:
                tmp_lst_parsed_reg.append('')
            # :: title
            title = self.register.find(self.profile['title-data']['type'], {self.profile['title-data']['class']: self.profile['title-data']['value']})
            if title:
                tmp_lst_parsed_reg.append(title.text.strip())
            else:
                tmp_lst_parsed_reg.append('')
            # :: web
            web = self.register.find(self.profile['web-data']['type'], {self.profile['web-data']['class']: self.profile['web-data']['value']})
            if web:
                tmp_lst_parsed_reg.append(self.profile['web-data']['base-url'] + web.get('href'))
            else:
                tmp_lst_parsed_reg.append('')
            # :: atts -> area + ambs
            atts = self.register.find(self.profile['atts-data']['type'], {self.profile['atts-data']['class']: self.profile['atts-data']['value']})
            if atts:
                flg_area = False
                flg_amb = False
                for att in atts:
                    tmp_val = att.text.strip()
                    if self.profile['atts-data']['string-area'] in tmp_val and not flg_area: # ademas de tomar los campos que tienen el valor especifico de area, me aseguro de tomar el area general (la primera)
                        tmp_lst_parsed_reg.append(tmp_val.replace(self.profile['atts-data']['string-area'], ''))
                        flg_area = True
                    if self.profile['atts-data']['string-ambs'] in tmp_val:
                        tmp_lst_parsed_reg.append(tmp_val.replace(self.profile['atts-data']['string-ambs'], ''))
                        flg_amb = True
                if not flg_area:
                    tmp_lst_parsed_reg.append(0)
                if not flg_amb:
                    tmp_lst_parsed_reg.append(0)
            else:
                tmp_lst_parsed_reg.append(0)
                tmp_lst_parsed_reg.append(0)
            # :: price_area_ratio
            try:
                tmp_lst_parsed_reg.append(int(float(tmp_lst_parsed_reg[1]) / float(tmp_lst_parsed_reg[6])))
            except BaseException as e:
                tmp_lst_parsed_reg.append(0)
        except BaseException as e:
            logging.error(' Error while parsing, returning basic empty list')
            tmp_lst_parsed_reg = ['', 0, '', '', '', '', 0, 0, 0]
        return tmp_lst_parsed_reg
