import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from function import FunctionDemo
from db import Database
from ttkbootstrap.dialogs.dialogs import Messagebox


class MianWindow(ttk.Window):
    def __init__(self):
        super().__init__("APP", "darkly", resizable=(True, True))
        self.title("app demo")

        self.login = DataEntryForm(self)
        self.login.pack(fill=BOTH, expand=YES)


class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        # form variables
        self.root = master
        self.name = ttk.StringVar(value="")
        self.password = ttk.StringVar(value="")

        self.db = Database()

        self.login_flag = False

        # form header
        hdr_txt = "Please enter your contact information"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("name", self.name)
        self.create_form_entry("password", self.password)
        self.create_buttonbox()

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        if label == "password":
            ent = ttk.Entry(master=container, textvariable=variable, show="*")
        else:
            ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)


    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()  # set focus to submit button

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        print("Name:", self.name.get())
        print("Address:", self.password.get())

        self.login_flag = self.db.login_check(self.name.get(), self.password.get())
        if self.login_flag:
            print("Login Success")
            self.db.conn.close()
            self.pack_forget()
            FunctionDemo(self.root)
        else:
            Messagebox.show_error("Login Failed", "Invalid username or password")
            self.name.set("")  # clear the entry fields
            self.password.set("")  # clear the entry fields

    def on_cancel(self):
        self.quit()


if __name__ == "__main__":
    app = MianWindow()
    app.mainloop()
