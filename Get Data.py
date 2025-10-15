#Get Data
import tushare as ts

# Tushare Token
ts.set_token('')
#pro = ts.pro_api()
# Get historical stock data
# Stock name setup
# stock name consists of its code (number) and its stock exchange (dot letters)
stock_code = '600000'  # 6xxxxx or 0xxx for ShanghaiX, 0xxxxx or 3xxx for ShenzhenX, etc.
stock_X = '.SH'  #'.SH' for Shanghai X, '.SZ' for Shenzhen X, '.BJ', '.HK'
asset_class = 'E'  # Asset: E=equity I=index C=crypto FT=future FD=fund O=option CB=convertible debt
stock = stock_code + stock_X
save_dir = 'C:\\Stock Price Library' + '\\' + stock + '.csv'
df = ts.pro_bar(ts_code=stock, start_date='20180101', end_date='20251014', asset = asset_class)
df.to_csv(save_dir)
# print(df)