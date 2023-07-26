
import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go




class ProphetNN:
    def __init__(self, stock_data, n_predictions, interval):
        self.stock_data = stock_data
        self.n_predictions = n_predictions
        self.interval = interval

    def predict(self):
        n_predictions = int(self.n_predictions)
        interval = int(self.interval)

        stock_data = pd.DataFrame(self.stock_data)
        df_sorted = stock_data.sort_values('timestamp')
        stock_data = df_sorted
        print(f'stock_data: {stock_data}')
        stock_data['timestamp'] = pd.to_datetime(stock_data['timestamp']).dt.tz_localize(None)
        stock_data = stock_data.rename(columns={'timestamp': 'ds', 'close': 'y'})
        stock_data['y'] = pd.to_numeric(stock_data['y'])

        model = Prophet()

        model.fit(stock_data)

        start = stock_data['ds'].iloc[-1]

        future = pd.DataFrame({'ds': pd.date_range(start=start, periods=n_predictions, freq=f'{interval}min')})

        forecast = model.predict(future)

        self.plot_and_save(model, forecast, stock_data)

    def plot_and_save(self, model, forecast, stock_data):
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=stock_data['ds'], y=stock_data['y'], mode='lines', name='Actual'))
        fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Prediction'))
        fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], mode='lines', name='Lower Bound'))
        fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], mode='lines', name='Upper Bound'))

        fig.update_layout(
            title='Prophet Neural Network Trend Predictions',
            xaxis_title='Time',
            yaxis_title='Close Value (USD)',
            autosize=False,
            width=500,
            height=500,
        )

        fig.write_html("AIStockAdvisor//templates//graphs//prophet.html")







