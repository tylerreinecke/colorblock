import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image

HEIGHT = 390
WIDTH = 844

class GUI():
	def __init__(self, username, num_photos):
		self.username = username
		self.num_photos = num_photos

		self.root = tk.Tk()
		self.root.geometry("415x844")
		self.root.title("COLORBLOCK")
		#root.resizeable(0,0)

		self.create_widgets()

	def change_button_image(self, i, image_name, pie_name):
		if self.button_dict[i][1] == False:
			self.button_dict[i][0].config(image=self.image_dict[image_name])
			print(i, self.button_dict[i][1], False)
			print(image_name)
			self.button_dict[i][1] = True
		else:
			self.button_dict[i][0].config(image=self.pie_dict[pie_name])
			print(i, self.button_dict[i][1], True)
			print(pie_name)
			self.button_dict[i][1] = False

	def create_widgets(self):
	
# root
# 	label
# 	frame
# 		canvas
# 			frame
# 				buttons
# 		scrollbar

		frame_main = tk.Frame(self.root)
		frame_main.grid()

		# Username
		neue_helv = font.Font(root=self.root, family='Helvetica', size=36, weight='bold')
		user_label = tk.Label(frame_main, text='@'+self.username, font=neue_helv)
		user_label.grid(row=0, column=0, sticky="W")

		# Frame
		frame_canvas = tk.Frame(frame_main)
		frame_canvas.grid(row=1, column=0)

		# Canvas and Scrollbar
		canvas = tk.Canvas(frame_canvas, width=400, height=800)
		canvas.grid(row=0, column=0)

		scrollbar = tk.Scrollbar(frame_canvas, orient='vertical', command=canvas.yview)
		scrollbar.grid(row=0, column=1, sticky='NS')
		canvas.configure(yscrollcommand=scrollbar.set)
		canvas.configure(scrollregion=canvas.bbox('all'))

		# Frame to hold buttons
		frame_buttons = tk.Frame(canvas)
		canvas.create_window((0,0), window=frame_buttons, anchor='nw')


		



# #####################
# 		# Canvas
# 		canvas = tk.Canvas(self.root, width=415, height = 800)
# 		canvas.pack()

# 		scrollbar = tk.Scrollbar(canvas, orient='vertical', command=canvas.yview)

# 		# Username
# 		neue_helv = font.Font(root=self.root, family='Helvetica', size=36, weight='bold')
# 		user_label = tk.Label(canvas, text='@'+self.username, font=neue_helv)
# 		user_label.grid(row=0, column=0, columnspan=2, sticky="W")

		# Posts
		self.button_dict = {} #key = int (index): value = (Button, bool)
		self.image_dict = {} #key = str (filename): value = PhotoImage
		self.pie_dict = {} #key = str (filename): value = PhotoImage

		for i in range(1, self.num_photos+1):
			# Generate filenames
			image_name = self.username + "/" + self.username + "_" + str(i) + ".jpg"
			pie_name = self.username + "/" + self.username + "_" + str(i) + "_pie.png"

			# Open images
			temp_image = Image.open(image_name)
			temp_pie = Image.open(pie_name)

			# Resize images
			temp_image_resized = temp_image.resize((130,130), Image.ANTIALIAS)
			temp_pie_resized = temp_pie.resize((130,130), Image.ANTIALIAS)

			# Save images
			self.image_dict[image_name] = ImageTk.PhotoImage(temp_image_resized)
			self.pie_dict[pie_name] = ImageTk.PhotoImage(temp_pie_resized)

			# Create buttons
			self.button_dict[i] = ImageButton(frame_buttons, i, self.pie_dict[pie_name], self.image_dict[image_name], self.root)
			self.button_dict[i].getButton().grid(row = int((i+2)/3), column = (i-1)%3)


class ImageButton():
	def __init__(self, parent, i, pie, image, root):
		self.showingPie = True
		self.parent = parent
		self.i = i
		self.pie = pie
		self.image = image
		self.root = root
		self.button = tk.Button(self.parent, image=pie, command=self.swapDisplay, bd=0, height=0)

	def getButton(self):
		return self.button

	def swapDisplay(self):
		if self.showingPie:
			self.button['image'] = self.image
		else:
			self.button['image'] = self.pie
		self.root.update_idletasks()
		self.showingPie = not self.showingPie

	


# def getUsername():
# 	root = tk.Tk()

# 	canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
# 	canvas.pack()

# 	frame = tk.Frame(root, height=HEIGHT, width=WIDTH)
# 	frame.place(relheight=1, relwidth=1)

# 	label = tk.Label(frame, text="Enter your Instagram username:", height=100)
# 	label.place(relwidth=1, relx=0.5, rely=0.2, anchor='center')

# 	entry = tk.Entry(frame)
# 	entry.place(relx=0.5, rely=0.5, anchor='center')

# def displayProfile(username, num_photos):
# 	root = tk.Tk()

# 	canvas = tk.Canvas(root, width=620, height=1000)
# 	canvas.pack()

# 	neue_helv = font.Font(root=root, family='Helvetica', size=36, weight='bold')
# 	user_label = tk.Label(canvas, text='@'+username, font=neue_helv)
# 	user_label.place(x=20, y=50)

# 	frame = tk.Frame(canvas, height = 850)
# 	frame.place(y=150)

# 	button_list = []
# 	for i in range(1, num_photos+1):


# 	row = 0
# 	col = 0
# 	for i in range(1, num_photos+1):
# 		image = ImageTk.PhotoImage(file="thomfhoolery_" + str(i) + ".jpg")
# 		image_pie_og = Image.open("thomfhoolery_" + str(i) + "_pie.png")
# 		image_pie_rsz = image_pie_og.resize((200,200), Image.ANTIALIAS)
# 		image_pie = ImageTk.PhotoImage(image_pie_rsz)
# 		button = tk.Button(frame, image=image_pie, bd=0)
# 		button.grid(row=row, column=col)
# 		col += 1
# 		if col == 3:
# 			col = 0
# 			row +=1


# 	# image1 = ImageTk.PhotoImage(file="thomfhoolery_1.jpg")
# 	# image1_pie_og = Image.open("thomfhoolery_1_pie.png")
# 	# image1_pie_rsz = image1_pie_og.resize((200,200), Image.ANTIALIAS)
# 	# image1_pie = ImageTk.PhotoImage(image1_pie_rsz)
# 	# button1 = tk.Button(frame, image=image1_pie, bd=0)
# 	# button1.grid(row=0, column=0)

# 	# image2 = ImageTk.PhotoImage(file=username + "_" + str(2) + ".jpg")
# 	# image2_pie = tk.PhotoImage(file=username + "_" + str(2) + "_pie.png")
# 	# button2 = tk.Button(frame, image=image2_pie, width=200, height=200)
# 	# button2.grid(row=0, column=1)

# 	# image3 = ImageTk.PhotoImage(file=username + "_" + str(3) + ".jpg")
# 	# image3_pie = tk.PhotoImage(file=username + "_" + str(3) + "_pie.png")
# 	# button3 = tk.Button(frame, image=image3_pie, width=200, height=200)
# 	# button3.grid(row=0, column=2)


# 	root.mainloop()
