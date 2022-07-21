import tkinter as tk
from tkinter import Button, ttk


class View(tk.Tk):

    PAD = 10
    button_search = "Start scraping data"
    button_getting_data = "Getting data from google maps database..."

    def __init__(self,controller):
        super().__init__()#initialize object which we are inherit from
        self.controller = controller
        self.title('ScrapeData 1.0')
        self.string_search = tk.StringVar()
        self._make_main_frame()
        self._make_entry()
        self._make_button()

    def main(self):
        self.mainloop()
        #after this line no code will be executed
    

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)


    def _make_entry(self):
        entr = ttk.Entry(self.main_frm, justify='center',textvariable=self.string_search, width=50)
        entr.pack(side='left')
    


    def _make_button(self):
        frm = ttk.Frame(self.main_frm,)
        frm.pack(side='right')
        btn = ttk.Button(frm, text=self.button_search, command=(
                lambda : self.controller.on_button_click()
                #lambda text = self.entr.get() : self.controller.on_button_click(text)
            )
        )
        btn.pack(side='right')
    