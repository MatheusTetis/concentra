import tkinter as tk
from tkinter import ttk
import datetime


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("350x500")
        self.configure(background='#1C0C5B')
        self.title('Hora da Concentração')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.foco_inicial = 1800
        self.dispersao_inicial = 600
        self.dispersar = False

        self.create_widgets()

        self.countdown(remaining=self.foco_inicial)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if not self.dispersar:
            if self.remaining <= 0:
                self.mensagem.configure(text='Hora de dispersar')
                self.canvas.itemconfigure(self.cronometro, text=f"{str(datetime.timedelta(seconds=self.remaining))[-5:]}")
                self.attributes('-topmost', 1)
                self.attributes('-topmost', 0)
                self.remaining = self.dispersao_inicial
                self.dispersar = True
                self.after(1000, self.countdown)

            else:
                self.canvas.itemconfigure(self.cronometro, text=f"{str(datetime.timedelta(seconds=self.remaining))[-5:]}")
                self.remaining = self.remaining - 1
                self.after(1000, self.countdown)

        else:
            if self.remaining <= 0:
                self.mensagem.configure(text='Hora de focar')
                self.canvas.itemconfigure(self.cronometro, text=f"{str(datetime.timedelta(seconds=self.remaining))[-5:]}")
                self.attributes('-topmost', 1)
                self.attributes('-topmost', 0)
                self.remaining = self.foco_inicial
                self.dispersar = False
                self.after(1000, self.countdown)

            else:
                self.canvas.itemconfigure(self.cronometro, text=f"{str(datetime.timedelta(seconds=self.remaining))[-5:]}")
                self.remaining = self.remaining - 1
                self.after(1000, self.countdown)

    def create_widgets(self):
        # reloogio
        self.canvas = tk.Canvas(self, bg='#1C0C5B', height=300, highlightthickness=0)
        x = 350/2
        y = 150
        r = 100
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="#3D2C8D", outline="")
        self.cronometro = self.canvas.create_text((x, y), font=('Arial', 40, 'bold'), text="0:00:00", fill="#C996CC")
        self.canvas.grid(column=0, row=0, columnspan=4)

        # mensagem - caixa de texto
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="#C996CC", background='#1C0C5B', font=('Arial', 11), anchor="center")

        self.mensagem = ttk.Label(text="Hora de focar", style="BW.TLabel")
        self.mensagem.grid(column=0, row=1, sticky=tk.NSEW, padx=10, pady=10)

        # quit button
        quit_button = tk.Button(self, text="Sair")
        quit_button.configure(bg='#1C0C5B', command=self.sair, fg="#C996CC", borderwidth=0, font=('Arial', 11))
        quit_button.bind("<Enter>", lambda e: quit_button.configure(bg="#3D2C8D"))
        quit_button.bind("<Leave>", lambda e: quit_button.configure(bg='#1C0C5B'))
        quit_button.grid(column=0, row=2, sticky=tk.NSEW, padx=10, pady=10)

    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

    def sair(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()