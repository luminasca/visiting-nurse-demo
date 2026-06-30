from core.views.main_window import MainWindow


class App:
    def __init__(self) -> None:
        self.window = MainWindow()

    def run(self) -> None:
        self.window.mainloop()
