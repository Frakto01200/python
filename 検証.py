import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def open_next_screen(screen_title, text_var):
    next_window = tk.Toplevel(root)
    next_window.title(screen_title)

    frame = tk.Frame(next_window, borderwidth=5, relief="ridge", padx=20, pady=20)
    frame.pack(padx=20, pady=20)

    def change_text():
        # フィールドからテキストを取得して共有変数を更新
        new_text = input_field.get()
        text_var.set(new_text)
        next_window.destroy()  # 次ウィンドウを閉じる

    # テキストを入力するためのフィールド
    input_field = tk.Entry(frame, font=("Helvetica", 20))
    input_field.pack()

    change_button = tk.Button(frame, text="テキストを変更", command=change_text)
    change_button.pack()

    # ウィンドウサイズを固定する
    next_window.resizable(False, False)


def open_next_screen1():
    open_next_screen("機器番号", shared_text1)

def open_next_screen2():
    open_next_screen("モード", shared_text2)

def open_next_screen3():
    open_next_screen("運転手コード", shared_text3)

def show_confirmation_dialog():
    # 確認メッセージを表示
    result = messagebox.askquestion("確認", "この内容でよろしいですか？")

    # ユーザーが"Yes"を選択した場合の処理
    if result == "yes":
        # ここに"Yes"を選択した場合の処理を追加
        print("Yes ボタンが押されました")

        
    # ユーザーが"No"を選択した場合の処理
    elif result == "no":
        # ここに"No"を選択した場合の処理を追加
        print("No ボタンが押されました")

def register():
    # エラーチェック
    if not shared_text1.get() or not shared_text2.get() or not shared_text3.get():
        messagebox.showerror("エラー", "全てのテキストを入力してください。")
        return  # エラーがある場合、処理を中断

# ウィンドウの作成
root = tk.Tk()
root.title("クレーン画面操作システム")

root.iconbitmap("crane.ico")

# 機器番号ラベル
equipment_number_label = tk.Label(root, text="機器番号", font=("Helvetica", 20))
equipment_number_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

# モードラベル
mode_label = tk.Label(root, text="モード", font=("Helvetica", 20))
mode_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")

# 運転手コードラベル
driver_code_label = tk.Label(root, text="運転手コード", font=("Helvetica", 20))
driver_code_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")

# 
shared_text1 = tk.StringVar()
shared_text2 = tk.StringVar()
shared_text3 = tk.StringVar()
shared_text1.set("入力項目")
shared_text2.set("入力項目")
shared_text3.set("入力項目")

# 囲み1
frame1 = tk.Frame(root, borderwidth=3, relief="ridge")
frame1.grid(row=1, column=1, padx=20, pady=20)

text_label1 = tk.Label(frame1, textvariable=shared_text1, font=("Helvetica", 20))
text_label1.grid(row=1, column=1)

# 囲み2
frame2 = tk.Frame(root, borderwidth=5, relief="ridge")
frame2.grid(row=2, column=1, padx=20, pady=20)

text_label2 = tk.Label(frame2, textvariable=shared_text2, font=("Helvetica", 20))
text_label2.grid(row=2, column=1)

# 囲み3
frame3 = tk.Frame(root, borderwidth=5, relief="ridge")
frame3.grid(row=3, column=1, padx=20, pady=20)

text_label3 = tk.Label(frame3, textvariable=shared_text3, font=("Helvetica", 20))
text_label3.grid(row=3, column=1)

# 登録ボタン
register_button = tk.Button(root, text="登録", width=10, height=1, command=lambda: (register(),show_confirmation_dialog()),font=("Helvetica", 20))
register_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# テキストクリック時のイベントを設定
text_label1.bind("<Button-1>", lambda event, text_var=shared_text1: open_next_screen1())
text_label2.bind("<Button-1>", lambda event, text_var=shared_text2: open_next_screen2())
text_label3.bind("<Button-1>", lambda event, text_var=shared_text3: open_next_screen3())

# ウィンドウの幅と高さを指定
window_width = 400
window_height = 350

# ウィンドウのサイズを指定
root.geometry(f"{window_width}x{window_height}")

# ウィンドウサイズを固定する
root.resizable(False, False)

root.mainloop()
