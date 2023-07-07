import tkinter.filedialog
import tkinter.messagebox
from tkinter import *
from taggen.udt.extractor import DBExtractor
from taggen.udt.dbwriter import DBWriter

version = '20230707-beta-0902'
info_update = '''
更新内容：20230707-beta-0902
1、更新完全适配变量生成器自动版.xlsm的格式
2、增加'是否UDT'栏位，用于筛选需要
'''

app = Tk()
app.title('D的自制小程序1号' + ' ' * 10 + version)
app.geometry('600x300')
# app.iconbitmap('20230707093606_38145_128.ico')
app.resizable(False, False)

# 标签
label_udt_path = Label(app, text='源文件地址：', compound='left')
label_udt_path.grid(row=0, padx=10)

# label_tia_file = Label(root, text='博图到处的DB文件地址：', justify='left')
# label_tia_file.grid(row=1, padx=10)
# label_defn_path = Label(root, text='生成文件保存地址：', justify='left')
# label_defn_path.grid(row=2, padx=10)

# UDT地址输入框
entry_udt_path = Entry(app, width=55)
entry_udt_path.grid(row=0, column=1)
entry_udt_path.delete(0, 'end')
entry_udt_path.insert(0, r'D:\工作资料\11-PYTHON测试\DB地址定义.xlsx')


def askdir():
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        entry_udt_path.delete(0, 'end')
        entry_udt_path.insert(0, filename)
    else:
        entry_udt_path.delete(0, 'end')
        entry_udt_path.insert(0, '你没有选择文件')


# # DB地址输入框
# entry_tia_file = Entry(root, width=50)
# entry_tia_file.grid(row=1, column=1)
# entry_tia_file.delete(0, 'end')
# entry_tia_file.insert(0, r'D:\工作资料\11-PYTHON测试\tia_file\HP_S_ALL.db')
#
# # UDT地址输入框
# entry_defn_path = Entry(root, width=50)
# entry_defn_path.grid(row=2, column=1)
# entry_defn_path.delete(0, 'end')
# entry_defn_path.insert(0, r'D:\工作资料\11-PYTHON测试\db_defn.xlsx')


def generate():
    try:
        path = entry_udt_path.get()
        udt_path = path + r'/DB地址定义.xlsx'
        tia_file = path + r'/'
        # defn_path = path + r'/变量生成辅助文件.xlsx'
        extractor = DBExtractor(filename=tia_file,
                                defn_filepath=udt_path)
        writer = DBWriter()
        defn_path = tkinter.filedialog.asksaveasfilename(defaultextension=path, filetypes=[('excel文件', '.xlsx')])
        writer.write_xlsm_to_excel(extractor, filename=defn_path)
    except PermissionError:
        tkinter.messagebox.showerror('出错', f'请关掉{defn_path}再尝试')
    else:
        tkinter.messagebox.showinfo('成功', f'文件保存至{defn_path}')
        # root.quit()


button_udt_path = Button(app, text='打开', command=askdir)
button_udt_path.grid(row=0, column=3, padx=10)
button_generate = Button(app, text='生成', command=generate)
button_generate.grid(row=1, column=3, padx=10)

button = Button(app, text='关闭', command=app.quit)
button.grid(row=3, column=3, padx=10)

text_help = '''
帮助
1、点击打开选择文件夹地址（文件夹中包含DB地址定义.xlsx文件以及.db文件）
2、点击生成并输入保存的文件名
'''

label_help = Label(app, width=60, height=5, text=text_help, justify='left', anchor='w')
label_help.grid(row=4, column=1)
label_update = Label(app, width=60, height=5, text=info_update, justify='left', anchor='w')
label_update.grid(row=5, column=1)

app.mainloop()
