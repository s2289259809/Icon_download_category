import requests
import re
import time
import pandas as pd
import os
import json
import tkinter as tk
import tkinter.messagebox
import icon

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
Package_names=[]
name=[]
error=[]
excep=[]
id=[]
def copy(pp):
    a=int(pp)+1
    for j in range(1,a):
        r = requests.get("http://app.mi.com/topList?page="+str(j), headers=headers)
        '''图片连接(正则)'''
        ec='id=([^"]+[^"])">(.{0,30})</a>'
        ev='http+://file.market.xiaomi.com/thumbnail/PNG/+[^\s]*'
        c = re.findall(ec, r.text, re.S)
        v = re.findall(ev, r.text, re.S)
        print('目前第%s页'%j)
        for i in range(len(c)):
            icon = c[i]
            b=v[i]
            url = b[:-1]
            # data={
            #     '包名':[icon[0]],
            #     '中文':[icon[1]]
            # }
            # df=pd.DataFrame(data)
            # df.to_csv("C:/Users/Wj009/Desktop/0/包名.csv", encoding="gbk", mode="a", index=False)
            r = requests.get(url=url, headers=headers)
            # with open('E:/icon/'+str(icon[0])+'-'+str(icon[1])+'.png', 'wb')as png: png.write(r.content)
            # print(icon)
            Package_names.append(icon[0])
            name.append(icon[1])

'''匹配文字公共长度'''
def getNumofCommonSubstr(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]  # 多一位
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位

    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i + 1][j + 1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    return str1[p - maxNum:p], maxNum

'''请求苹果高清图片'''
def apple_id():

    for i in range(len(name)):
        icon = name[i]
        try:
            url = 'https://itunes.apple.com/search?country=CN&media=software&entity=software&limit=6&term=' +icon
            re = requests.get(url=url, headers=headers)
            re = json.loads(re.text)
            '''id苹果市场的名称，re软件链接'''
            id = re['results'][0]['trackCensoredName']
            re = re['results'][0]['artworkUrl60']
            res = re.replace("60x60", "1024x1024")
            print(icon)
            if icon == getNumofCommonSubstr(icon,id)[0]:
                apple_icon=requests.get(url=res,headers=headers)
                with open('E:/icon/'+Package_names[i] + '.png', 'wb')as png: png.write(apple_icon.content)
                time.sleep(0.3)
            else:
                time.sleep(0.3)
                error.append(Package_names[i])
        except:
            print('Zzz')
            time.sleep(0.2)

def difference():
    for root, dirs, files in os.walk('./'):
        for f in files:
            id.append(f[0:-4])
    c = list(set(error).difference(set(id)))
    return c

def mi_id():
    try:
        os.mkdir('E:/icon')
        os.mkdir('E:/图标')
    except:
        pass
    copy(mub.get().strip())
    apple_id()
    a=difference()
    print(a)
    for i in range(len(a)):
        url='http://app.mi.com/details?id='+str(difference()[i])
        rea=requests.get(url=url,headers=headers)
        ec='src="(http://file.market.xiaomi.com/thumbnail/PNG/l114/.*)" alt=".*" width="114" height="114">'
        yy = re.findall(ec, rea.text, re.S)
        res = yy[0].replace("l114", "l1024")
        mi=requests.get(url=res,headers=headers)
        print(res)
        with open('E:/icon/'+str(difference()[i]) + '.png', 'wb')as png: png.write(mi.content)
        # time.sleep(0.3)

def gui():
    top = tk.Tk()
    top.title('下载图标并进行对比')
    top.geometry('300x150')
    '''显示文字'''
    l=tk.Label(top,text='输入需要爬取的页数(数字)', bg='green', font=('Arial', 12), width=30, height=2)
    l.pack()

    '''输入框'''
    global mub
    mub=tk.Entry(top, show=None,  font=('Arial', 14))
    mub.pack()

    #按钮
    buttons = tk.Button(top, text="爬取", fg="white", bg="OliveDrab", command=mi_id)
    buttons.pack()

    buttons = tk.Button(top, text="对比", fg="white", bg="OliveDrab", command=icon.play)
    buttons.pack()
    top.mainloop()

if __name__ == '__main__':
    gui()

