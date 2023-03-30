import logging
import os
from datetime import datetime
import pandas as pd
import yaml
from objects.browser import NewBrowser
from objects.parser import NewParser
from objects.register import NewRegister


logging.getLogger().setLevel(logging.DEBUG)


class ExcSource(Exception):
    pass


class NewSite(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.registers = []
        self.profile = ''

    def _get_profile(self):
        try:
            profile = './profiles/' + self.name + '.yaml'
            with open(profile) as f:
                self.profile = yaml.safe_load(f)
        except FileNotFoundError:
            logging.error(' Object could not be created because there is no profile for this site')
            exit()


    def _get_registers(self):
        self._get_profile()
        retries_cnt = 10  # number of trials in case of response errors
        while retries_cnt > 0:
            try:
                browser = NewBrowser(self.url).initialize(self.name)
                self.registers = browser.find_all(self.profile['parent-data']['type'], {self.profile['parent-data']['class']: self.profile['parent-data']['value']})
                if self.registers:
                    retries_cnt = 0
                else:
                    retries_cnt = retries_cnt - 1
                    logging.info('  :: Info could not be retrieved')
            except BaseException as e:
                logging.error(' Object could not be created because there is no source code for this site or exceeded connection attempts')
                exit()

    def _parse_registers(self):
        self._get_registers()
        lst_reg_objs = []
        for iteration, reg in enumerate(self.registers):
            tmp_reg = NewRegister()
            tmp_reg.empty_obj()
            tmp_lst_parsed_reg = NewParser(self.name, self.profile, reg).parse()
            tmp_reg.fill_obj(tmp_lst_parsed_reg)
            lst_reg_objs.append(tmp_reg.to_dict())
            logging.info('  :: Iteration #{} completed'.format(iteration + 1))
        return lst_reg_objs

    def output(self):
        now = str(datetime.now().strftime("%Y%m%d_%H%M%S"))
        reg_dic = self._parse_registers()
        ds_out = pd.DataFrame(reg_dic)
        # logging.info(ds_out.head())
        ds_out = ds_out.drop_duplicates(keep='first')
        ds_out = ds_out.drop_duplicates(subset=['price', 'address'], keep='first')
        ds_out = ds_out.sort_values(by=['price'], ascending=False)
        logging.info('  :: Sorting and duplicates removal completed')
        file_name = now + '_' + self.name + '_webscrap.csv'
        relative_data_path = './data/'
        try:
            if not os.path.exists(relative_data_path):
                os.mkdir(relative_data_path)
            ds_out.to_csv(relative_data_path + file_name, sep='\t', index=False)
            logging.info('  :: File saved')
        except BaseException as e:
            logging.error(' CSV could not be saved due to an unexpected error')
        finally:
            logging.info(' :: Process finished')
            logging.info(' :::::::::::::::::::::::::\n')
