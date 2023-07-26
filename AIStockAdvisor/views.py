from django.shortcuts import render
from .utils import Utils
import sys
import os
from AIStockAdvisor.validation.stockdataform import StockForm

API_KEY = os.environ.get('API_KEY')
if not API_KEY:
    print('You need to set up an environment variable for your AlphaVantage API_KEY.')
    sys.exit()


def stock_view(request):
    utils = Utils(api_key='API_KEY')
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock_name = request.POST.get('stock_name')
            time_interval = request.POST.get('time_interval')
            n_predictions = request.POST.get('n_predictions')
            df, stock_data = utils.get_stock_data(stock_name, interval=time_interval)
            company_data = utils.get_company_data(stock_name)
            n_predictions = int(n_predictions)
            print(f' Stock Name: {stock_name} Number of predictions: {n_predictions} Type: {type(n_predictions)}')
            utils.predict(stock_data=stock_data, n_predictions=n_predictions, interval=time_interval)
            return render(request,
                          'stock.html',
                          {'stock_data': stock_data, 'stock_name': stock_name,
                           'company_data': company_data})
    return render(request, 'stock.html')
