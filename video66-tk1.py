from tkinter import * #导入全部后，与之前的区别就是在调用tk函数时，不用写出tk
def callback():
    var.set('我才不信！')



root = Tk()
root.title('性感荷官，在线发牌')
#设置两个frame， 来分别装不同的内容
#frame1 装textLable和imgLable,  frame2 装Button
frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('下载的影片含有未成年限制内容，\n请满18岁后再点击!')

#textvariable 使文本内容可变 ，显示tkinter的变量。text显示字符串，
textLable = Label(frame1,textvariable =var ,
                    font = ('Helvetica', 30 ,'bold'), #设置字体格式 大小 bold：黑体
                  justify = LEFT)#justify 是对齐，默认为居中
textLable.pack(side = LEFT)

photo = PhotoImage(file='./18.png') # tkinter的一个图片对象  实例化之后就可以获取图像
imgLable = Label(frame1,image=photo)
imgLable.pack(side=RIGHT)

theButton = Button(frame2,text='我已满18岁',command =callback)
theButton.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)
# <倒数日>app人机交互分析报告

mainloop()