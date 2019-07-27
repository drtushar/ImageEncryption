import hashlib
import cv2
import os
import base64

def encrypt_string(hash_string):
	sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
	return sha_signature
	
def load_images_from_folder(folder):
    f = open('/home/tushar/Desktop/SIH.txt','a+')
    img = cv2.imread(folder,cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
    if img is not None:
        with open(folder, "rb") as imageFile:
            s = base64.b64encode(imageFile.read())                
            sha_signature = encrypt_string(str(s))
            print(sha_signature,folder,file = f)
            print(sha_signature,folder)
    f.close() 
    
load_images_from_folder('/home/tushar/Desktop/8s.png')      	  	