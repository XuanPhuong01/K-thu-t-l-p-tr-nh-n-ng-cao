import tkinter as tk
from tkinter import filedialog, font, messagebox
from collections import Counter
import re
import matplotlib.pyplot as plt

# ================== HÀM XỬ LÝ ==================
def open_file():
    path = filedialog.askopenfilename(
        title="Chọn file văn bản",
        filetypes=[("Text files", "*.txt")]
    )
    if path:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, content)

def analyze_text():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Thông báo", "Chưa có nội dung văn bản!")
        return

    words = re.findall(r'\w+', text.lower())
    counter = Counter(words)

    result_box.delete("1.0", tk.END)
    for word, count in counter.most_common(10):
        result_box.insert(tk.END, f"{word:<15} : {count}\n")

    show_chart(counter)

def show_chart(counter):
    top = counter.most_common(10)
    labels = [w for w, _ in top]
    values = [c for _, c in top]

    plt.figure(figsize=(8, 4))
    plt.bar(labels, values)
    plt.title("Top 10 từ xuất hiện nhiều nhất")
    plt.xlabel("Từ")
    plt.ylabel("Số lần")
    plt.tight_layout()
    plt.show()

# ================== GIAO DIỆN ==================
root = tk.Tk()
root.title("Phân tích văn bản")
root.geometry("1000x550")
root.configure(bg="#e8ecf3")

# Font
title_font = font.Font(family="Segoe UI", size=18, weight="bold")
label_font = font.Font(family="Segoe UI", size=11)
text_font = font.Font(family="Segoe UI", size=11)
btn_font = font.Font(family="Segoe UI", size=11, weight="bold")

# ===== HEADER =====
header = tk.Frame(root, bg="#2c3e50", height=70)
header.pack(fill="x")

title = tk.Label(
    header,
    text="CHƯƠNG TRÌNH PHÂN TÍCH VÀ THỐNG KÊ TỪ KHÓA",
    font=title_font,
    fg="white",
    bg="#2c3e50"
)
title.pack(pady=15)

# ===== MAIN CONTENT =====
content = tk.Frame(root, bg="#e8ecf3")
content.pack(fill="both", expand=True, padx=15, pady=15)

# ===== LEFT PANEL =====
left = tk.Frame(content, bg="white", bd=1, relief="solid")
left.pack(side="left", fill="both", expand=True, padx=10)

left_title = tk.Label(
    left,
    text="NỘI DUNG VĂN BẢN",
    font=label_font,
    bg="white"
)
left_title.pack(pady=8)

btn_open = tk.Button(
    left,
    text="Chọn file văn bản (.txt)",
    font=btn_font,
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    relief="flat",
    command=open_file
)
btn_open.pack(pady=5)

text_input = tk.Text(
    left,
    font=text_font,
    wrap="word",
    height=15,
    bd=0
)
text_input.pack(fill="both", expand=True, padx=10, pady=10)

# ===== RIGHT PANEL =====
right = tk.Frame(content, bg="white", bd=1, relief="solid")
right.pack(side="right", fill="both", expand=True, padx=10)

right_title = tk.Label(
    right,
    text="KẾT QUẢ PHÂN TÍCH",
    font=label_font,
    bg="white"
)
right_title.pack(pady=8)

btn_analyze = tk.Button(
    right,
    text="Phân tích văn bản",
    font=btn_font,
    bg="#27ae60",
    fg="white",
    activebackground="#1e8449",
    relief="flat",
    command=analyze_text
)
btn_analyze.pack(pady=5)

result_box = tk.Text(
    right,
    font=text_font,
    height=15,
    bd=0,
    bg="#f7f9fc"
)
result_box.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
