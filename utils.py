import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cv2
from instaloader import Instaloader, Profile
from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors


def downloadPics(username):
	loader = Instaloader()
	loader.interactive_login(username)
	profile = Profile.from_username(loader.context, username)
	print("Logged in? ")
	print(loader.context.is_logged_in)

	posts = profile.get_posts()
	count = 0
	for post in posts:
		count += 1
		loader.download_pic(username + "_" + str(count), post.url, post.date_utc)
	return count

def savePieCharts(username, numImages, colorCount=5):
	for i in range(1, numImages + 1):
		fileName = username + "_" + str(i) + ".jpg"
		generate_pie_chart(fileName, colorCount)


def moveFiles(username, numImages):
	# Create username directory
	current_directory = os.getcwd()
	final_directory = os.path.join(current_directory, username)
	if not os.path.exists(final_directory):
   		os.makedirs(final_directory)

	for i in range(1, numImages+1):
   		# Generate source and destination filenames
   		image_src = username + "_" + str(i) + ".jpg"
   		pie_src = username + "_" + str(i) + "_pie.png"

   		# Move
   		os.replace(image_src, username + "/" + image_src)
   		os.replace(pie_src, username + "/" + pie_src)


def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color

def prep_image(raw_img):
    modified_img = cv2.resize(raw_img, (900, 600), interpolation = cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3)
    return modified_img

def color_analysis(img, filename, num_colors):
	matplotlib.use("TkAgg")
	clf = KMeans(n_clusters = num_colors)
	color_labels = clf.fit_predict(img)
	center_colors = clf.cluster_centers_
	counts = Counter(color_labels)
	ordered_colors = [center_colors[i] for i in counts.keys()]
	hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
	fig = plt.figure(figsize = (12, 8))
	plt.pie(counts.values(), colors = hex_colors)
	plt.savefig(filename[:len(filename) - 4] + "_pie.png", transparent=True, bbox_inches='tight')
	plt.close(fig)
	print(hex_colors)

def generate_pie_chart(file, num_colors):
	image = cv2.imread(file)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	modified_img = prep_image(image)
	color_analysis(modified_img, file, num_colors)
