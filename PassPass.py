import customtkinter as ctk

credit_font = ('Inter', 14, 'bold')
title_font = ('Inter', 24, 'bold')
common_text_font = ('Inter', 16)
elements_font = ('Inter', 18)
passpass_color_theme = '#1000FE'
passpass_text_color = 'black'
entrys_color = 'white'
passpass_icon_font = ('Inter', 40, 'bold')
passpass_bordercolor = 'black'

class PassPass:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("PassPass")
        self.root._set_appearance_mode('system')
        self.root.geometry('230x430')
        self.root.resizable(False, False)
        self.root.config(bg=passpass_color_theme)
        self.top = ctk.CTkFrame(self.root, fg_color=passpass_color_theme, bg_color=passpass_color_theme)
        self.top.pack(pady=10)

        credit = ctk.CTkLabel(self.top, text='Zac Milioli', font=credit_font, text_color=passpass_text_color, fg_color=passpass_color_theme, bg_color=passpass_color_theme)
        credit.pack(pady=2)

        title = ctk.CTkLabel(self.top, text='PassPass', font=title_font, text_color=passpass_text_color, fg_color=passpass_color_theme, bg_color=passpass_color_theme)
        title.pack(pady=2)

        # criar frame completo do PassPass e incluir o botão de ajuda
        self.mainscreen = ctk.CTkFrame(self.root, fg_color=passpass_color_theme, bg_color=passpass_color_theme)
        self.mainscreen.pack(fill='both', expand=True)

        self.entry1 = ctk.CTkEntry(self.mainscreen, placeholder_text='Entrada 1', placeholder_text_color=passpass_text_color, font=elements_font, fg_color=entrys_color, bg_color=passpass_color_theme, width=200, border_color=passpass_bordercolor)
        self.entry1.pack(pady=10)        
        self.entry2 = ctk.CTkEntry(self.mainscreen, placeholder_text='Entrada 2', placeholder_text_color=passpass_text_color, font=elements_font, fg_color=entrys_color, bg_color=passpass_color_theme, width=200, border_color=passpass_bordercolor)
        self.entry2.pack(pady=10)        
        self.entry3 = ctk.CTkEntry(self.mainscreen, placeholder_text='Entrada 3', placeholder_text_color=passpass_text_color, font=elements_font, fg_color=entrys_color, bg_color=passpass_color_theme, width=200, border_color=passpass_bordercolor)
        self.entry3.pack(pady=10)        

        self.generator = ctk.CTkButton(self.mainscreen, text='', fg_color=passpass_text_color, corner_radius=50, width=80, height=80, border_color=passpass_bordercolor)
        self.generator.pack(pady=20)

        self.button_icon = ctk.CTkLabel(self.mainscreen, text='🔒', font=title_font, text_color=entrys_color, fg_color=passpass_text_color, bg_color=passpass_text_color)
        self.button_icon.place(x=100, y=190)

        self.output = ctk.CTkEntry(self.mainscreen, placeholder_text='', font=elements_font, fg_color=entrys_color, bg_color=passpass_color_theme, width=200, border_color=passpass_bordercolor, state='disabled')
        self.output.pack(pady=2)
        self.copy_clipboard = ctk.CTkButton(self.mainscreen, text='📋', width=40, font=credit_font, text_color=entrys_color, fg_color=passpass_text_color, border_color=passpass_bordercolor)
        self.copy_clipboard.place(x=15, y=295)
        self.nsei = ctk.CTkButton(self.mainscreen, text='n sei ainda', width=155, font=credit_font, text_color=entrys_color, fg_color=passpass_text_color, border_color=passpass_bordercolor)
        self.nsei.place(x=60, y=295)
    
        # criar frame completo de ajuda e incluir o botão de voltar


    def switch_mainscreen(self):
        pass
        # self.mainscreen.pack_forget()

    def switch_helpscreen(self):
        pass
        # self.helpscreen.pack_forget()

if __name__ == "__main__":
    root = ctk.CTk()
    app = PassPass(root)
    root.mainloop()
