import os
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
from lfsr_generator import LFSR
from sg_generator import SG


class Input_error(Exception):
    pass


def print_error(error):
    """ Выводит описание ошибки """
    mb.showerror("Ошибка", error)


def print_result(text_result: tk.Text, label_T: tk.Label, label_pirson: tk.Label, sequence: list[int], period: int, pirson: str):
    """ Выводит результаты генерации псевдослучайной последовательности """
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, "".join(str(i) for i in sequence))
    label_T["text"] = "Период: " + str(period)
    label_pirson["text"] = "Критерий Пирсона: " + pirson


def save_result(sequence: list[int], period: int, pirson: str):
    """ Сохраняет результаты генерации псевдослучайной последовательности """
    file_result = "result.txt"
    with open(file_result, "w", encoding="utf-8") as file_out:
        print("Сгенерированная последовательность: ", "".join(str(i) for i in sequence), file=file_out)
        print("Период: ", period, file=file_out)
        print("Критерий Пирсона: ", pirson, file=file_out)
    msg = f"Результаты генератора сохранены в файл: {file_result}. Открыть файл {file_result}?"
    if mb.askyesno("Открыть файл", msg):
        os.startfile(file_result)


def load_polynomials(filename: str) -> list[int]:
    """ Загружает и возвращает полиномы из файла """
    polynomials = []
    with open(filename, "r", encoding="utf-8") as file_in:
        polynomials = file_in.read().split()
    return polynomials


def get_polynomials(combobox_polynomial_1: ttk.Combobox, combobox_polynomial_2: ttk.Combobox) -> tuple[list[int], list[int]]:
    """ Считывает выбранные полиномы из выпадающего списка """
    polynomial_1 = [int(i) for i in combobox_polynomial_1.get()]
    polynomial_2 = [int(i) for i in combobox_polynomial_2.get()]
    if len(polynomial_1) == 0:
        raise Input_error("Заполните поле 'Полином 1'")
    elif len(polynomial_2) == 0:
        raise Input_error("Заполните поле 'Полином 2'")
    elif (len(polynomial_1) == len(polynomial_2)):
        raise Input_error("Степени полиномов должны быть взаимно-простыми")
    return polynomial_1, polynomial_2


def generate_sequence(combobox_polynomial_1: ttk.Combobox, combobox_polynomial_2: ttk.Combobox, text_result: tk.Text, label_T: tk.Label, label_pirson: tk.Label):
    """ Обрабатывает кнопку генерации псевдослучайной последовательности """
    try:
        polynomial_1, polynomial_2 = get_polynomials(combobox_polynomial_1, combobox_polynomial_2)
        G1 = LFSR(polynomial_1)
        G2 = LFSR(polynomial_2)
        G = SG(G1, G2)
        sequence = G.generate()
        period = G.calc_period()
        pirson = G.check_pirson(sequence)
        print_result(text_result, label_T, label_pirson, sequence, period, pirson)
        save_result(sequence, period, pirson)
    except Input_error as e:
        print_error(e)


def  create_app():
    """ Создает окно приложения """
    root = tk.Tk()
    root.title("Генерирование РРСП")
    root.geometry("400x350+200+100")
    root.resizable(False, False)
    polynomials = load_polynomials("polynomials.txt")

    label_state_1 = tk.Label(text="Полином 1: ", font=("Arial", 10))
    label_state_1.grid(row=0, column=0, stick="w", padx=20, pady=10)
    combobox_polynomial_1 = ttk.Combobox(values=polynomials, width=55, state="readonly")
    combobox_polynomial_1.grid(row=1, column=0, stick="w", padx=20)
    label_state_2 = tk.Label(text="Полином 2: ", font=("Arial", 10))
    label_state_2.grid(row=2, column=0, stick="w", padx=20, pady=10)
    combobox_polynomial_2 = ttk.Combobox(values=polynomials, width=55, state="readonly")
    combobox_polynomial_2.grid(row=3, column=0, stick="w", padx=20)
    label_result = tk.Label(text="Результат: ", font=("Arial", 10))
    label_result.grid(row=4, column=0, stick="w", padx=20, pady=10)
    text_result = tk.Text(width=50, height=3, font=("Arial", 10), wrap="char")
    text_result.grid(row=5, column=0, stick="w", padx=20)
    label_T = tk.Label(text="Период (T): ", font="Arial 10 italic")
    label_T.grid(row=6, column=0, stick="w", padx=20, pady=10)
    label_pirson = tk.Label(text="Критерий Пирсона: ", font="Arial 10 italic")
    label_pirson.grid(row=7, column=0, stick="w", padx=20)
    button_generate = tk.Button(text="Сгенерировать", width=20, font=("Arial", 10), activebackground="#00CED1", background="#FFFFFF",
                                command=lambda: generate_sequence(combobox_polynomial_1, combobox_polynomial_2, text_result, label_T, label_pirson))
    button_generate.grid(row=8, column=0, stick="we", padx=20, pady=10)
    
    root.mainloop()