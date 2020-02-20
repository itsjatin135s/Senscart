from mainapp. __init__ import app
import os
import random


pf= os.path.join('static','images','index')
app.config['UPLOAD_FOLDER'] = pf




def change_img():
	img = random.randint(1,5)
	if img == 1 :
		img1=os.path.join(app.config['UPLOAD_FOLDER'],'img1.jpg')	
	elif img == 2 :
		img1=os.path.join(app.config['UPLOAD_FOLDER'],'img2.jpg')	
	elif img == 3 :
		img1=os.path.join(app.config['UPLOAD_FOLDER'],'img3.jpg')
	elif img == 4 :
		img1=os.path.join(app.config['UPLOAD_FOLDER'],'img4.jpg')
	else :
		img1=os.path.join(app.config['UPLOAD_FOLDER'],'img5.jpg')

	return (img1)


def change_img1():
	img = random.randint(1,5)
	if img == 1 :
		img2=os.path.join(app.config['UPLOAD_FOLDER'],'img6.jpg')	
	elif img == 2 :
		img2=os.path.join(app.config['UPLOAD_FOLDER'],'img7.jpg')	
	elif img == 3 :
		img2=os.path.join(app.config['UPLOAD_FOLDER'],'img8.jpg')
	elif img == 4 :
		img2=os.path.join(app.config['UPLOAD_FOLDER'],'img9.jpg')
	else :
		img2=os.path.join(app.config['UPLOAD_FOLDER'],'img10.jpg')

	return (img2)