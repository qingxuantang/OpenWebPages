'''CRYPTOCURRENCY'''

import webbrowser

def open_cc_stock_charts():
    cc_url =[
        'https://www.tradingview.com/chart/1qYvHMZe/',
        'https://www.tradingview.com/chart/rcf2kDWN/',
        'https://www.tradingview.com/chart/E65JE3rd/',
        'https://www.tradingview.com/chart/wAYfQDbj/',
        'https://www.tradingview.com/chart/gt9JkAPV/',
        'https://www.tradingview.com/chart/QjBsfVxM/',
        'https://www.tradingview.com/chart/XU4AWmqn/',
        'https://www.tradingview.com/chart/sEEYf86p/',
        'https://www.tradingview.com/chart/nKGXQSFu/',
        'https://www.tradingview.com/chart/EmlxTwBc/',
    ] 
    for cc in cc_url:
        webbrowser.get('chrome').open_new(cc)

cc_con = input("Are you sure about openning all the CRYPTO charts? (y/n)")
if cc_con == 'y':
    open_cc_stock_charts()
else:
    print('Action aborted.')