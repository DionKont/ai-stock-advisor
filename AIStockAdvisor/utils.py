from .alphavantage.api import AlphaVantageAPI

from AIStockAdvisor.machinelearning.prophetnn import ProphetNN


class Utils:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query?function="
        self.api = AlphaVantageAPI(self.api_key)

    def get_stock_data(self, stock_name, interval=5):
        df, stock_data = self.api.get_stock_data_with_time_series_intraday(stock_name=stock_name, interval=interval)
        return df, stock_data

    def get_company_data(self, stock_name):
        data = self.api.get_data(function='OVERVIEW', symbol=stock_name)

        company_data = {
            'name': data.get('Name'),
            'industry': data.get('Industry'),
            'sector': data.get('Sector'),
            'country': data.get('Country'),
            'description': data.get('Description'),
            'exchange': data.get('Exchange'),
            'market_cap': data.get('MarketCapitalization'),
            'pe_ratio': data.get('PERatio'),
            'profit_margin': data.get('ProfitMargin'),
            'ebitda': data.get('EBITDA'),
            'price_to_book_ratio': data.get('PriceToBookRatio'),

        }
        return company_data

    # TODO: To fix this
    def get_news_data(self, stock_name):
        # api = AlphaVantageAPI(api_key=self.api_key)
        #
        # data = api.get_data(function='NEWS_SENTIMENT', symbol=stock_name)
        # data = response.json()
        #
        # news_data = []
        pass

    def predict(self, stock_data, df, n_predictions, interval):
        prophet = ProphetNN(stock_data, n_predictions, interval)
        prophet.predict()

        return 1
