import tkinter
import random

root = tkinter.Tk()
root.geometry("1200x800")
root.title("猜数字游戏")

hits = 0
submission_count = 0

# 初始化输入和结果变量
g_var = [tkinter.StringVar() for _ in range(4)]
result_vars = [[tkinter.StringVar() for _ in range(4)] for _ in range(2)]
# 生成目标答案
# 生成随机目标数字
target = [random.randint(0, 9) for _ in range(4)]
print(target)


# 编写程序功能
def write_num(num):
    global hits
    g_var[hits%4].set(num)
    hits += 1
     
    
# 清空数字输入
def clear_number():
    global hits
    hits = 0
    for var in g_var:
        var.set("")  # 清空每个StringVar的值
        
        
# 提交并于正确答案比较
# 将输入组件的4个数字存放在一个结果组件之中
def submit_and_compare():
    global submission_count
    
    var = tkinter.StringVar()
    
    current_result = "   ".join(var.get() for var in g_var)
    
    print(current_result)
    
    row = submission_count % 4
    col = submission_count // 4
    
    if col > 1:
        print("结果组件已满")
        return
    
    result_vars[col][row].set(current_result)
    
    submission_count += 1
    
    print("比较答案")
    correct_count = sum(1 for i in range(4) if int(current_result[i]) == target[i])
    print(f"用户输入正确的数字数量: {correct_count}")



#添加清空按钮
clear_button = tkinter.Button(root, bg="lightblue", text = "清空", font = (33), command=clear_number)
clear_button.place(x=700, y=700, width=100, height=40)
    


# 构建数字
for i in range(10):
    exec('''bn{} = tkinter.Button(root,bg="pink",text="{}",font=(33),command=lambda:write_num({}))'''.format(i,i,i))
    exec("bn{}.place(x=20+{}*60,y=700,width=40,height=40)".format(i,i))
    

# 输入组件
for i in range(4):
    exec('''lb{}=tkinter.Label(root,bg="pink",font=(30),textvariable=g_var[{}])'''.format(i,i,i))
    exec("lb{}.place(x=40+{}*200,y=100,width=150,height=150)".format(i,i))
        

# 存放结果组件(左边)
for i in range(4):
    lb_t=tkinter.Label(root,bg="pink",font=(30),textvariable=result_vars[0][i],anchor='w')
    lb_t.place(x=40,y=300 + (i * 70),width=350,height=40)
    
for i in range(4):
    lb_t=tkinter.Label(root,bg="pink",font=(30),textvariable=result_vars[1][i])
    lb_t.place(x=430,y=300 + (i * 70),width=350,height=40)
    
# 添加提交按钮
submit_button = tkinter.Button(root,bg="lightgreen",text="提交",font=33,command=submit_and_compare)
submit_button.place(x=250, y=600, width=300, height=70)


root.mainloop()