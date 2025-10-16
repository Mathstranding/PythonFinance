import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

plt.rcParams['figure.dpi'] = 1000 # DPI setup

# Data processing
df = pd.read_csv('C:\\Stock Price Library\\603825.SH.csv',encoding='utf-8-sig',usecols=['close'])
df.replace(0,np.nan,inplace=True) # replace close with 0 value with the previous close
df.ffill(inplace=True)

# ARIMA Model
model = ARIMA(df.close, order=(2,1,2))
model_fit = model.fit()
# Model estimation of sample data
observe_model_values = model_fit.predict(start=1, end=len(df)-1)

# Model prediction of future data
model_forecast_values = model_fit.forecast(steps=10)

# Concatenation
model_values = pd.concat([observe_model_values,model_forecast_values], axis=0)

# Plot original curve and model generated curve
plt.plot(df['close'], label='Original Curve')
plt.plot(model_values, label='Model Estimation with Prediction')
plt.legend()
plt.show()

# Auto-select optimal ARIMA parameters
import pmdarima as pm
model = pm.auto_arima(df.values,
                      stationary=True,
                      test='kpss',
                      stepwise=False,
                      seasonal_test='cocssb',
                      with_intercept=True,
                      n_jobs=-1,
                      trend='ctt',
                     trace=True,)
# print(model.summary())

# Prediction with the selected parameters
n_periods = 7
fc, confint = model.predict(n_periods=n_periods, return_conf_int=True)
index_of_fc = np.arange(len(df.values), len(df.values)+n_periods)
# ARIMA prediction interval
fc_series = pd.Series(fc, index=index_of_fc)
lower_series = pd.Series(confint[:, 0], index=index_of_fc) # lower bound
upper_series = pd.Series(confint[:, 1], index=index_of_fc) # upper bound
# output graph
plt.plot(df.values)
plt.plot(fc_series, color='darkgreen')
plt.fill_between(lower_series.index,
                 lower_series,
                 upper_series,
                 color='k', alpha=.15)
plt.show()
