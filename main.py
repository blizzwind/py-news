import requests
import tkinter as tk
from bs4 import BeautifulSoup

def crawl():
    listbox.delete(0, tk.END)
    url = var_url.get()
    selector = var_selector.get()
    r = requests.get(url)
    html_str = r.text
    soup = BeautifulSoup(html_str, features="html.parser")
    for i in soup.select(selector):
        listbox.insert(tk.END, i.text)

window = tk.Tk()
window.title("news")
window.geometry("800x600")

var_url = tk.StringVar()
var_selector = tk.StringVar()

label_url = tk.Label(window, text="url:")
label_url.pack()

entry_url = tk.Entry(window, textvariable=var_url)
entry_url.pack()

label_selector = tk.Label(window, text="selector:")
label_selector.pack()

entry_selector = tk.Entry(window, textvariable=var_selector)
entry_selector.pack()

button = tk.Button(window, text="crawl", command=crawl)
button.pack()

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(window, width=800, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=listbox.yview)

window.mainloop()
