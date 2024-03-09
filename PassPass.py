import customtkinter as ctk

credit_font = ('Inter', 14, 'bold')
title_font = ('Inter', 24, 'bold')
common_text_font = ('Inter', 16)
elements_font = ('Inter', 18)
passpass_color_theme = '#00F6FF'


class PassPass:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("PassPass")
        self.root._set_appearance_mode('system')
        self.root.geometry('230x430')
        self.root.config(bg=passpass_color_theme)
        self.wn = ctk.CTkFrame(self.root, bg_color=passpass_color_theme, fg_color=passpass_color_theme)
        self.wn.pack(fill='both', expand=True)

        credit = ctk.CTkLabel(self.wn, text='Zac Milioli', font=credit_font, text_color='black', fg_color='transparent')
        credit.pack(padx=5, pady=5)

        title = ctk.CTkLabel(self.wn, text='PassPass', font=title_font, text_color='black', fg_color='transparent')
        title.pack(padx=5, pady=3)

    def mainscreen(self):
        pass

    def helpscreen(self):
        pass

if __name__ == "__main__":
    root = ctk.CTk()
    app = PassPass(root)
    root.mainloop()
