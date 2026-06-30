import customtkinter as ctk


class MainWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("訪問看護記録票作成デモ")
        self.geometry("900x600")

        label = ctk.CTkLabel(self, text="訪問看護記録票作成デモ")
        label.pack(pady=20)
