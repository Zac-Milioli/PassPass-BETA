import customtkinter as ctk
from hashlib import sha512

my_font = 'Inter'
credit_font = (my_font, 14, 'bold')
title_font = (my_font, 24, 'bold')
passpass_icon_font = (my_font, 40, 'bold')
common_text_font = (my_font, 16)
elements_font = (my_font, 20)
passpass_color_theme = '#1414b8'
primary = 'white'
secondary = 'black'

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

        self.entry1 = ctk.CTkEntry(self.mainscreen, placeholder_text='Entrada 1', placeholder_text_color=primary, font=elements_font, fg_color=secondary, bg_color=passpass_color_theme, width=200, border_color=primary, text_color=primary)
        self.entry1.pack(pady=10)        
        self.entry2 = ctk.CTkEntry(self.mainscreen, placeholder_text='Entrada 2', placeholder_text_color=primary, font=elements_font, fg_color=secondary, bg_color=passpass_color_theme, width=200, border_color=primary, text_color=primary)
        self.entry2.pack(pady=10)        
        self.entry3 = ctk.CTkEntry(self.mainscreen, placeholder_text='Entrada 3', placeholder_text_color=primary, font=elements_font, fg_color=secondary, bg_color=passpass_color_theme, width=200, border_color=primary, text_color=primary)
        self.entry3.pack(pady=10)        

        self.generator = ctk.CTkButton(self.mainscreen, text='🔒', font=passpass_icon_font, text_color=secondary, fg_color=primary, corner_radius=50, width=60, height=80, border_color=primary, command=self.generate_password)
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
        self.helpscreen = ctk.CTkFrame(self.root, fg_color=passpass_color_theme, corner_radius=0)

        # criar frame completo de config
        self.configscreen = ctk.CTkFrame(self.root, fg_color=passpass_color_theme, corner_radius=0)


    def switch_mainscreen(self):
        self.helpscreen.pack_forget()
        self.configscreen.pack_forget()
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
        self.helpscreen.pack(fill='both', expand=True)

    def switch_configscreen(self):
        self.mainscreen.pack_forget()
        self.help_button.place_forget()
        self.config_button.place_forget()
        self.back_button.place(relx=0.01, y=3)
        self.configscreen.pack(fill='both', expand=True)

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.output.get())
        self.root.update()
        self.output.configure(state='normal')
        if self.output.get() != '':
            self.output.delete(0, 'end')
            self.output.insert(0, 'Salva no clipboard!')
        else:
            self.output.insert(0, 'Nada para copiar')
        self.output.configure(state='disabled')

    def generate_password(self):
        gen = {
            'primeiro': self.entry1.get().encode('latin-1'),
            'segundo': self.entry2.get().encode('latin-1'),
            'terceiro': self.entry3.get().encode('latin-1'),
            'salt': b'=R7Q9ju:xT>=!C\?wWB:pjgc{[!{yGAG{SgLqb|rV:zjt4kJFk/a6fRyv?6B{N@on,?]6!cfv\93caM51}Pg9`0g]$oW}frs6[csGp=6&3v?TXzi8Il}J.(1^Oh-oEz+n56|&oR4=tnD"<x!AZ!y!.Gl{YmS=}=v8*6`6D`nK/5O@&,<&9',
            'special': '!@#$%¨&*(),.:;/?]}[{+_-=*<>',
            'letters': 'ABCDEFGHIJKLMMNOPRSTUVWXYZ'
        }

        gen['combination'] = f'{gen["primeiro"]}{gen["segundo"]}{gen["terceiro"]}'.encode('latin-1')
        gen['combination_salted'] = f'{gen["salt"]}{gen["combination"]}{gen["salt"]}'.encode('latin-1')
        gen['first_step'] = sha512(sha512(gen['combination_salted']).hexdigest().encode('latin-1')).hexdigest().encode('latin-1')
        gen['second_step'] = f"{sha512(gen['primeiro']).hexdigest()}{sha512(gen['segundo']).hexdigest()}{sha512(gen['terceiro']).hexdigest()}{sha512(gen['combination_salted']).hexdigest()}".encode('latin-1')
        gen['third_step'] = f"{sha512(gen['combination_salted']).hexdigest()}".encode('latin-1')
        gen['forth_step'] = f"{sha512(gen['second_step']).hexdigest()}{sha512(gen['third_step']).hexdigest()}".encode('latin-1')
        gen['fifth_step'] = f"{sha512(gen['forth_step']).hexdigest()}".encode('latin-1')
        gen['sixth_step'] = f"{sha512(gen['fifth_step']).hexdigest()}{sha512(gen['fifth_step']).hexdigest()}".encode('latin-1')
        gen['seventh_step'] = sha512(gen['sixth_step']).hexdigest()
        gen['eighth_step'] = gen['seventh_step'][::18]
        specpos1 = len(gen["primeiro"])
        specpos2 = len(gen["segundo"])
        specpos3 = len(gen["terceiro"])
        letpos1 = len(gen["primeiro"])
        letpos2 = len(gen["segundo"])
        letpos3 = len(gen["terceiro"])
        if specpos1 > 27:
            while specpos1 > 27:
                specpos1 -= 27
        if specpos2 > 27:
            while specpos2 > 27:
                po2 -= 27
        if specpos3 > 27:
            while specpos3 > 27:
                specpos3 -= 27
        if letpos1 > 26:
            while letpos1 > 26:
                letpos1 -= 26
        if letpos2 > 26:
            while letpos2 > 26:
                letpos2 -= 26
        if letpos3 > 26:
            while letpos3 > 26:
                letpos3 -= 26
        special1 = gen['special'][specpos1]
        special2 = gen['special'][specpos2]
        special3 = gen['special'][specpos3]
        letter1 = gen['letters'][letpos1]
        letter2 = gen['letters'][letpos2]
        letter3 = gen['letters'][letpos3]
        if specpos1 >= 9:
            while specpos1 >= 9:
                specpos1 -= 9
        if specpos2 >= 9:
            while specpos2 >= 9:
                po2 -= 9
        if specpos3 >= 9:
            while specpos3 >= 9:
                specpos3 -= 9
        if letpos1 >= 12:
            while letpos1 >= 12:
                letpos1 -= 12
        if letpos2 >= 12:
            while letpos2 >= 12:
                letpos2 -= 12
        if letpos3 >= 12:
            while letpos3 >= 12:
                letpos3 -= 12
        gen['last_step'] = f'{gen["eighth_step"][0:specpos1]}{special1}{gen["eighth_step"][specpos1:specpos2]}{special2}{gen["eighth_step"][specpos2:specpos3]}{special3}{gen["eighth_step"][specpos3:]}'
        gen['last_step'] = f'{gen["last_step"][0:letpos1]}{letter1}{gen["last_step"][letpos1:letpos2]}{letter2}{gen["last_step"][letpos2:letpos3]}{letter3}{gen["last_step"][letpos3:]}'
        
        self.output.configure(state='normal')
        self.output.delete(0, 'end')
        self.output.insert(0, gen['last_step'])
        self.output.configure(state='disabled')
        gen = None

if __name__ == "__main__":
    root = ctk.CTk()
    app = PassPass(root)
    root.mainloop()
