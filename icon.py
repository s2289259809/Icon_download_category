import os
import shutil
import pandas as pd

def copy1(bi):
    icon=[]
    yuanlai=[]
    '''遍历待添加的图标'''
    for root, dirs, files in os.walk("E:/icon", topdown=False):
        for name in files:
            local = os.path.join(root, name)
            icon_1=local[8:-4]
            icon.append(icon_1)
    '''遍历之前存在的图标'''
    for root1, dirs1,files1 in os.walk(bi, topdown=False):
        for name1 in files1:
            local1 = os.path.join(name1)
            icon_2=local1[:-4]
            yuanlai.append(icon_2)
    '''对比两个文件夹并输出没有的文件'''
    mk = bi[22:28]
    os.mkdir('E:/图标/' +mk)
    aab=set(icon).difference(yuanlai)
    aaab=tuple(aab)
    for i in range(len(aaab)):
        b = aaab[i]
        data = {
            '包名': [b]
        }
        df = pd.DataFrame(data)
        df.to_csv('E:/图标/'+mk+'/包名.csv', encoding="gbk", mode="a", index=False)
        p='E:/icon/'+b+'.png'
        shutil.copy(p,'E:/图标/'+mk)
        print(b)
    df = pd.read_csv('E:/图标/' + mk + '/包名.csv', engine='python', encoding='gbk')
    df1 = df[df['包名'] != "包名"]
    df1.to_csv('E:/图标/' + mk + '/包名.csv', encoding="gbk")
def xlsx(bi):
    mk = bi[22:28]
    df=pd.read_csv('E:/图标/'+mk+'/包名.csv',engine='python',encoding='gbk')
    df1=df[df['包名']!="包名"]
    df1.to_csv('E:/图标/' + mk + '/包名.csv', encoding="gbk")

def play():
    copy1('//Vicgee/主题项目/02图标包/03OS类图标包/01普通OS类图标包/第三方完成')
    copy1('//Vicgee/主题项目/02图标包/04扁平类图标包/01For扁平风图标包/01扁平风（新）')
    copy1('//Vicgee/主题项目/02图标包/02纯色类图标包/01纯色小图标包/01纯白色')
    copy1('//Vicgee\主题项目/02图标包/01线性类图标包/01简线整合包/01经典灰')

if __name__ == '__main__':
    play()
