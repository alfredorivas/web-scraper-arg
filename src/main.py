import logging
import yaml
from objects.site import NewSite


logging.getLogger().setLevel(logging.DEBUG)


def main():
    with open('./profiles/general.yaml') as f:
        url_data = yaml.safe_load(f)
    names = ['argenprop', 'meli', 'zonaprop']
    for name in names:
        logging.info(' :::::::::::::::::::::::::')
        logging.info(' :: Processing ' + name)
        url_data_tmp = url_data['url-data-' + name]
        url = url_data_tmp['base'] + url_data_tmp['type'] + url_data_tmp['ops'] + url_data_tmp['size'] + url_data_tmp['pri-loc'] + url_data_tmp['sec-loc'] + url_data_tmp['price-range'] + url_data_tmp['end']
        logging.info('  :: URL: ' + url)
        site = NewSite(name, url)
        site.output()


if __name__ == "__main__":
    main()
