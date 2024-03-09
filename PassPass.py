import customtkinter as ctk

class PassPass:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("PassPass")
        self.root._set_appearance_mode('system')
        self.root.config(bg='#0000cd')
        self.wn = ctk.CTkFrame(self.root, bg_color='#0000cd', fg_color='#0000cd')
        self.wn.pack(fill='both', expand=True)

    def mainscreen(self):
        pass

    def helpscreen(self):
        pass

if __name__ == "__main__":
    root = ctk.CTk()
    app = PassPass(root)
    root.mainloop()
