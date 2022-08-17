
def openWebPage():
    import os
    url =[
        'https://www.tradingview.com/chart/1qYvHMZe/', #BTCUSD
        'https://www.tradingview.com/chart/caDek3Z6/', #鼎盛新材
        'https://www.tradingview.com/chart/O5w6cxmD/', #福莱特
        'https://www.tradingview.com/chart/g5CelBO9/', #明德生物
        'https://www.tradingview.com/chart/VpgCvDG8/', #海源复材
        #'https://www.tradingview.com/chart/RBVJp2WS/', #铭普光磁
        #'https://www.tradingview.com/chart/fBmBFdIX/', #中航光电
        #'https://www.tradingview.com/chart/Mr0LbiKB/', #金智科技
       ]
    for i in url:
        os.system("python3 -m webbrowser " + i) #220805update

input_msg = input("Are you sure about openning all the pages? (y/n)")
if input_msg == 'y':
    openWebPage()
else:
    print('Action aborted.')


