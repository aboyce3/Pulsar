import matplotlib.figure as mpl
from Pulsar import Pulsar
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import *
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg


def helper():
    if not (MassEntry.get().isdigit() and LumEntry.get().isdigit() and TempEntry.get().isdigit() and
            XEntry.get().isdigit() and ZEntry.get().isdigit() and MaxPeriodEntry.get().isdigit() and
            MaxAmpEntry.get().isdigit()):
        ProgressBar.delete(1.0, END)
        ProgressBar.insert(END, "All fields must contain a positive number")
        return False
    else:
        if not ((float(MassEntry.get()) > 0) and (float(MassEntry.get()) < 100) and (float(LumEntry.get()) < 100000) and
                (float(LumEntry.get()) > 0) and (float(TempEntry.get()) > 3000) and (float(TempEntry.get()) < 10000)):
            ProgressBar.delete(1.0, END)
            ProgressBar.insert(END, "Mass, Temperature, and/or Luminosity are invalid")
            return False
        else:
            if (float(XEntry.get()) >= 0) and (float(ZEntry.get()) >= 0) and (float(MaxPeriodEntry.get()) >= 0) and \
                    (float(MaxAmpEntry.get()) >= 0):
                return True


def linking():
    if not var.get() == "CepheidFile.txt":
        if var.get() == "RRLyraeFile.txt":
            name = "RR"
        else:
            ProgressBar.delete(1.0, END)
            ProgressBar.insert(END, "No Pulsar has been selected")
            return None
    else:
        name = "C"

    if helper():
        pulsar = Pulsar(float(MassEntry.get()), float(LumEntry.get()), float(XEntry.get()), float(ZEntry.get()), name,
                        float(MaxAmpEntry.get()), float(MaxPeriodEntry.get()), float(TempEntry.get()))
        notification_message = "Successfully created a Cepheid" if name == "C" else "Successfully created an RR-Lyrae"
        ProgressBar.delete(1.0, END)
        ProgressBar.insert(END, notification_message)
        return pulsar
    else:
        return None


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w / 2, loc[1] + figure_h / 2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo


root = Tk()
root.title('Pulsar GUI')
root.geometry('500x700')

rows = 0
while rows < 50:
    root.rowconfigure(rows, weight=1)
    root.columnconfigure(rows, weight=1)
    rows += 1

n = ttk.Notebook(root)
n.grid(row=1, column=1, columnspan=50, rowspan=49, sticky='NESW')
f1 = ttk.Frame(n)
f2 = Canvas(n)
n.add(f1, text='Input Tab')
n.add(f2, text='Output Tab')
n.select(f1)
n.enable_traversal()

var = StringVar()
var.set("L")
R1 = Radiobutton(f1, text="Cepheid", variable=var, value="CepheidFile.txt", command=None)
R1.pack(anchor=W)
R2 = Radiobutton(f1, text="RR-Lyrae", variable=var, value="RRLyraeFile.txt", command=None)
R2.pack(anchor=W)

MassLabel = Label(f1, text="Mass")
MassLabel.pack(anchor=W)
MassEntry = Entry(f1, bd=15)
MassEntry.pack(anchor=W)

TempLabel = Label(f1, text="Temperature")
TempLabel.pack(anchor=W)
TempEntry = Entry(f1, bd=15)
TempEntry.pack(anchor=W)

LumLabel = Label(f1, text="Luminosity")
LumLabel.pack(anchor=W)
LumEntry = Entry(f1, bd=15)
LumEntry.pack(anchor=W)

XLabel = Label(f1, text="Hydrogen Composition")
XLabel.pack(anchor=W)
XEntry = Entry(f1, bd=15)
XEntry.pack(anchor=W)

ZLabel = Label(f1, text="Metal Composition")
ZLabel.pack(anchor=W)
ZEntry = Entry(f1, bd=15)
ZEntry.pack(anchor=W)

MaxPeriodLabel = Label(f1, text="Max Period")
MaxPeriodLabel.pack(anchor=W)
MaxPeriodEntry = Entry(f1, bd=15)
MaxPeriodEntry.pack(anchor=W)

MaxAmpLabel = Label(f1, text="Max Amp")
MaxAmpLabel.pack(anchor=W)
MaxAmpEntry = Entry(f1, bd=15)
MaxAmpEntry.pack(anchor=W)

ProgressBar = Text(f1, height=1, width=50)
ProgressBar.pack(side=LEFT)
quote = "Something is happening"
ProgressBar.insert(END, quote)

# Creates a pulsar object
submit = Button(f1, text="Submit", command=linking)
submit.pack(side=BOTTOM)

X = np.linspace(0, 2 * np.pi, 50)
Y = np.sin(X)

fig = mpl.Figure(figsize=(2, 1))
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(X, Y)

fig_x, fig_y = 100, 100
fig_photo = draw_figure(f2, fig, loc=(fig_x, fig_y))
fig_w, fig_h = fig_photo.width(), fig_photo.height()

root.mainloop()
