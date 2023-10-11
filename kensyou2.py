import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("ウィンドウサイズ固定の例")

# ウィンドウサイズを固定する
root.resizable(False, False)

# ラベルの作成
label1 = tk.Label(root, text="ラベル1", font=("Helvetica", 20))
label2 = tk.Label(root, text="ラベル2", font=("Helvetica", 20))
label3 = tk.Label(root, text="ラベル3", font=("Helvetica", 20))

# ラベルの配置（packレイアウトを使用）
label1.pack(padx=10, pady=10)
label2.pack(padx=10, pady=10)
label3.pack(padx=10, pady=10)

root.mainloop()
