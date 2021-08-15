import tkinter as tk
from tkinter import messagebox


class Security:
    def __init__(self, algorimth: str = "cesar") -> None:
        """Aplica el cifrado {'cesar', 'vigenere'} utilizando el alfabeto español

        :params
            algorimth: str, default='cesar'
                Algoritmo a utilizar, soporte ['cesar', 'vigenere']
        """

        self.algorimth = algorimth
        self.__alphabet = "abcdefghijklmnopqrstuvwxyz"  # --> add 'enie'

    def encode(self, text: str = None, key: str = None) -> str:
        """Realiza la codificación {'cesar', 'vigenere'} a partir del texto y llave ingresada.

        :params
            text: srt, default=None
                texto plano a codificar
            key: str, default=None
                valor de desplazamiento para cifrado 'cesar' ó palabra clave para 'vigenere'

        :returns
            encrypted:str
                devuelve el texto codificado de acuerdo al algoritmo seleccionado
        """

        self.text = text.lower()

        if self.algorimth == "cesar":
            self.key = [int(x) for x in key]
        elif self.algorimth == "vigenere":
            self.key = key.lower()
            self.key = [self.__alphabet.find(x) for x in self.key]
        else:
            raise ValueError("Cipher Algorimth not supported")

        encrypted = ""
        i = 0

        for char in self.text:

            if char in self.__alphabet:
                char_index = self.__alphabet.find(char)
                new_char_index = char_index + self.key[i]

                if new_char_index > len(self.__alphabet) - 1:
                    new_char_index = new_char_index - len(self.__alphabet)

                new_char = self.__alphabet[new_char_index]
                encrypted += new_char
                i += 1
            else:
                encrypted += char

            if i >= len(self.key):
                i = 0

        return encrypted

    def decode(self, text: str, key: str) -> str:
        """Realiza la decodificación {'cesar', 'vigenere'} a partir del texto y llave ingresada.

        :params
            text: srt, default=None
                texto codificado
            key: str, default=None
                valor de desplazamiento para cifrado 'cesar' ó palabra clave para 'vigenere'

        :returns
            decrypted:str
                devuelve el texto decodificado de acuerdo al algoritmo seleccionado
        """

        self.text = text.lower()

        if self.algorimth == "cesar":
            self.key = [int(x) for x in key]
        elif self.algorimth == "vigenere":
            self.key = key.lower()
            self.key = [self.__alphabet.find(x) for x in self.key]
        else:
            raise ValueError("Cipher Algorimth not supported")

        decrypted = ""
        i = 0

        for char in self.text:

            if char in self.__alphabet:
                char_index = self.__alphabet.find(char)
                new_char_index = char_index - self.key[i]

                if new_char_index < 0:
                    new_char_index = new_char_index + len(self.__alphabet)

                new_char = self.__alphabet[new_char_index]
                decrypted += new_char
                i += 1
            else:
                decrypted += char

            if i >= len(self.key):
                i = 0

        return decrypted


class App(tk.Frame):
    def __init__(self, master: object) -> None:
        """Clase para la interfaz gráfica de usuario."""

        super().__init__(master)
        self.master = master
        self.master.geometry("800x300")
        self.master.title("Cifrador y Desifrador")
        self.master.resizable(False, False)
        self.add_widgets()

        self.algorimth = ""
        self.select_cesar()

    def add_widgets(self) -> None:
        """Constructor de los widget utilizados en la GUI"""

        self.DARK = "#222222"
        self.LIGHT = "#f0f0f0"
        self.RED = "#e03c31"

        main_frame = tk.Frame(self.master, background=self.DARK)
        main_frame.place(x=0, y=0, width=800, height=300)

        title_lbl = tk.Label(
            main_frame,
            background=self.DARK,
            foreground=self.LIGHT,
            text="CIFRADO CÉSAR & VIGENERE",
            font=("Arial", 20),
        )
        title_lbl.place(x=150, y=20, width=500, height=30)

        self.input_text = tk.Text(
            main_frame,
            background=self.LIGHT,
            foreground=self.DARK,
            font=("Arial", 11),
            padx=4,
            pady=4,
        )
        self.input_text.place(x=50, y=75, width=300, height=90)

        key_lbl = tk.Label(
            main_frame,
            background=self.DARK,
            foreground=self.LIGHT,
            text="Clave:",
            font=("Arial", 12),
        )
        key_lbl.place(x=50, y=175, width=75, height=30)

        self.key_text = tk.Text(
            main_frame,
            background=self.LIGHT,
            foreground=self.DARK,
            font=("Arial", 11),
            padx=4,
            pady=4,
        )
        self.key_text.place(x=125, y=175, width=225, height=30)

        self.output_text = tk.Text(
            main_frame,
            background=self.LIGHT,
            foreground=self.DARK,
            font=("Arial", 11),
            padx=4,
            pady=4,
            state="disable",
        )
        self.output_text.place(x=450, y=75, width=300, height=90)

        encode_btn = tk.Button(
            main_frame,
            text="Cifrar",
            background=self.LIGHT,
            activebackground=self.LIGHT,
            foreground=self.DARK,
            activeforeground=self.DARK,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Arial", 15),
            command=self.encode_btn_fun,
        )
        encode_btn.place(x=125, y=240, width=150, height=40)

        decode_btn = tk.Button(
            main_frame,
            text="Decifrar",
            background=self.LIGHT,
            activebackground=self.LIGHT,
            foreground=self.DARK,
            activeforeground=self.DARK,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Arial", 15),
            command=self.decode_btn_fun,
        )
        decode_btn.place(x=325, y=240, width=150, height=40)

        exit_btn = tk.Button(
            main_frame,
            text="Salir",
            background=self.RED,
            activebackground=self.RED,
            foreground=self.LIGHT,
            activeforeground=self.LIGHT,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Arial", 15),
            command=self.master.destroy,
        )
        exit_btn.place(x=525, y=240, width=150, height=40)

        second_frame = tk.Frame(main_frame, background=self.LIGHT)
        second_frame.place(x=450, y=175, width=300, height=30)

        self.opt_1 = tk.Button(
            second_frame,
            text="Cesar",
            foreground=self.LIGHT,
            activeforeground=self.LIGHT,
            background=self.DARK,
            activebackground=self.DARK,
            relief="flat",
            borderwidth=0,
            font=("Arial", 12),
            command=self.select_cesar,
        )
        self.opt_1.place(x=1, y=1, width=148, height=28)

        self.opt_2 = tk.Button(
            second_frame,
            text="Vigenere",
            foreground=self.LIGHT,
            activeforeground=self.LIGHT,
            background=self.DARK,
            activebackground=self.DARK,
            relief="flat",
            borderwidth=0,
            font=("Arial", 12),
            command=self.select_vigenere,
        )
        self.opt_2.place(x=151, y=1, width=148, height=28)

    def encode_btn_fun(self) -> None:
        """Función a ejecutar para la acción de codificación."""

        method = self.algorimth
        input_txt = self.input_text.get("1.0", "end-1c")
        input_key = self.key_text.get("1.0", "end-1c")

        cipher = Security(method)

        try:
            output_txt = cipher.encode(input_txt, input_key)
        except ValueError as err:
            output_txt = ""
            messagebox.showerror(
                message=f"Clave inválida para cifrado César: {err}",
                title="Valor inválido",
            )

        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", output_txt)
        self.output_text.config(state="disable")

    def decode_btn_fun(self) -> None:
        """Función a ejecutar para la acción de decodificación."""

        method = self.algorimth
        input_txt = self.input_text.get("1.0", "end-1c")
        input_key = self.key_text.get("1.0", "end-1c")

        cipher = Security(method)

        try:
            output_txt = cipher.decode(input_txt, input_key)
        except ValueError as err:
            output_txt = ""
            messagebox.showerror(
                message=f"Clave inválida para cifrado César: {err}",
                title="Valor inválido",
            )

        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", output_txt)
        self.output_text.config(state="disable")

    def select_cesar(self) -> None:
        """Permite seleccionar el algoritmo de cifrado 'cesar'."""

        self.algorimth = "cesar"

        self.opt_1.config(
            foreground=self.DARK,
            activeforeground=self.DARK,
            background=self.LIGHT,
            activebackground=self.LIGHT,
        )

        self.opt_2.config(
            foreground=self.LIGHT,
            activeforeground=self.LIGHT,
            background=self.DARK,
            activebackground=self.DARK,
        )

    def select_vigenere(self) -> None:
        """Permite seleccionar el algoritmo de cifrado 'vigenere'."""

        self.algorimth = "vigenere"

        self.opt_2.config(
            foreground=self.DARK,
            activeforeground=self.DARK,
            background=self.LIGHT,
            activebackground=self.LIGHT,
        )

        self.opt_1.config(
            foreground=self.LIGHT,
            activeforeground=self.LIGHT,
            background=self.DARK,
            activebackground=self.DARK,
        )


def main() -> None:
    root = tk.Tk()
    app = App(root)
    app.mainloop()


if __name__ == "__main__":
    main()
