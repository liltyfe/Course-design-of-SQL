import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from page import Insert_Page, Delete_Page, Show_Page, Select_Page, About_Page, Student
from db import Database



class FunctionDemo(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.navbar = ttk.Frame(self, bootstyle=SECONDARY)
        self.navbar.pack(side=TOP, fill=X)

        self.database = Database()

        self.insert_page = Insert_Page(self, self.database)
        self.delete_page = Delete_Page(self, self.database)
        self.show_page = Show_Page(self, self.database)
        self.select_page = Select_Page(self, self.database)
        self.about_page = About_Page(self)

        self.student = Student("DEMO", 1, 80, 90, 85)

        self.insert_button = self.add_nav_button("insert", self.show_insert_page)
        self.delete_button = self.add_nav_button("delete", self.show_delete_page)
        self.show_button = self.add_nav_button("show", self.show_show_page)
        self.select_button = self.add_nav_button("select", self.show_select_page)
        self.about_button = self.add_nav_button("about", self.show_about_page)

        self.insert_button.pack(side=LEFT, padx=5, pady=5)
        self.delete_button.pack(side=LEFT, padx=5, pady=5)
        self.show_button.pack(side=LEFT, padx=5, pady=5)
        self.select_button.pack(side=LEFT, padx=5, pady=5)
        self.about_button.pack(side=LEFT, padx=5, pady=5)

        self.show_show_page()

    def add_nav_button(self, text, command):
        button = ttk.Button(self.navbar, text=text, command=command, bootstyle=(OUTLINE, SECONDARY))
        return button

    def show_insert_page(self):
        self.hide_all_pages()
        self.insert_page.pack(fill=BOTH, expand=YES)
        self.insert_button.configure(bootstyle=SECONDARY)

    def show_delete_page(self):
        self.hide_all_pages()
        self.delete_page.pack(fill=BOTH, expand=YES)
        self.delete_button.configure(bootstyle=SECONDARY)

    def show_show_page(self):
        self.hide_all_pages()
        self.show_page.pack(fill=BOTH, expand=YES)
        self.show_button.configure(bootstyle=SECONDARY)

    def show_select_page(self):
        self.hide_all_pages()
        self.select_page.pack(fill=BOTH, expand=YES)
        self.select_button.configure(bootstyle=SECONDARY)

    def show_about_page(self):
        self.hide_all_pages()
        self.about_page.pack(fill=BOTH, expand=YES)
        self.about_button.configure(bootstyle=SECONDARY)

    def hide_all_pages(self):
        """隐藏所有页面"""
        for page in [self.insert_page, self.delete_page, self.show_page, self.select_page, self.about_page]:
            page.pack_forget()

        for button in [self.insert_button, self.delete_button, self.show_button, self.select_button, self.about_button]:
            button.configure(bootstyle=(OUTLINE, SECONDARY))


if __name__ == '__main__':
    function = ttk.Window(title="Function Demo", themename="darkly", resizable=(True, True), size=(1500, 1000))
    FunctionDemo(function)
    function.mainloop()
