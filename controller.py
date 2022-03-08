
from typing_extensions import Self
from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)


    def main(self):
        self.view.main()
        self.model.main()

    def on_button_click(self):
        print(f'typed {self.view.string_search.get()} sentence')
        result = self.model.search(self.view.string_search.get())
        if result:
            print("Data collected")
        else:
            print("Failure")
        self.view.string_search.set("")

if __name__ == '__main__':
    websscraper = Controller()
    websscraper.main()