import requests
import tkinter as tk
from bs4 import BeautifulSoup

window = tk.Tk()
window.title("news")
window.geometry("800x600")

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(window, width=800, yscrollcommand=scrollbar.set)

url_1 = "https://www.setn.com/ViewAll.aspx"
r_1 = requests.get(url_1)
html_str_1 = r_1.text
soup_1 = BeautifulSoup(html_str_1, features="html.parser")
selector = "#NewsList div div h3 a"
for i in soup_1.select(selector):
  if i.get("href").startswith("http"):
    listbox.insert(tk.END, i.text+" "+i.get("href"))
  else:
    listbox.insert(tk.END, i.text+" "+"https://www.setn.com"+i.get("href"))

url_2 = "https://www.ltn.com.tw"
r_2 = requests.get(url_2)
html_str_2 = r_2.text
soup_2 = BeautifulSoup(html_str_2, features="html.parser")
selector_1 = ".breakingnews_pc ul li a"
selector_2 = ".breakingnews_pc ul li.hiddenBlock a"
for i in set(soup_2.select(selector_1))-set(soup_2.select(selector_2)):
  listbox.insert(tk.END, i.get("title")+" "+i.get("href"))

url_3 = "https://www.chinatimes.com/?chdtv"
r_3 = requests.get(url_3)
html_str_3 = r_3.text
soup_3 = BeautifulSoup(html_str_3, features="html.parser")
selector = "#news-pane-1-1 ul li h4 a"
for i in soup_3.select(selector):
  listbox.insert(tk.END, i.text+" "+i.get("href"))

url_4 = "https://udn.com/news/index"
r_4 = requests.get(url_4)
html_str_4 = r_4.text
soup_4 = BeautifulSoup(html_str_4, features="html.parser")
selector = ".udn-tab div div a"
for i in soup_4.select(selector):
  listbox.insert(tk.END, i.get("title")+" "+i.get("href"))

url_5 = "https://news.tvbs.com.tw/realtime"
r_5 = requests.get(url_5)
html_str_5 = r_5.text
soup_5 = BeautifulSoup(html_str_5, features="html.parser")
selector = ".list ul li a h2"
for i in soup_5.select(selector):
  listbox.insert(tk.END, i.text+" "+"https://news.tvbs.com.tw"+i.parent.get("href"))

listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=listbox.yview)

window.mainloop()
