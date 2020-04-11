from __future__ import absolute_import, print_function, unicode_literals

import json
import sys
import time
from datetime import datetime, timedelta
import pandas as pd
import requests

from pandas.io.json._normalize import nested_to_record
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from pytrends.request import TrendReq

if sys.version_info[0] == 2:  # Python 2
    from urllib import quote
else:  # Python 3
    from urllib.parse import quote
google_username = ""  #Insert gmail email
google_password = ""  #Insert gmail password

# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq(google_username, google_password, custom_useragent='My Pytrends Script')

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['coronavirus', 'unemployment'])

# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()

# Interest by Region
interest_by_region_df = pytrend.interest_by_region()
