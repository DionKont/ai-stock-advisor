import sys

import requests
import pandas as pd
from dateutil.parser import parse
import pytz


class AlphaVantageAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query?"

    def get_data(self, function, symbol, interval=None, outputsize='full', ticker=None):
        if function == 'OVERVIEW':
            url = f"{self.base_url}function={function}&symbol={symbol}&apikey={self.api_key}"
        elif function == 'TIME_SERIES_INTRADAY':
            url = f"{self.base_url}function={function}&interval={interval}&symbol={symbol}&apikey={self.api_key}" \
                  f"&outputsize={outputsize}"
        elif function == 'NEWS_SENTIMENT':
            url = f"{self.base_url}function={function}&ticker={symbol}&apikey={self.api_key}"
        else:
            print(f'Invalid function: {function}')
            sys.exit(1)
        response = requests.get(url)
        print(f'The URL for the request is: {url}')
        if response.status_code == 200:
            print(f'All good with the Request response: {response.text}')
            return response.json()
        else:
            print(f'Something went wrong with the Request response: {response.status_code}')
            return 0

    def get_stock_data_with_time_series_intraday(self, stock_name, interval, outputsize='full'):
        data = self.get_data(function='TIME_SERIES_INTRADAY', symbol=stock_name, interval=f'{interval}min',
                             outputsize=outputsize)
        stock_data = []
        time_series = data.get(f'Time Series ({interval}min)', {})
        old_tz = pytz.timezone('US/Eastern')
        new_tz = pytz.timezone('Europe/London')
        for timestamp, values in time_series.items():
            timestamp_uk = old_tz.localize(parse(timestamp)).astimezone(new_tz)
            stock_data.append({
                'timestamp': timestamp_uk,
                'open': values.get('1. open'),
                'high': values.get('2. high'),
                'low': values.get('3. low'),
                'close': values.get('4. close'),
                'volume': values.get('5. volume')
            })
        df = pd.DataFrame(stock_data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hour'] = df['timestamp'].dt.hour
        df['minute'] = df['timestamp'].dt.minute
        df['day_of_week'] = df['timestamp'].dt.dayofweek
        df['month'] = df['timestamp'].dt.month
        df = df.drop('timestamp', axis=1)
        return df, stock_data
