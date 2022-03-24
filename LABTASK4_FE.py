# FRONT END

import tkinter as tk
import LABTASK4_DB as dbc

db = dbc.CDB
db.new_connect(db)

root = tk.Tk()

root.title(
    "TheAtifWaheed - LabTask 4"
)

frame1 = tk.Frame(
    root,
    height=200,
    width=200
)

frame2 = tk.Frame(
    root,
    height=200,
    width=200
)

l_id = tk.Label(
    frame1,
    text="ID: ",
    font=20,
    foreground="black"
)
l_name = tk.Label(
    frame1,
    text="Name: ",
    font=20,
    foreground="black"
)
l_degree = tk.Label(
    frame1,
    text="Degree: ",
    font=20,
    foreground="black"
)

e_id = tk.Entry(
    frame1,
    font=20
)

e_name = tk.Entry(
    frame1,
    font=20
)

e_degree = tk.Entry(
    frame1,
    font=20
)

b_s = tk.Button(
    frame2,
    text="Search",
    font=25,
    background="yellow",
    command=lambda: fun_s()
)

b_u = tk.Button(
    frame2,
    text="Update",
    font=25,
    background="pink",
    command=lambda: fun_u()
)

frame1.pack(
    side=tk.LEFT,
    fill=tk.Y
)

frame2.pack(
    side=tk.LEFT,
    fill=tk.Y
)

l_id.pack(
    expand=tk.FALSE
)

e_id.pack(
    expand=tk.FALSE
)

l_name.pack(
    expand=tk.FALSE
)

e_name.pack(
    expand=tk.FALSE
)


l_degree.pack(
    expand=tk.FALSE
)


e_degree.pack(
    expand=tk.FALSE
)

b_s.pack(
    expand=tk.TRUE
)

b_u.pack(
    expand=tk.TRUE
)


def fun_s():
    sid = str(e_id.get())
    data = db.getData(db, sid)
    e_id.delete(0, tk.END)
    e_id.insert(0, data[0][0])
    e_name.insert(0, data[0][1])
    e_degree.insert(0, data[0][2])

def fun_u():
    g_id = str(e_id.get())
    g_name = str(e_name.get())
    g_degree = str(e_degree.get())
    db.updateData(db, g_id, g_name, g_degree)
    print("Update Success")



root.mainloop()