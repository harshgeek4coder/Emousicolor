
from flask import Flask, render_template, Response,request,url_for
import os
import numpy as np
import cv2
from werkzeug.datastructures import MIMEAccept
from camera import camera_stream,video_capture
from PIL import Image, ImageOps
import tensorflow as tf
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array, array_to_img

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import random
import time 
import os

import win32api
import win32gui
import win32con



app = Flask(__name__)
h_path=r"D:\[Working]Test Mod Obj Det\Wallpapers\Happy & Neutral"
s_path=r"D:\[Working]Test Mod Obj Det\Wallpapers\Sad & Angry"
colours=["1.jpg","2.jpg","3.jpg"]
happy=["green.jpg","pink.jpg","yellow.jpg"]
sad=["blue.jpg","purple.jpg","grey.jpg"]
hp=r"\Happy & Neutral"
sp=r"\Sad & Angry"

model = model_from_json(open("Emousic Models/vgg16_model.json", "r").read())
model.load_weights("Emousic Models/vgg16_model_weights.h5")

emotions = ['ANGRY 😡', 'HAPPY 😀', 'NEUTRAL 😐', 'SAD 🙁']


def import_and_predict(image_data, model):
    size = (150, 150)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    image = np.asarray(image)
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_haar_cascade = cv2.CascadeClassifier(
        'haarcascade_frontalface_default.xml')
    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
    for (x, y, w, h) in faces_detected:
        roi_gray = gray_img[y:y+w, x:x+h]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        img_pixels = img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255
        predictions = model.predict(img_pixels)
        max_index = np.argmax(predictions[0])
        emotions = ('ANGRY 😡', 'HAPPY 😀', 'NEUTRAL 😐', 'SAD 🙁')
        predicted = emotions[max_index]
    return predicted

def get_music_emo(emo):
    list1=[]    
    if emo=='HAPPY 😀':
        wrds = ["Vivaldi four seasons", "The Beatles twist and shout", "50 cent heat"]
        kwrd = ["Vivaldi", "Beatles", "50"]
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\Harsh\Downloads\chromedriver_win32 (1)\chromedriver.exe')
        for i, j in zip(wrds, kwrd):
            driver.get("https://www.youtube.com/")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
            driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
            WebDriverWait(driver, 10).until(EC.title_contains(j))
            list1.append(driver.current_url)

        driver.quit()
        webbrowser.open(random.choice(list1))
    elif emo=='SAD 🙁':
        wrds = ["Alec Benjamin - Let Me Down Slowly", "Trevor Daniel - Falling ", "Marshmello ft. Bastille - Happier"]
        kwrd = ["Slowly", "Falling", "Happier"]
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\Harsh\Downloads\chromedriver_win32 (1)\chromedriver.exe')
        for i, j in zip(wrds, kwrd):
            driver.get("https://www.youtube.com/")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
            driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
            WebDriverWait(driver, 10).until(EC.title_contains(j))
            list1.append(driver.current_url)

        driver.quit()
        webbrowser.open(random.choice(list1))  




    elif emo=='ANGRY 😡':
        wrds = ["Alec Benjamin - Let Me Down Slowly", "Trevor Daniel - Falling ", "Marshmello ft. Bastille - Happier"]
        kwrd = ["Slowly", "Falling", "Happier"]
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\Harsh\Downloads\chromedriver_win32 (1)\chromedriver.exe')
        for i, j in zip(wrds, kwrd):
            driver.get("https://www.youtube.com/")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
            driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
            WebDriverWait(driver, 10).until(EC.title_contains(j))
            list1.append(driver.current_url)

        driver.quit()
        webbrowser.open(random.choice(list1))  

    elif emo=='NEUTRAL 😐':
        wrds = ["Alec Benjamin - Let Me Down Slowly", "Trevor Daniel - Falling ", "Marshmello ft. Bastille - Happier"]
        kwrd = ["Let Me Down Slowly", "Falling", "Happier"]
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\Harsh\Downloads\chromedriver_win32 (1)\chromedriver.exe')
        for i, j in zip(wrds, kwrd):
            driver.get("https://www.youtube.com/")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
            driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
            WebDriverWait(driver, 10).until(EC.title_contains(j))
            list1.append(driver.current_url)

        driver.quit()
        webbrowser.open(random.choice(list1))  

def wallpaper(path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)  
    
    

def emo_wall(emotion):

    for i in range(0,3):
        time.sleep(20)
        if emotion=='HAPPY 😀' or 'NEUTRAL 😐':
            fp=os.path.join(h_path,happy[i])
        elif emotion=='ANGRY 😡' or  'SAD 🙁':
            fp=os.path.join(s_path,sad[i])
        print(fp)
        wallpaper(fp)    


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/takeimage', methods = ['GET','POST'])
def takeimage():
    _, frame = video_capture.read()
    cv2.imwrite('./images_direc/photo.jpg', frame)
    #file='./images_direc/photo.jpg'
    #image=Image.open(file)
    #predictions=import_and_predict(image,model)
    
    return Response(status = 200)




@app.route('/getimage', methods = ['GET','POST'])
def getimage():
    file='./images_direc/photo.jpg'
    image=Image.open(file)
    predictions=import_and_predict(image,model)
    get_music_emo(predictions)
    emo_wall(predictions)
    return render_template('index.html',predict=predictions)



def gen_frame():
    """Video streaming generator function."""
    while True:
        frame = camera_stream()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') # concate frame one by one and show result


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(threaded=True)




