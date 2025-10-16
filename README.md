# PythonFinance
## Contact
Author: Jason Jiang

Email: zhichengjiang2023@outlook.com

Readme Last Modified: 2025-10-16

## Disclaimer and Warnings

The project aims to investigate security data from quantitative perspectives. 

### Any file in this repository is solely for the purpose of study and does not constitute any financial advice. 

### Any file in this repository is solely for the purpose of study and does not constitute any financial advice. 

### Any file in this repository is solely for the purpose of study and does not constitute any financial advice. 

Please be reminded that any investment comes at a risk. Please be responsible and rational if you are currently investing in the market. Should you find any bugs/encounter any questions, please email the author. Thank you very much for reading. Have fun!

## Written at the Beginning
The instruction is written with the assumption that whoever is reading this might not have a coding foundation. Those interested but without a programming background deserve the same rights to access the fun of quantitative finance, whether visually or mathematically. I have tried my best to write the instructions and comments with the mindset as if I am presenting this to my grandma. If you have any suggestions on clarification, please let me know and it would be highly appreciated!

## Instructions

### I. Get your Tushare token
Here we use API from Tushare for Hong Kong and Mainland China exchanges. A token is needed to run the code. You may register [here](https://tushare.pro/register?reg=717744). 

### II. Get your stock data: Go to Get Data.py
1. Prepare the stock code. You may find this information on Sina Finance, Yahoo Finance, etc. Each stock code contains two parts: stock number and exchange acronym. For instance, the stock code for "Shanghai Pudong Development Bank Co Ltd" is "600000.SH" where 600000 is the number representing the company and .SH means Shanghai Stock Exchange.

2. Go to Copy paste your token, and replace 'your token' in ts.set_token('your token').

### If you are a Python pro already, you may ignore anything below

3. Modify save_dir = 'C:\\\\ABC\\\\DEF' + '\\\\' + stock + '.csv'

  * Select a folder you would like to store your stock data. The folder location can be found by right-clicking the folder icon, under "Properties." Copy and paste it to replace the 'C:\\\\ABC\\\\DEF' part with your folder directory. If your folder directory comes with only one slash '\\' and it did not work, try replacing all the '\\' with '\\\\.'

5. Update the following (read comments):

  * stock_code; stock_X; asset_class; start_date; end_date

### III. After Getting the Data

1. Open other .py files. Remember to replace the dataframe reading directory with the one you used for saving the data. If you can locate your .csv (might show up with Excel icon) file in your folder, you may find its directory following the same procedure as I-3.

2. Read the comments and replace anything that you would like to change.
