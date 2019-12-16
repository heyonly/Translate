

from tkinter import Tk
from tkinter import Button
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import showerror

class Data:
    def __init__(self):
        self.keyList=[]
        self.info={}
    def setKey(self,key):
        self.keyList.append(key)
    def setKeyData(self,key,value):
        self.info[key]=value

    def getKey(self,key):
        return self.info.get(key)
class WorkPanel():
    def __init__(self,root):
        self.root=root
        self.fileOne=None
        self.fileTwo=None
        self.initView()
    def initView(self):
        self.root.geometry('1000x700')
        self.root.title("文件对比工具")

        btn1=Button(self.root,text="选择文件一")

        btn1.grid(row=0,column=0,sticky=W)
        # btn1.place(x=0,y=10)

        btn2 = Button(self.root, text="选择文件二")
        # btn2.place(x=80, y=10)
        btn2.grid(row=0,column=1)

        btn3 = Button(self.root, text="比较")
        # btn3.place(x=160, y=10)
        btn3.grid(row=0,column=2)

        btn4 = Button(self.root, text="清空内容")
        btn4.grid(row=0,column=3)
        # btn4.place(x=240, y=10)

        btn2["command"]=lambda btnName="btn2":self.doAction(btnName)
        btn1["command"]=lambda btnName="btn1":self.doAction(btnName)
        btn3["command"] = lambda btnName="btn3": self.doAction(btnName)
        btn4["command"] = lambda btnName="btn4": self.doAction(btnName)

        self.lb1=Label(self.root,text="文件一路径:")
        self.lb1.grid(row=1,column=0,padx=5,sticky=W)
        self.lb2=Label(self.root,text="文件二路径:")
        self.lb2.grid(row=2,column=0,padx=5,sticky=W)

        s1= Scrollbar(root)
        s2=Scrollbar(root)
        self.t1=Text(self.root,height=45,width=70)
        self.t1.grid(row=4,column=0,columnspan=6,padx=5)
        self.t1.insert(1.0,"文件一内容:\n")

        self.t2=Text(self.root,height=45,width=70)
        s1.grid(row=4,column=7,sticky=N+S+W+E)
        self.t2.grid(row=4,column=6,columnspan=6,padx=5)
        self.t2.insert(1.0,"文件二内容:\n")
        s2.grid(row=4,column=13,sticky=N+S+W+E)
        self.t1.config(yscrollcommand=s1.set)
        s1.config(command=self.t1.yview)

        self.t2.config(yscrollcommand=s2.set)
        s2.config(command=self.t2.yview)
    def doAction(self,btnName):
        if btnName=="btn1":
            self.fileOne=fileOne=askopenfilename()
            if not fileOne:return
            self.lb1["text"]=self.lb1["text"]+" "+fileOne
        if btnName=="btn2":
            self.fileTwo=fileTwo = askopenfilename()
            if not fileTwo: return
            self.lb2["text"]=self.lb2["text"]+" "+fileTwo

        if btnName=="btn3":
            if not self.fileOne and not self.fileTwo:
                showerror("error","请选择两个文件进行对比")
            self.sortValue(self.fileOne,self.fileTwo)

        if btnName=="btn4":
            self.t1.delete(0.0,END)
            self.t2.delete(0.0, END)

            self.t1.insert(1.0, "文件一内容:\n")
            self.t2.insert(1.0, "文件二内容:\n")

    def replace(self,value):
        value=value.replace("”","")
        value=value.replace("“","")
        value=value.replace("\"","")
        return value.strip()
    def getData(self,fileObj,data):
        with open(fileObj,"r",encoding="utf-8") as f1:
            for line in f1:
                if "#" in line or "//" in line:continue
                if len(line.split("="))<=1:continue
                key=line.split("=")[0]
                value=line.split("=")[1]
                key=self.replace(key)
                value=self.replace(value)
                data.setKey(key)
                data.setKeyData(key,value)
    def sortValue(self,fileOne,fileTwo):
        self.first=Data()
        self.two=Data()
        self.getData(fileOne,self.first)
        self.getData(fileTwo,self.two)
        self.showSame()
    def showSame(self):
        self.sameOne=self.first.keyList
        self.sameTwo=self.two.keyList
        keySame=set(self.sameOne).intersection(self.sameTwo)
        differentOne=set(self.sameOne).difference(self.sameTwo)
        differentTwo=set(self.sameTwo).difference(self.sameOne)
        self.t1.tag_config('a', foreground='red')
        self.t1.tag_config('b', foreground='blue')

        self.t2.tag_config('a', foreground='red')
        self.t2.tag_config('b', foreground='blue')

        self.t1.insert(END, "==========================相同的===============================\n")
        self.t2.insert(END, "==========================相同的==============================\n")
        scroll1 = Scrollbar()
        scroll2 =Scrollbar()
        # scroll1.place(x=10,y=10)
        scroll1.config(command=self.t1.yview)  # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
        self.t1.config(yscrollcommand=scroll1.set)

        scroll1.config(command=self.t2.yview)  # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
        self.t2.config(yscrollcommand=scroll2.set)

        for same in keySame:
            value="\"{}\"".format(same)
            self.t1.insert(END,value,"b")
            self.t1.insert(END, "= \"{}\"\n".format(self.first.getKey(same)))
            self.t2.insert(END, value, "b")
            self.t2.insert(END, "= \"{}\"\n".format(self.two.getKey(same)))



        self.t1.insert(END, "===========================不相同的===============================\n")
        self.t2.insert(END, "==========================不相同的================================\n")


        for difA in differentOne:
            value = "\"{}\"".format(difA)
            self.t1.insert(END, value, "a")
            self.t1.insert(END, "= \"{}\"\n".format(self.first.getKey(difA)))

        for difB in differentTwo:
            value = "\"{}\"".format(difB)
            self.t2.insert(END, value, "a")
            self.t2.insert(END, "= \"{}\"\n".format(self.two.getKey(difB)))





if __name__ == '__main__':
    root=Tk()
    work=WorkPanel(root)
    root.mainloop()