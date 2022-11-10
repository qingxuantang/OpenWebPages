
import os
url =[
    'https://www.tradingview.com/chart/1qYvHMZe/', #BTCUSD
    'https://www.tradingview.com/chart/caDek3Z6/', #鼎盛新材
    'https://www.tradingview.com/chart/O5w6cxmD/', #福莱特
    'https://www.tradingview.com/chart/g5CelBO9/', #明德生物
    'https://www.tradingview.com/chart/Mr0LbiKB/', #南玻A
    'https://www.tradingview.com/chart/fBmBFdIX/', #科伦药业, SR > 5
    'https://www.tradingview.com/chart/VpgCvDG8/', #巨星科技, SR > 2
    
    #'https://www.tradingview.com/chart/VpgCvDG8/', #古井贡酒
    #'https://www.tradingview.com/chart/Mr0LbiKB/', #招商银行
    #'https://www.tradingview.com/chart/VpgCvDG8/', #海源复材
    #'https://www.tradingview.com/chart/RBVJp2WS/', #铭普光磁
    #'https://www.tradingview.com/chart/fBmBFdIX/', #中航光电
    #'https://www.tradingview.com/chart/Mr0LbiKB/', #金智科技
    ]

def openWithPython3(url=url):    
    for i in url:
        os.system("python3 -m webbrowser " + i) #220805update

def openWithPython(url=url):    
    for i in url:
        os.system("python -m webbrowser " + i)

input_msg = input("Are you sure about openning all the pages? (p3 / p)")
if input_msg == 'p3':
    openWithPython3()
elif input_msg == 'p':
    openWithPython()
else:
    print('Action aborted.')


