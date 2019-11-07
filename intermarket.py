'''INTER MARKET CHARTS'''

import webbrowser

def open_im_stock_charts():
    im_url =[
       'https://www.tradingview.com/chart/OpAP6D80/',
        'https://www.tradingview.com/chart/5WtdWwAj/',
        'https://www.tradingview.com/chart/XHrMFFAi/',
        'https://www.tradingview.com/chart/6etjc7dC/', 
    ] 
    for im in im_url:
        webbrowser.get('chrome').open_new(im)

im_con = input("Are you sure about openning all the CRYPTO charts? (y/n)")
if im_con == 'y':
    open_im_stock_charts()
else:
    print('Action aborted.')