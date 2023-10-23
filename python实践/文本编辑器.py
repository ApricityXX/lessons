import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import simpledialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("文本编辑器")
        self.text_area = scrolledtext.ScrolledText(root, width=80, height=30, undo=True)
        self.text_area.pack()
        self.file_path = None
        self.text_modified = False

        # 创建菜单栏
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # 创建文件菜单
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="打开 -Control-o", command=self.open_file)
        self.file_menu.add_command(label="保存 -Control-s", command=self.save_file)
        self.file_menu.add_command(label="另存为 -Control-Shift-s", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="退出", command=self.exit_app)
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)

        # 创建编辑菜单
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="撤销 -Control-z", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="重做 -Control-y", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="查找 -Control-f", command=self.find_text)
        self.edit_menu.add_command(label="替换 -Control-r", command=self.replace_text)
        self.menu_bar.add_cascade(label="操作", menu=self.edit_menu)

        # 绑定快捷键
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-Shift-s>", lambda event: self.save_file_as())
        self.root.bind("<Control-z>", lambda event: self.text_area.edit_undo())
        self.root.bind("<Control-y>", lambda event: self.text_area.edit_redo())
        self.root.bind("<Control-f>", lambda event: self.find_text())
        self.root.bind("<Control-r>", lambda event: self.replace_text())

        # 监听文本修改
        self.text_area.bind("<<Modified>>", self.text_modified_callback)

        # 创建帮助菜单
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="使用说明", command=self.show_help)
        self.menu_bar.add_cascade(label="帮助", menu=self.help_menu)

    def open_file(self):
        # 弹出打开文件对话框
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                # 打开文件并读取内容
                with open(file_path, "r") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
                    self.file_path = file_path
                    self.text_modified = False
                    self.root.title("Text Editor - " + file_path)
            except Exception as e:
                # 处理异常并显示错误消息
                messagebox.showerror("Error", str(e))

    def save_file(self):
        if self.file_path:
            try:
                # 将文本内容保存到文件
                with open(self.file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                    self.text_modified = False
                    messagebox.showinfo("保存", "成功保存")
            except Exception as e:
                # 处理异常并显示错误消息
                messagebox.showerror("Error", str(e))
        else:
            self.save_file_as()

    def save_file_as(self):
        # 弹出另存为文件对话框
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                # 将文本内容保存到指定文件
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                    self.file_path = file_path
                    self.text_modified = False
                    self.root.title("Text Editor - " + file_path)
                    messagebox.showinfo("保存", "文件成功保存")
            except Exception as e:
                # 处理异常并显示错误消息
                messagebox.showerror("Error", str(e))

    def exit_app(self):
        if self.text_modified:
            # 如果文本被修改过，则弹出确认对话框询问是否保存
            save_changes = messagebox.askyesnocancel("退出", "你要保存变化吗？")
            if save_changes is None:
                return
            elif save_changes:
                self.save_file()
        self.root.destroy()

    def find_text(self):
        # 弹出查找对话框并获取要查找的文本
        search_text = simpledialog.askstring("查找", "输入要查找的文本:")
        if search_text:
            content = self.text_area.get(1.0, tk.END)
            start_index = content.find(search_text)
            if start_index != -1:
                end_index = start_index + len(search_text)
                # 选中匹配的文本
                self.text_area.tag_add(tk.SEL, f"1.0 + {start_index}c", f"1.0 + {end_index}c")
                self.text_area.focus_set()
                self.text_area.tag_config(tk.SEL, background="yellow")
            else:
                messagebox.showinfo("查找", "找不到指定的文本。")

    def replace_text(self):
        # 弹出替换对话框并获取要查找和替换的文本
        search_text = simpledialog.askstring("替换", "输入要查找的文本:")
        if search_text:
            replace_text = simpledialog.askstring("替换", "输入要替换成的文本:")
            if replace_text:
                content = self.text_area.get(1.0, tk.END)
                modified_content = content.replace(search_text, replace_text)
                if modified_content != content:
                    # 替换文本并标记为已修改
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, modified_content)
                    self.text_modified = True

    def text_modified_callback(self, event):
        # 监听文本修改事件
        self.text_modified = True

    def show_help(self):
        # 显示帮助信息
        help_text = """使用说明：
- 打开文件：Ctrl + O
- 保存文件：Ctrl + S
- 另存为：Ctrl + Shift + S
- 撤销：Ctrl + Z
- 重做：Ctrl + Y
- 查找：Ctrl + F
- 替换：Ctrl + R

"""
        messagebox.showinfo("帮助", help_text)

# 创建主窗口
root = tk.Tk()

# 创建文本编辑器实例
text_editor = TextEditor(root)

# 运行应用程序
root.mainloop()
