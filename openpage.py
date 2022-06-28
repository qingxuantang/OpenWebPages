
def openWebPage():
    import os
    url =[
       'https://www.tradingview.com/chart/caDek3Z6/',
       'https://www.tradingview.com/chart/O5w6cxmD/',
       'https://www.tradingview.com/chart/VpgCvDG8/',
       #'https://www.tradingview.com/chart/RBVJp2WS/', 铭普光磁
       'https://www.tradingview.com/chart/g5CelBO9/',
       'https://www.tradingview.com/chart/fBmBFdIX/',
       'https://www.tradingview.com/chart/1qYvHMZe/',]
    for i in url:
        os.system("python -m webbrowser " + i)

input_msg = input("Are you sure about openning all the pages? (y/n)")
if input_msg == 'y':
    openWebPage()
else:
    print('Action aborted.')


