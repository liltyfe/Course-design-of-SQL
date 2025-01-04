import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.dialogs import Messagebox
import webbrowser

"""基础类"""


class select_frame(ttk.Frame):
    def __init__(self, master, text, function_Select, function_Exit):
        super().__init__(master)

        self.text = text

        self.ent_frame = EnterPage(self, self.text)
        self.ent_frame.pack(fill=X, pady=10)

        self.show_tree = ttk.Treeview(
            self,
            columns=("Name", "ID", "Math Score", "Chinese Score", "English Score"),
            show="headings",
            height=10
        )

        # 设置表头
        self.show_tree.heading("Name", text="Name", anchor=CENTER)
        self.show_tree.heading("ID", text="ID", anchor=CENTER)
        self.show_tree.heading("Chinese Score", text="Chinese Score", anchor=CENTER)
        self.show_tree.heading("Math Score", text="Math Score", anchor=CENTER)
        self.show_tree.heading("English Score", text="English Score", anchor=CENTER)

        # 设置列宽
        self.show_tree.column("Name", width=150, anchor=CENTER)
        self.show_tree.column("ID", width=100, anchor=CENTER)
        self.show_tree.column("Chinese Score", width=200, anchor=CENTER)
        self.show_tree.column("Math Score", width=200, anchor=CENTER)
        self.show_tree.column("English Score", width=200, anchor=CENTER)
        self.show_tree.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        self.btn_frame = ttk.Frame(self)
        self.btn_frame.pack(fill=X, pady=10)

        self.btn_select = ttk.Button(self.btn_frame, text="Select", command=function_Select, bootstyle=SUCCESS, width=6)
        self.btn_exit = ttk.Button(self.btn_frame, text="Exit", command=function_Exit, bootstyle=DANGER, width=6)
        self.btn_select.pack(padx=5, side=RIGHT)
        self.btn_exit.pack(padx=5, side=RIGHT)


class EnterPage(ttk.Frame):
    def __init__(self, master, text):
        super().__init__(master)

        self.text = text
        self.data_get = ttk.StringVar(value="")
        self.ent_frame = ttk.Frame(self)
        self.ent_frame.pack(fill=X, pady=10)
        self.label_student = ttk.Label(self.ent_frame, text=self.text, font=("Helvetica", 12), width=20)
        self.entry_student = ttk.Entry(self.ent_frame, textvariable=self.data_get)
        self.label_student.pack(side=LEFT, padx=5)
        self.entry_student.pack(side=LEFT, padx=5, fill=X, expand=YES)


class Student(object):
    def __init__(self, name, id, math_score, chinese_score, english_score):
        self.name = name
        self.id = id
        self.math_score = math_score
        self.chinese_score = chinese_score
        self.english_score = english_score


"""以下是五个界面"""


class Insert_Page(ttk.Frame):
    def __init__(self, master, db):
        super().__init__(master)

        self.db = db

        self.student = Student(id=ttk.StringVar(value=""),
                               name=ttk.StringVar(value=""),
                               math_score=ttk.StringVar(value=""),
                               chinese_score=ttk.StringVar(value=""),
                               english_score=ttk.StringVar(value=""))

        self.label_title = ttk.Label(self, text="Insert Page", font=("Helvetica", 16))
        self.label_title.pack(pady=30, anchor=CENTER)

        self.ent_name_frame = self.create_entry_frame("Student Name:", self.student.name)
        self.ent_id_frame = self.create_entry_frame("Student ID:", self.student.id)
        self.ent_math_score_frame = self.create_entry_frame("Student Math Score:", self.student.math_score)
        self.ent_chinese_score_frame = self.create_entry_frame("Student Chinese Score:", self.student.chinese_score)
        self.ent_english_score_frame = self.create_entry_frame("Student English Score:", self.student.english_score)
        self.ent_name_frame.pack(fill=X, pady=30)
        self.ent_id_frame.pack(fill=X, pady=30)
        self.ent_math_score_frame.pack(fill=X, pady=30)
        self.ent_chinese_score_frame.pack(fill=X, pady=30)
        self.ent_english_score_frame.pack(fill=X, pady=30)

        self.btn_frame = ttk.Frame(self)
        self.btn_frame.pack(fill=X, pady=5)

        self.btn_submit = ttk.Button(self, text="Submit", command=self.submit_inquire, bootstyle=SUCCESS, width=6)
        self.btn_exit = ttk.Button(self, text="Exit", command=self.destroy, bootstyle=DANGER, width=6)
        self.btn_submit.pack(padx=5, side=RIGHT)
        self.btn_exit.pack(padx=5, side=RIGHT)

    def create_entry_frame(self, text, data_get):
        ent_frame = ttk.Frame(self)
        ent_frame.pack(fill=X, pady=10)
        label_student = ttk.Label(ent_frame, text=text, font=("Helvetica", 12), width=20)
        entry_student = ttk.Entry(ent_frame, textvariable=data_get)
        label_student.pack(side=LEFT, padx=5)
        entry_student.pack(side=LEFT, padx=5, fill=X, expand=YES)
        return ent_frame

    def submit_inquire(self):
        flag = self.db.insert_data(self.student.name.get(), self.student.id.get(), self.student.math_score.get(),
                                   self.student.chinese_score.get(), self.student.english_score.get())
        self.student.name.set("")
        self.student.id.set("")
        self.student.math_score.set("")
        self.student.chinese_score.set("")
        self.student.english_score.set("")
        if flag:
            messagebox = Messagebox()
            messagebox.ok("Insert data success!", text="Insert success")
        else:
            messagebox = Messagebox()
            messagebox.show_error("Insert data failed!", text="Insert failed")

    def destroy(self):
        self.quit()


class Delete_Page(ttk.Frame):
    def __init__(self, master, db):
        super().__init__(master)

        self.db = db

        self.label_title = ttk.Label(self, text="Delete Page", font=("Helvetica", 16))
        self.label_title.pack(pady=30, anchor=CENTER)

        # self.student = Student(id=None, name=None, math_score=None, chinese_score=None, english_score=None)

        self.ent_name_frame = EnterPage(self, "Student Name:")

        self.ent_name_frame.pack(fill=X, pady=30)

        self.btn_frame = ttk.Frame(self)
        self.btn_frame.pack(fill=X, pady=10)

        self.btn_submit = ttk.Button(self, text="Submit", command=self.submit_inquire, bootstyle=SUCCESS, width=6)
        self.btn_exit = ttk.Button(self, text="Exit", command=self.destroy, bootstyle=DANGER, width=6)
        self.btn_submit.pack(padx=5, side=RIGHT)
        self.btn_exit.pack(padx=5, side=RIGHT)

    def submit_inquire(self):
        flag = self.db.delete_data(self.ent_name_frame.data_get.get())
        self.ent_name_frame.data_get.set("")
        if flag:
            messagebox = Messagebox()
            messagebox.ok("Delete data success!", text="Delete success")
        else:
            messagebox = Messagebox()
            messagebox.show_error("Delete data failed!", text="Delete failed")

    def destroy(self):
        self.quit()


class Show_Page(ttk.Frame):
    def __init__(self, master, db):
        super().__init__(master)

        self.db = db

        self.label_title = ttk.Label(self, text="Show Page", font=("Helvetica", 16))
        self.label_title.pack(pady=30, anchor=CENTER)

        self.tree = ttk.Treeview(
            self,
            columns=("Name", "ID", "Math Score", "Chinese Score", "English Score"),
            show="headings",
            height=10
        )
        self.tree.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        # 设置表头
        self.tree.heading("Name", text="Name", anchor=CENTER)
        self.tree.heading("ID", text="ID", anchor=CENTER)
        self.tree.heading("Chinese Score", text="Chinese Score", anchor=CENTER)
        self.tree.heading("Math Score", text="Math Score", anchor=CENTER)
        self.tree.heading("English Score", text="English Score", anchor=CENTER)

        # 设置列宽
        self.tree.column("Name", width=150, anchor=CENTER)
        self.tree.column("ID", width=100, anchor=CENTER)
        self.tree.column("Chinese Score", width=200, anchor=CENTER)
        self.tree.column("Math Score", width=200, anchor=CENTER)
        self.tree.column("English Score", width=200, anchor=CENTER)

        self.btn_frame = ttk.Frame(self)
        self.btn_frame.pack(fill=X, pady=5)

        self.btn_update = ttk.Button(self, text="Update", command=self.update_data, bootstyle=SUCCESS, width=6)
        self.btn_update.pack(padx=5, side=RIGHT)

        self.btn_exit = ttk.Button(self, text="Exit", command=self.destroy, bootstyle=DANGER, width=6)
        self.btn_exit.pack(padx=5, side=RIGHT)

        self.insert_data()

    def insert_data(self):
        # 插入数据
        stu_Data = self.db.show_data()
        # print(stu_Data)
        for stu in stu_Data:
            self.tree.insert("", "end", values=(stu[0], stu[1], stu[2], stu[3], stu[4]))

    def clear_data(self):
        """清空 Treeview 数据"""
        self.tree.delete(*self.tree.get_children())

    def update_data(self):
        self.clear_data()
        self.insert_data()

    def destroy(self):
        self.quit()


class Select_Page(ttk.Frame):
    def __init__(self, master, db):
        super().__init__(master)

        self.db = db

        self.label_title = ttk.Label(self, text="Select Page", font=("Helvetica", 16))
        self.label_title.pack(pady=30, anchor=CENTER)

        # self.student = Student(id=None, name=None, math_score=None, chinese_score=None, english_score=None)

        self.combobox = ttk.Combobox(self, values=["ID Select", "Name Select"])
        self.combobox.pack(pady=10)
        self.combobox.current(0)  # 默认选中第一个选项
        self.combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)

        self.id_select_frame = select_frame(self, "ID Select:", self.Select_by_Id, self.destroy)
        self.name_select_frame = select_frame(self, "Name Select:", self.Select_by_Name, self.destroy)

        self.show_id_select_page()

    def on_combobox_select(self, event):
        selected_page = self.combobox.get()
        if selected_page == "ID Select":
            self.show_id_select_page()
        elif selected_page == "Name Select":
            self.show_name_select_page()

    def Select_by_Id(self):
        result = self.db.select_data_id(self.id_select_frame.ent_frame.data_get.get())
        self.id_select_frame.ent_frame.data_get.set("")
        if result is not None:
            self.id_select_frame.show_tree.insert("", "end",
                                                  values=(result[0], result[1], result[2], result[3], result[4]))

    def show_id_select_page(self):
        self.forget_page()
        self.id_select_frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    def show_name_select_page(self):
        self.forget_page()
        self.name_select_frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    def forget_page(self):
        self.id_select_frame.forget()
        self.name_select_frame.forget()

    def Select_by_Name(self):
        result = self.db.select_data_name(self.name_select_frame.ent_frame.data_get.get())
        self.name_select_frame.ent_frame.data_get.set("")
        if result is not None:
            self.name_select_frame.show_tree.insert("", "end",
                                                    values=(result[0], result[1], result[2], result[3], result[4]))

    def destroy(self):
        self.quit()


class About_Page(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_title = ttk.Label(self, text="About Page", font=("Helvetica", 16))
        self.label_title.pack(pady=30, anchor=CENTER)

        self.label_about1 = ttk.Label(self, text="这是一个超级无敌简单的数据库管理系统demo，版本V0.1",
                                      font=("Helvetica", 12))
        self.label_about1.pack(expand=YES, padx=20, pady=5)
        self.label_about2 = ttk.Label(self,
                                      text="使用 tkinter 完成 GUI 设计，美化使用ttkbootstrap库，使用 MySQL 完成数据库操作。",
                                      font=("Helvetica", 12))
        self.label_about2.pack(expand=YES, padx=20, pady=5)
        self.label_about3 = ttk.Label(self, text="这个视频对我有很大的启发和帮助（可点击）。", font=("Helvetica", 12))
        self.label_about3.pack(expand=YES, padx=20, pady=5)

        def open_url(event):
            webbrowser.open(
                "https://www.bilibili.com/video/BV1Uv4y1X76n/?spm_id_from=333.337.search-card.all.click&vd_source=958633e12684eb6031a43772ebfbd213",
                new=0)

        self.label_about3.bind("<Button-1>", open_url)
        self.label_about = ttk.Label(self,
                                     text="总之经过不断的努力和学习，我终于还是把这东西搓出来了，其实还是挺有意思的。",
                                     font=("Helvetica", 12))
        self.label_about.pack(expand=YES, padx=20, pady=5)
        self.label_about = ttk.Label(self, text="人生建议，最好把每个frame写成一个类，会简化很多工作。",
                                     font=("Helvetica", 12))
        self.label_about.pack(expand=YES, padx=20, pady=5)
        self.label_about = ttk.Label(self, text="祝你人生顺利，天天开心。", font=("Helvetica", 12))
        self.label_about.pack(expand=YES, padx=20, pady=5)
        self.label_about = ttk.Label(self, text="仅供学习交流使用。", font=("Helvetica", 12))
        self.label_about.pack(expand=YES, padx=20, pady=5)

        self.btn_exit = ttk.Button(self, text="Exit", command=self.destroy)
        self.btn_exit.pack(pady=10, anchor=E)

    def destroy(self):
        self.quit()


if __name__ == '__main__':
    root = ttk.Window()
    root.title("Student Management System")
    root.geometry("2000x1000")
    app = Insert_Page(root)
    app.pack(fill=BOTH, expand=YES)
    root.mainloop()
