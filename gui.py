import PySimpleGUI as sg
from fuc import en_rc4, get_str,de_rc4

sg.theme('DarkAmber')  # 设置当前主题
# 界面布局，将会按照列表顺序从上往下依次排列，二级列表中，从左往右依此排列
layout = [[sg.Text('message'), sg.InputText(key='message')],
          [sg.Text('key     '), sg.InputText(key='key')],
          [sg.Text("", key='show')],
          [sg.Button('加密'), sg.Button('解密')]]

# 创造窗口
window = sg.Window('网络安全理论与技术', layout)
# 事件循环并获取输入值
en_message = []
ks=[]



while True:
    event, values = window.read()
    if event == None:  # 如果用户关闭窗口或点击`Cancel`
        break
    if event in ('加密'):
        ks, en_message = en_rc4(values['message'],values['key'])
        str = get_str(en_message)
        str="密文："+str
        window['show'].update(str)
        print('encrypt sucess')
    if event in ("解密"):
        de_meg=de_rc4(ks,en_message)
        str="明文："
        str=str+"".join(de_meg)
        window['show'].update(str)
        print('decrypt sucess')
window.close()
