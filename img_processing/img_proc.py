import tkinter as tk
from PIL import Image, ImageTk, ImageFilter


def Edge_Detection(path):
	img = Image.open(path)
	img_edge = img.filter(ImageFilter.FIND_EDGES)
	img_edge.save('a1.png')
	pat = 'a1.png'
	display(pat)
def Blur(path):
	img = Image.open(path)
	img_blur = img.filter(ImageFilter.GaussianBlur(2))
	img_blur.save('a1.png')
	pat = 'a1.png'
	display(pat)
def Reflect(path):
	img = Image.open(path)
	img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
	img_flip.save('a1.png')
	pat = 'a1.png'
	display(pat)
def Sharp(path):
	img = Image.open(path)
	img_sharp = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
	img_sharp.save('a1.png')
	pat = 'a1.png'
	display(pat)
def Kernel(path):
	img = Image.open(path)
	img_sharp = img.filter(ImageFilter.ModeFilter(size=9))
	img_sharp.save('a1.png')
	pat = 'a1.png'
	display(pat)
def Contour(path):
	img = Image.open(path)
	img_cont = img.filter(ImageFilter.CONTOUR)
	img_cont.save('a1.png')
	pat = 'a1.png'
	display(pat)
def Emboss(path):
	img = Image.open(path)
	img_emb = img.filter(ImageFilter.EMBOSS)
	img_emb.save('a1.png')
	pat = 'a1.png'
	display(pat)
def Org(path):
	display(path)
def display(pat):
	size = int(lower_frame.winfo_height()*0.75)
	img = ImageTk.PhotoImage(Image.open(pat).resize((size, size)))
	output.delete("all")
	output.create_image(500,0, anchor='nw', image=img)
	output.image = img

	
root = tk.Tk()
root.title('Image Processing')
path = 'a.jpeg'
canvas = tk.Canvas(root, height=1080, width=1920)
canvas.pack()

background_image = tk.PhotoImage(file='bggg.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#595959', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

frame_a = tk.Frame(root, bg='#595959', bd=10)
frame_a.place(relx=0.08, rely=0.1, relwidth=0.1, relheight=0.7, anchor='n')

#horizontal
kernel = tk.Button(frame_a, text='Kernel', command = lambda: Kernel(path), font = ('calibri',20, 'bold'))
kernel.place(relx=0.0, relheight=0.2, relwidth=0.9)

contour = tk.Button(frame_a, text='Contour', command = lambda: Contour(path), font = ('calibri',20, 'bold'))
contour.place(relx=0.0, rely =0.4, relheight=0.2, relwidth=0.9)

emboss = tk.Button(frame_a, text='Emboss', command = lambda: Emboss(path), font = ('calibri',20, 'bold'))
emboss.place(relx=0.0, rely =0.8, relheight=0.2, relwidth=0.9)

#vertical
edge_detect = tk.Button(frame, text = 'Edge Detection', command = lambda: Edge_Detection(path), font = ('calibri',20, 'bold'))
edge_detect.place(relx=0, relheight=0.9, relwidth=0.2)

mirror = tk.Button(frame, text='Reflect', command = lambda: Reflect(path), font = ('calibri',20, 'bold'))
mirror.place(relx=0.2, relheight=0.9, relwidth=0.2)

blur = tk.Button(frame, text='Blur', command = lambda: Blur(path), font = ('calibri',20, 'bold'))
blur.place(relx=0.4, relheight=0.9, relwidth=0.2)

org = tk.Button(frame, text='Original', command = lambda: Org(path), font = ('calibri',20, 'bold'))
org.place(relx=0.6, relheight=0.9, relwidth=0.2)

sharp = tk.Button(frame, text='Sharpen', command = lambda: Sharp(path), font = ('calibri',20, 'bold'))
sharp.place(relx=0.8, relheight=0.9, relwidth=0.2)





lower_frame = tk.Frame(root, bg='#595959', bd=10)
lower_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.6, anchor='n')
bg_color = 'white'
output = tk.Canvas(lower_frame, bg=bg_color, bd=10, highlightthickness=0)
output.place(relx=0, rely=0, relwidth=1, relheight=0.9)

root.mainloop()