import logging
import yaml
from objects.site import NewSite


logging.getLogger().setLevel(logging.DEBUG)


def main():
    names = ['argenprop', 'meli', 'zonaprop']
    for name in names:
        logging.info(' :::::::::::::::::::::::::')
        logging.info(' :: Processing ' + name)
        with open('./profiles/' + name + '.yaml') as f:
            url_data = yaml.safe_load(f)
            url_data = url_data['url-data']
        url = url_data['base'] + url_data['type'] + url_data['ops'] + url_data['size'] + url_data['pri-loc'] + url_data['sec-loc'] + url_data['price-range'] + url_data['end']
        logging.info('  :: URL: ' + url)
        site = NewSite(name, url)
        site.output()


if __name__ == "__main__":
    main()
