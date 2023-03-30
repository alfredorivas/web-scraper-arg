import logging
import cloudscraper
from bs4 import BeautifulSoup


logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger('urllib3').setLevel(logging.WARNING)


class ExcSource(Exception):
    pass


class NewBrowser(object):
    def __init__(self, url):
        if not url:
            logging.error(' Object could not be created because there is no URL for this site')
            exit()
        else:
            self.url = url

    def initialize(self, name):
        retries_cnt = 20 # number of trials (zonaprop uses Cloudfare which is .... not nice)
        while retries_cnt > 0:
            try:
                scraper = cloudscraper.create_scraper()
                if name == 'zonaprop':
                    scraper.delay = 10 # this reduces the chances of captcha 2 of preventing access
                source = BeautifulSoup(scraper.get(self.url).content.decode('utf-8', 'ignore'), 'html.parser') # without decode, meli raises debug error
                logging.info('  :: Connected to ' + name)
                if not source:
                    raise ExcSource()
                else:
                    return source
            except ExcSource as e:
                logging.error(' Object could not be created because there is no source code for this site')
                exit()
            except BaseException as e:
                logging.error(' Connection did not succeed due to: "' + str(e) + '"')
                source = ''
                retries_cnt = retries_cnt - 1
        return source
