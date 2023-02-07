
import os
url =[
    'https://www.tradingview.com/chart/1qYvHMZe/', #BTCUSD
    'https://www.tradingview.com/chart/WFQjAmDL/', #小米
    'https://www.tradingview.com/chart/caDek3Z6/', #鼎盛新材
    'https://www.tradingview.com/chart/O5w6cxmD/', #福莱特
    'https://www.tradingview.com/chart/g5CelBO9/', #明德生物
    'https://www.tradingview.com/chart/fBmBFdIX/', #科伦药业, SR = 8
    'https://www.tradingview.com/chart/VpgCvDG8/', #巨星科技, SR = 4
    'https://www.tradingview.com/chart/RBVJp2WS/', #中钨高新
    'https://www.tradingview.com/chart/uIOtTO4I/', #深深房A
    'https://www.tradingview.com/chart/Mr0LbiKB/', #南玻A
    'https://www.tradingview.com/chart/24PY4ZGk/', #芯能科技
    'https://www.tradingview.com/chart/xN3apmRm/', #和而泰
    'https://www.tradingview.com/chart/dEaD5qXm/', #万邦达, SR = 6.8
    'https://www.tradingview.com/chart/E65JE3rd/', #GQY视讯, SR = 3.36
    'https://www.tradingview.com/chart/j8Iu5MEr/', #奥飞数据, SR = 2.89
    
    

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


