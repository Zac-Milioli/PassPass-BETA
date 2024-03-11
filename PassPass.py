import customtkinter as ctk
import tkinter as tk

credit_font = ('Inter', 14, 'bold')
title_font = ('Inter', 24, 'bold')
common_text_font = ('Inter', 16)
elements_font = ('Inter', 20)
passpass_color_theme = '#1414b8'
primary = 'white'
secondary = 'black'
passpass_icon_font = ('Inter', 40, 'bold')

class PassPass:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("PassPass")
        self.root._set_appearance_mode('system')
        self.root.geometry('230x430')
        self.root.resizable(False, False)
        self.root.config(bg=passpass_color_theme)
        self.top = ctk.CTkFrame(self.root, fg_color=passpass_color_theme, bg_color=passpass_color_theme)
        self.top.pack(pady=10, fill='both')

        credit = ctk.CTkLabel(self.top, text='Zac Milioli', font=credit_font, text_color=primary, fg_color=passpass_color_theme, bg_color=passpass_color_theme)
        credit.pack(pady=2)

        title = ctk.CTkLabel(self.top, text='PassPass', font=title_font, text_color=primary, fg_color=passpass_color_theme, bg_color=passpass_color_theme)
        title.pack(pady=2)

        # criar frame completo do PassPass e incluir o botão de ajuda
        self.mainscreen = ctk.CTkFrame(self.root, fg_color=passpass_color_theme, bg_color=passpass_color_theme)
        self.mainscreen.pack(fill='both', expand=True)

        self.entry1 = ctk.CTkEntry(self.mainscreen, placeholder_text='Entrada 1', placeholder_text_color=primary, font=elements_font, fg_color=secondary, bg_color=passpass_color_theme, width=200, border_color=primary)
        self.entry1.pack(pady=10)        
        self.entry2 = ctk.CTkEntry(self.mainscreen, placeholder_text='Entrada 2', placeholder_text_color=primary, font=elements_font, fg_color=secondary, bg_color=passpass_color_theme, width=200, border_color=primary)
        self.entry2.pack(pady=10)        
        self.entry3 = ctk.CTkEntry(self.mainscreen, placeholder_text='Entrada 3', placeholder_text_color=primary, font=elements_font, fg_color=secondary, bg_color=passpass_color_theme, width=200, border_color=primary)
        self.entry3.pack(pady=10)        

        self.generator = ctk.CTkButton(self.mainscreen, text='🔒', font=passpass_icon_font, text_color=secondary, fg_color=primary, corner_radius=50, width=60, height=80, border_color=primary)
        self.generator.pack(pady=20)

        self.output = ctk.CTkEntry(self.mainscreen, placeholder_text='', text_color=primary, font=elements_font, fg_color=secondary, bg_color=passpass_color_theme, width=200, border_color=primary, state='disabled')
        self.output.pack(pady=2)

        self.copy_clipboard = ctk.CTkButton(self.mainscreen, text='📎', width=80, height=30, font=elements_font, text_color=secondary, fg_color=primary, border_color=primary, command=self.copy_to_clipboard)
        self.copy_clipboard.pack(pady=1)

        self.help_button = ctk.CTkButton(self.top, text='❔', width=0, font=elements_font, text_color=primary, fg_color=passpass_color_theme, border_color=passpass_color_theme, command=self.switch_helpscreen)
        self.help_button.place(relx=0.85, y=0)
        
        self.config_button = ctk.CTkButton(self.top, text='⚙️', width=0, font=elements_font, text_color=primary, fg_color=passpass_color_theme, border_color=passpass_color_theme, command=self.switch_configscreen)
        self.config_button.place(relx=0.01, y=3)

        self.back_button = ctk.CTkButton(self.top, text='↩️', width=0, font=elements_font, text_color=primary, fg_color=passpass_color_theme, border_color=passpass_color_theme, command=self.switch_mainscreen)

        # criar frame completo de ajuda



        # criar frame completo de config


    def switch_mainscreen(self):
        self.back_button.place_forget()
        self.mainscreen.pack(fill='both', expand=True)
        self.help_button.place(relx=0.85, y=0)
        self.config_button.place(relx=0.01, y=3)
        self.output.configure(state='normal')
        self.output.delete(0, 'end')
        self.output.configure(state='disabled')

    def switch_helpscreen(self):
        self.mainscreen.pack_forget()
        self.help_button.place_forget()
        self.config_button.place_forget()
        self.back_button.place(relx=0.01, y=3)

    def switch_configscreen(self):
        self.mainscreen.pack_forget()
        self.help_button.place_forget()
        self.config_button.place_forget()
        self.back_button.place(relx=0.01, y=3)

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.output.get())
        self.root.update()
        self.output.configure(state='normal')
        self.output.delete(0, 'end')
        self.output.insert(0, 'Salva no clipboard!')
        self.output.configure(state='disabled')

    def generate_password(self):
        pass

if __name__ == "__main__":
    root = ctk.CTk()
    app = PassPass(root)
    root.mainloop()
