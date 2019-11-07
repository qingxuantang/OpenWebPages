'''HKEX STOCKS'''

import webbrowser

def open_hk_stock_charts():
    hk_url =[
        'https://www.tradingview.com/chart/JFOjCX22/',
        'https://www.tradingview.com/chart/D7npspCZ/',
        'https://www.tradingview.com/chart/bROtEnmB/',
        'https://www.tradingview.com/chart/lhY2xdab/',
        'https://www.tradingview.com/chart/bf5YdIwW/',
        'https://www.tradingview.com/chart/Zdseb3pw/',
        'https://www.tradingview.com/chart/WFQjAmDL/',
        'https://www.tradingview.com/chart/2GxFomf3/',
    ] 
    for hk in hk_url:
        webbrowser.get('chrome').open_new(hk)

hk_con = input("Are you sure about openning all the HKEX STOCK charts? (y/n)")
if hk_con == 'y':
    open_hk_stock_charts()
else:
    print('Action aborted.')