import requests
import pprint
from bs4 import BeautifulSoup

class espn_request:

    base_id = 39346
    root_page = 'http://www.espn.com/mens-college-basketball/player/_/id/'
    remainder = '/justin-jenifer?src=mobile'