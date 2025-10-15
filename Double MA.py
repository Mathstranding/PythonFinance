import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ffn

# Variable setups
hold = False #holding status (Bool)
pos = 0 #position, number of shares on hold
cash = 100000 # starting cash
port = cash + pos
fee = 0.0005 # transaction fee rate at 5/10,000
port_log = [] # daily portfolio change
num_MA_I = 5 # Shortest term MA number of days
num_MA_II = 10 # Longest term MA number of days
MA5_array = np.zeros(num_MA_I) # 5-day MA array
MA10_array = np.zeros(num_MA_II) # 10-day MA array
df = pd.read_csv('input data directory')

# Body
for i in range(len(df)):
    price = df.loc[i, 'close']
    date = df.loc[i, 'trade_date']
    # shift price series by 1 unit
    MA5_array[0:(num_MA_I-1)] = MA5_array[1:num_MA_I]
    MA10_array[0:(num_MA_II-1)] = MA10_array[1:num_MA_II]
    # add new price to the end of array
    MA5_array[-1] = price
    MA10_array[-1] = price
    if i < num_MA_II:
        port_log.append(port)
        continue
         # pass if i is smaller than number of days for longest MA
    # Calculate mean for each of the array
    MA5 = MA5_array.mean()
    MA10 = MA10_array.mean()

    # Timing Strategy
    # Buy
    if MA5 >= MA10 and hold == False:
        pos = int(cash / price // 10) * 10 # number of buy -> current position
        cash -= pos * price * (1 + fee)
        hold = True # update holding status
        port = cash + pos * price
        #print('Buy on', date, 'Price', price, 'Portfolio Value', port)
    # Sell
    elif MA5 < MA10 and hold == True:
        cash += pos * price * (1 - fee) + cash
        pos = 0
        hold = False
        port = cash + pos * price
        #print('Sell on', date, 'Price', price, 'Portfolio Value', port)
    # Record new portfolio value
    if hold == True: # update portfolio value if having a position
        port = pos * price + cash
    port_log.append(port)



# Manipulate series. Assign portfolio value changes (port_log) to df,
#   and make "trade_date" into pandas datetime format
df = df.iloc[::-1] # reverse dataframe so that the order goes from old to new
df['trade_date']= pd.to_datetime(df['trade_date'], format='%Y%m%d') # convert trade_date info to panda datetime
df['portfolio_value'] = port_log # create a new time series, port value against trade_date
df.set_index('trade_date', inplace=True) # index date; inplace here replace the original data
port_series = df['portfolio_value'][num_MA_II:] # omit first a couple of days without valid info for MA
port_returns = ffn.to_returns(port_series) # port value change rates by each time unit


# Total Return
returns = ffn.calc_total_return(port_series)
max_drawdown = ffn.calc_max_drawdown(port_series)
sharpe = ffn.calc_sharpe(port_returns, rf = 0.02, nperiods = 1)
calmar = ffn.calc_calmar_ratio(port_series)

print('Return/收益率: ', returns * 10000//1/100, '%')
print('Max Drawdown/最大回撤: ', max_drawdown * 10000//1/100, '%')
print('Sharpe Ratio/夏普率: ', sharpe * 100//1/100)
print("Calmar Ratio/卡玛率: ", calmar * 100//1/100)

# Visualize
#plt.plot(range(len(port_log)), port_log)
plt.plot(port_series)
plt.xlabel('Time')
plt.ylabel('Portfolio Value')
plt.title('MA5~MA10 Backtest Result')
plt.show()

