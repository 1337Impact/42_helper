#!/usr/bin/env python
import tkinter
from multiprocessing import Process
import customtkinter
from watch_my_post import post_watcher

class my_app(customtkinter.CTk):
    def __init__(self):
        self.check_var = "off"
        self.process = 0
        self.li_pos = .2
        self.li_list = []
        self.data = []
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.app = customtkinter.CTk()
        self.app.geometry("550x400")
        self.app.title("WatchMyPost")
        self.set_up_gui()
        self.app.mainloop()
        self.kill_watcher()

    def add_to_watch(self):
        self.clear_list()
        text = self.entry.get()
        self.entry.delete(0, 'end')
        self.data = text.split(" ")
        self.add_posts_to_list(self.data)
        self.async_post_watcher(self.data, self.check_var)

    def message_service(self):
        self.check_var = "on" if self.check_var == "off" else "off"
        print("messaging is now: " + self.check_var)

    def set_up_gui(self):
        # frames
        self.input_f = customtkinter.CTkFrame(master=self.app, height=120)
        self.input_f.pack(pady=10, padx=60, fill="both", expand=True)

        self.list_f = customtkinter.CTkFrame(master=self.app)
        self.list_f.pack(pady=10, padx=60, fill="both", expand=True)

        #post input
        self.entry = customtkinter.CTkEntry(master=self.input_f, width=250, height=50,  placeholder_text="Enter Post to watch Ex: e2r13p1")
        self.entry.place(relx=.35, rely=0.5, anchor=tkinter.CENTER)

        #submit button
        self.s_button = customtkinter.CTkButton(master=self.input_f, width=100, height=50, hover_color="#1f538d",  text="watch", command=self.add_to_watch)
        self.s_button.place(relx=.8, rely=0.5, anchor=tkinter.CENTER)

        #send mgs checkbox
        self.msg_checkbox = customtkinter.CTkCheckBox(master=self.input_f, width=50, height=10, text="send msg", command=self.message_service, onvalue="on", offvalue="off")
        self.msg_checkbox.place(relx=.15, rely=0.95, anchor=tkinter.S)

        # list lable
        self.ul_lable = customtkinter.CTkLabel(master=self.list_f, width=100, height=50, font=("Times bold", 20), text="List Of Watched Posts:")
        self.ul_lable.place(relx=.05, rely=0, anchor=tkinter.NW)

        #reset button
        self.r_button = customtkinter.CTkButton(master=self.list_f, width=60, height=30, fg_color="#9c332c", hover_color="#782620",  text="reset", command=self.reset_watcher)
        self.r_button.place(relx=.95, rely=.95, anchor=tkinter.SE)
    
    def add_posts_to_list(self, posts):
        for post in posts:
            self.li_lable = customtkinter.CTkLabel(master=self.list_f, width=100, height=20, font=("Times bold", 16), text=post)
            self.li_lable.place(relx=.05, rely=self.li_pos, anchor=tkinter.NW)
            self.li_list.append(self.li_lable)
            self.li_pos += .1
    
    def clear_list(self):
        for li in self.li_list:
            li.destroy()
        self.li_pos = .2
        self.li_list = []
        self.data = []

    def reset_watcher(self):
        self.clear_list()
        self.kill_watcher()


    def async_post_watcher(self, data, msg):
        self.kill_watcher()
        self.process = Process(target=post_watcher, args=[data, msg])
        self.process.start()

    def kill_watcher(self):
        if self.process:
            print("terminate")
            self.process.terminate()


if __name__ == '__main__':
    obj = my_app()