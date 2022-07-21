
from typing_extensions import Self
from model import Model
from view import View
import asyncio

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)


    def main(self):
        self.view.main()
        self.model.main()

    def on_button_click(self):
        print(f'typed {self.view.string_search.get()} sentence')
        #task = asyncio.create_task(self.start_search(self.view.string_search.get()))
        task = asyncio.create_task(self.model.search(self.view.string_search.get()))
        # print("cos mozna")
        result = self.model.search(self.view.string_search.get())
        if result:
            print("Data collected")
            self.view.quit
        else:
            print("Failure")
        self.view.string_search.set("")

    async def start_search(self, text):
        await self.model.search(text)


if __name__ == '__main__':
    websscraper = Controller()
    websscraper.main()