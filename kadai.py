import tkinter as tk

def open_next_screen():
    # ここに次の画面を開くコードを追加する

# ウィンドウの作成
root = tk.Tk()
root.title("クレーン画面操作システム")

# システム名ラベル
system_name_label = tk.Label(root, text="システム名")
system_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# 機器番号ラベル
equipment_number_label = tk.Label(root, text="機器番号")
equipment_number_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# モードラベル
mode_label = tk.Label(root, text="モード")
mode_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# 運転手コードラベル
driver_code_label = tk.Label(root, text="運転手コード")
driver_code_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# テキスト
text_label = tk.Label(root, text="クリックして次の画面を開く")
text_label.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

# テキストクリック時のイベントを設定
text_label.bind("<Button-1>", lambda event: open_next_screen())

root.mainloop()
