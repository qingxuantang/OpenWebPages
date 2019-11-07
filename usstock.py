'''US STOCKS'''

import webbrowser

def open_us_stock_charts():
    us_url =[
        'https://www.tradingview.com/chart/dEaD5qXm/',
        'https://www.tradingview.com/chart/IYbVpsS9/',
        'https://www.tradingview.com/chart/RBVJp2WS/',
        'https://www.tradingview.com/chart/oNPA20MP/',
        'https://www.tradingview.com/chart/j8Iu5MEr/',
        'https://www.tradingview.com/chart/k1LCnnM9/',
        'https://www.tradingview.com/chart/mK1GyiKc/',
        'https://www.tradingview.com/chart/Mr0LbiKB/',
    ] 
    for us in us_url:
        webbrowser.get('chrome').open_new(us)

us_con = input("Are you sure about openning all the US STOCK charts? (y/n)")
if us_con == 'y':
    open_us_stock_charts()
else:
    print('Action aborted.')
