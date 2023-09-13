import tkinter.filedialog
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import Combobox

from taggen.udt.extractor import DBExtractor
from taggen.udt.dbwriter import DBWriter
from taggen.udt.taglist import TagList
from taggen import intouch
from taggen import kepserver

version = '20230707-beta-1503'
info_update = '''
更新说明：

版本：20230707-beta-1503
1、更新生成可导入文件功能，需要在DB地址定义.xlsx的udt_content中填入udt定义内容

版本：20230707-beta-0902
1、更新完全适配变量生成器自动版.xlsm的格式
2、增加'是否UDT'栏位，用于筛选需要
'''

root = Tk()
root.anchor('center')
root.title('D的自制小程序1号' + ' ' * 10 + version)
root.geometry('700x400')
# app.iconbitmap('20230707093606_38145_128.ico')
root.resizable(False, False)

# 标签
label_udt_path = Label(root, text='源文件地址：', compound='left')
label_udt_path.grid(row=0, padx=10)

# label_tia_file = Label(root, text='博图到处的DB文件地址：', justify='left')
# label_tia_file.grid(row=1, padx=10)
# label_defn_path = Label(root, text='生成文件保存地址：', justify='left')
# label_defn_path.grid(row=2, padx=10)

# UDT地址输入框
entry_udt_path = Entry(root, width=55)
entry_udt_path.grid(row=0, column=1, columnspan=6, sticky='w')
entry_udt_path.delete(0, 'end')
entry_udt_path.insert(0, r'D:\工作资料\11-PYTHON测试\DB地址定义.xlsx')

cb_intouch_mode = Combobox(root, width=8)
cb_intouch_mode.grid(row=2, column=0, padx=10)
cb_intouch_mode['value'] = ('ask', 'replace', 'update')
cb_intouch_mode.current(0)

cb_access_name = Combobox(root, width=8)
cb_access_name.grid(row=2, column=1, padx=10)
cb_access_name['value'] = ('kep1200', 'kep1500')
cb_access_name.current(1)


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
    defn_path: str = ''
    try:
        path = entry_udt_path.get()
        udt_path = path + r'/DB地址定义.xlsx'
        tia_file = path + r'/'

        extractor = DBExtractor(filename=tia_file,
                                defn_filepath=udt_path)
        writer = DBWriter()
        defn_path = tkinter.filedialog.asksaveasfilename(defaultextension=path, filetypes=[('excel文件', '.xlsx')])
        writer.write_xlsm_to_excel(extractor, filename=defn_path)
    except PermissionError:
        tkinter.messagebox.showerror('出错', f'请关掉{defn_path}再尝试')
    except ValueError:
        tkinter.messagebox.showerror('出错', f'源文件可能存在错误')
    else:
        tkinter.messagebox.showinfo('成功', f'文件保存至{defn_path}')
        # root.quit()


def generate_csv():
    try:
        path = entry_udt_path.get()
        udt_path = path + r'/DB地址定义.xlsx'
        tia_file = path + r'/'
        extractor = DBExtractor(filename=tia_file,
                                defn_filepath=udt_path)

        taglist = TagList()
        for db in extractor.db:
            taglist.traverse(db, extractor.udt_dict, extractor.struct_dict)

        intouch_path = tkinter.filedialog.asksaveasfilename(title='intouch导入文件',
                                                            defaultextension=path,
                                                            filetypes=[('csv文件', '.csv')])
        access_name = cb_access_name.get()
        intouch_mode = cb_intouch_mode.get()
        intouch.output_csv(tag_list=taglist, output_path=intouch_path,
                           access_name=access_name,
                           mode=intouch_mode,
                           item_use_tag_name=True)

        kep_path = tkinter.filedialog.asksaveasfilename(title='kep导入文件',
                                                        defaultextension=path,
                                                        filetypes=[('csv文件', '.csv')])
        kepserver.output_csv(tag_list=taglist, output_path=kep_path)

    except PermissionError:
        tkinter.messagebox.showerror('出错', f'请关掉已打开的文件再尝试')
    except ValueError:
        tkinter.messagebox.showerror('出错', f'源文件可能存在错误')
    else:
        tkinter.messagebox.showinfo('成功', f'文件保存至{intouch_path}\r{kep_path}')


button_udt_path = Button(root, text='打开', command=askdir)
button_udt_path.grid(row=0, column=7, padx=10)
button_generate = Button(root, text='生成辅助文件', command=generate)
button_generate.grid(row=1, column=7, padx=10)

button_generate = Button(root, text='生成导入文件', command=generate_csv)
button_generate.grid(row=2, column=7, padx=10)

button = Button(root, text='关闭', command=root.quit)
button.grid(row=3, column=7, padx=10)

text_help = '''
帮助
1、点击打开选择文件夹地址（文件夹中包含DB地址定义.xlsx文件以及.db文件）
2、点击生成并输入保存的文件名
'''

label_help = Label(root, width=70, height=5, text=text_help, justify='left', anchor='w')
label_help.grid(row=4, column=0, columnspan=6, padx=10)


def show_update():
    global info_update
    win_info_update = Toplevel(root)
    win_info_update.anchor('center')
    root.lower(win_info_update)
    label_update = Label(win_info_update, width=70, height=10, text=info_update, justify='left', anchor='w',
                         padx=10, pady=10)
    label_update.pack()
    b1 = Button(win_info_update, text='关闭', command=win_info_update.destroy)
    b1.pack()


show_update()
root.mainloop()
