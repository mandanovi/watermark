# Import required libraries
from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image, ImageGrab, ImageDraw, ImageFont
from tkinter.ttk import *
import io


class ImageWatermark(Tk):  # Create an instance of tkinter window
    def __init__(self):
        super().__init__()
        self.title("Photo Watermark")
        self.geometry("400x500")  # Define the geometry of the window
        self.widget()

    def find_image(self):
        file_types = (("jpeg", "*.jpg"), ("png", "*.png"))
        pic_name = fd.askopenfilename(title="Open an image", initialdir='/Users/manda/portfolio/CODING',
                                 filetypes=file_types)
        self.img_name = pic_name.split('/')[-1]
        self.img = Image.open(pic_name)
        o_size = self.img.size
        f_size = (700, 700)
        factor = min(float(f_size[1]) / o_size[1], float(f_size[0]) / o_size[0])
        width = int(o_size[0] * factor)
        height = int(o_size[1] * factor)
        self.rImg = self.img.resize((width, height), Image.Resampling.LANCZOS)
        self.rImg = ImageTk.PhotoImage(self.rImg)
        self.canvas.create_image(225, 225, anchor="center", image=self.rImg)
        self.canvas.image = self.rImg  # keep reference to the image

    def widget(self):
        # logo = Image.open('logo.jpg')
        # logo = ImageTk.PhotoImage(logo)
        # logo_label = Label(image=logo)
        # logo_label.image = logo
        # logo_label.grid(column=1, row=0)
        style = Style()
        style.configure("TButton", foreground="purple", background="pink")
        self.input = Label(width=25, text="Write your text")
        self.input.grid(column=3, row=3)
        self.entry = Entry(width=30)
        self.entry.grid(column=4, row=3)
        self.white = Button(self, text="White Text", width=20, command=self.add_white)
        self.white.grid(column=3, row=4, sticky=W)
        self.black = Button(self, text="Black Text", width=20, command=self.add_black)
        self.black.grid(column=3, row=5, sticky=W)
        self.add_img = Button(self, text="Add image WM", width=20, command=self.add_image)
        self.add_img.grid(column=3, row=6, sticky=W)
        self.upload = Button(self, text="Upload Picture", width=20, command=self.find_image)
        self.upload.grid(column=4, row=4, padx=10)
        self.save = Button(self, text="Save Picture", width=20, command=self.save_picture)
        self.save.grid(column=4, row=5)
        self.exit = Button(self, text="Exit", width=20, command=exit)
        self.exit.grid(column=4, row=6)
        self.canvas = Canvas(self, width=400, height=400)
        self.canvas.grid(row=0, column=1, columnspan=5)

    def add_white(self):
        self.canvas.create_text(350, 350, fill="white", font=("Arial",25),
                                text=self.entry.get())

    def add_black(self):
        self.canvas.create_text(300, 350, fill="black", font=("Arial",25),
                                text=self.entry.get())

    def add_image(self):
        file_types = (("jpeg", "*.jpg"), ("png", "*.png"))
        pic_name = fd.askopenfilename(title="Open an image", initialdir='/Users/manda/portfolio/CODING',
                                      filetypes=file_types)
        image_name = pic_name.split('/')[-1]
        img = Image.open(image_name)
        o_size = img.size
        f_size = (100, 100)
        factor = min(float(f_size[1]) / o_size[1], float(f_size[0]) / o_size[0])
        print(f"factor = {factor}")
        width = int(o_size[0] * factor)
        height = int(o_size[1] * factor)
        self.wImg = img.resize((width, height), Image.Resampling.LANCZOS)
        self.wImg = ImageTk.PhotoImage(self.wImg)
        self.canvas.create_image(390, 300, anchor="ne", image=self.wImg)
        self.canvas.image = self.wImg  # keep reference to the image


    def exit(self):
        self.destroy()

    def save_picture(self):
        wd = 800
        ht = 800
        ps = self.canvas.postscript(colormode='color', pagewidth=wd, pageheight=ht)
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        file_location = fd.askdirectory(title="Save new images to...")
        new_name = 'watermarked_' + self.img_name
        img.save(f"{file_location}/{new_name}")

        # x = self.winfo_rootx() + self.canvas.winfo_x()
        # y = self.winfo_rooty() + self.canvas.winfo_y()
        # print(x, y)
        # x1 = x + self.canvas.winfo_width() + 300
        # y1 = y + self.canvas.winfo_height() + 250
        # print(x1, y1)
        # new_name = 'watermarked_' + self.img_name
        # file_location = fd.askdirectory(title="Save new images to...")
        # image = ImageGrab.grab().crop((x, y, x1, y1))
        # image.save(f"{file_location}/{new_name}")


App = ImageWatermark()
App.mainloop()