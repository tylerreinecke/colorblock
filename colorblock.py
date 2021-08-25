from tkinter import *
import utils
from gui import GUI
import os


if __name__ == '__main__':
	username = input("Enter Instagram username: ")
	user_dir = "./" + username + "/"
	if not os.path.exists(user_dir):
		# Download the images
		num_downloaded = utils.downloadPics(username)
		
		# Analyze the images and get dominant colors, save to pie charts
		utils.savePieCharts(username, num_downloaded, 5)
		
		# Move images and pie charts to new directory
		utils.moveFiles(username, num_downloaded)
		
		gui = GUI(username, num_downloaded)
	else:
		num_exists = int(len(os.listdir(user_dir)) / 2)
		gui = GUI(username, num_exists)
	gui.root.mainloop()
