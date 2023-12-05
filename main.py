import tkinter as tk
from PIL import Image, ImageTk
def press_button():
    print('Botão pressionado')
    p = entry1.get()
    s = entry2.get()
    t = entry3.get()
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    saida.delete(0, 'end')
    saida.insert(0, f'{p}{s}{t}')
background_color = 'blue'
text_color = 'black'
font = ('Arial', 15)
padding_y = 30
window = tk.Tk()
window.configure(bg=background_color)
window.geometry('400x600')
entry1 = tk.Entry(window, bg='white', fg=text_color, font=font)
entry2 = tk.Entry(window, bg='white', fg=text_color, font=font)
entry3 = tk.Entry(window, bg='white', fg=text_color, font=font)
entry1.pack(pady=padding_y)
entry2.pack(pady=padding_y)
entry3.pack(pady=padding_y)
image = Image.open("lock.png")
resize_image = image.resize((150, 150))
imagem_file = ImageTk.PhotoImage(resize_image, master=window)
image = tk.Button(image=imagem_file, master=window, bg=background_color, command=press_button)
image.pack(pady=padding_y)
saida = tk.Entry(window, bg='white', fg=text_color, font=font)
saida.pack(pady=padding_y)
window.mainloop()