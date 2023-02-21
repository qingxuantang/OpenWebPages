
import os
url =[
    'https://www.tradingview.com/chart/1qYvHMZe/', #BTCUSD
    'https://www.tradingview.com/chart/WFQjAmDL/', #Xiao Mi
    'https://www.tradingview.com/chart/caDek3Z6/', #Ding Sheng Xin Cai
    'https://www.tradingview.com/chart/O5w6cxmD/', #Fu Lai Te
    'https://www.tradingview.com/chart/g5CelBO9/', #Ming De Sheng Wu
    'https://www.tradingview.com/chart/fBmBFdIX/', #KE Lun Yao Ye, SR = 8
    'https://www.tradingview.com/chart/VpgCvDG8/', #Ju Xing Ke Ji, SR = 4
    'https://www.tradingview.com/chart/RBVJp2WS/', #Zhong Wu Gao Xin
    'https://www.tradingview.com/chart/uIOtTO4I/', #Shen Shen Fang A
    'https://www.tradingview.com/chart/Mr0LbiKB/', #Nan Bo A
    'https://www.tradingview.com/chart/24PY4ZGk/', #Xin Neng Ke Ji
    'https://www.tradingview.com/chart/xN3apmRm/', #He Er Tai
    'https://www.tradingview.com/chart/dEaD5qXm/', #Wan Bang Da, SR = 6.8
    'https://www.tradingview.com/chart/E65JE3rd/', #GQY Shi Xun, SR = 3.36
    'https://www.tradingview.com/chart/j8Iu5MEr/', #Ao Fei Shu Ju, SR = 2.89
    'https://www.tradingview.com/chart/2GxFomf3/', #Shen Zhou Shu Ma，
    
    

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


