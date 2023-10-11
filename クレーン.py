import tkinter as tk
from tkinter import messagebox

def open_next_screen(screen_title, text_var):
    next_window = tk.Toplevel(root)
    next_window.title(screen_title)

    def change_text():
        new_text = input_field.get()
        text_var.set(new_text)
        next_window.destroy()  # 次ウィンドウを閉じる

    input_field = tk.Entry(next_window, font=("Helvetica", 20))
    input_field.pack()

    change_button = tk.Button(next_window, text="テキストを変更", command=change_text)
    change_button.pack()

def open_next_screen1():
    open_next_screen("機器番号", shared_text1)

def open_next_screen2():
    open_next_screen("モード", shared_text2)

def open_next_screen3():
    open_next_screen("運転手コード", shared_text3)

def show_confirmation_dialog():
    result = messagebox.askquestion("確認", "この内容でよろしいですか？")
    if result == "yes":
        print("Yes ボタンが押されました")
    elif result == "no":
        print("No ボタンが押されました")

def register():
    if not shared_text1.get() or not shared_text2.get() or not shared_text3.get():
        messagebox.showerror("エラー", "全てのテキストを入力してください。")
    else:
        show_confirmation_dialog()

root = tk.Tk()
root.title("クレーン画面操作システム")

equipment_number_label = tk.Label(root, text="機器番号", font=("Helvetica", 20))
equipment_number_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

mode_label = tk.Label(root, text="モード", font=("Helvetica", 20))
mode_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")

driver_code_label = tk.Label(root, text="運転手コード", font=("Helvetica", 20))
driver_code_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")

shared_text1 = tk.StringVar()
shared_text2 = tk.StringVar()
shared_text3 = tk.StringVar()

text_label1 = tk.Label(root, textvariable=shared_text1, font=("Helvetica", 20), relief="ridge")
text_label1.grid(row=1, column=1, padx=20, pady=20)

text_label2 = tk.Label(root, textvariable=shared_text2, font=("Helvetica", 20), relief="ridge")
text_label2.grid(row=2, column=1, padx=20, pady=20)

text_label3 = tk.Label(root, textvariable=shared_text3, font=("Helvetica", 20), relief="ridge")
text_label3.grid(row=3, column=1, padx=20, pady=20)

register_button = tk.Button(root, text="登録", width=20, height=3, command=register)
register_button.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

text_label1.bind("<Button-1>", lambda event, text_var=shared_text1: open_next_screen1())
text_label2.bind("<Button-1>", lambda event, text_var=shared_text2: open_next_screen2())
text_label3.bind("<Button-1>", lambda event, text_var=shared_text3: open_next_screen3())

window_width = 400
window_height = 350
root.geometry(f"{window_width}x{window_height}")

root.mainloop()
