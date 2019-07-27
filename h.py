import hashlib
import cv2
import os
from stegano import lsb
import base64

def encrypt_string(hash_string):
	sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
	return sha_signature
	
def load_images_from_folder(folder):
    f = open('/home/tushar/Desktop/PythonProject/HashOutputs/ubuntuMade1.txt','a+')
    for filename in os.listdir(folder):
        img = cv2.imread(folder+'/'+filename,cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
        #secret = lsb.hide(folder+'/'+filename, "Hello Rushi")
        #secret.save('/home/tushar/Desktop/PythonProject/secretimages/14/'+filename+'_secret.tif')
        img = cv2.imread(folder+'/'+filename+"secret",cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
        if img is not None:
            with open(folder+'/'+filename, "rb") as imageFile:
                s = base64.b64encode(imageFile.read())                
            sha_signature = encrypt_string(str(s))
            print(sha_signature,filename+"secret",file = f)
            
    f.close()                        		            		

for i in range(1,15):
    load_images_from_folder('/home/tushar/Desktop/PythonProject/images/'+str(i),str(i))
#load_images_from_folder('/home/tushar/Desktop/PythonProject/images/14')       	
	
'''	
with open("t.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())

directory = os.fsencode(directory_in_str)	
for file in os.listdir(directory):
    
    				
secret = lsb.hide("./tests/sample-files/Lenna.png", "Hello World")
>>> secret.save("./Lenna-secret.png")
>>>
>>> clear_message = lsb.reveal("./Lenna-secret.png")	
				
							
										
																
	
img = str(cv2.imread('C:/Users/ItsTRD/Desktop/pyhtonWork/2.tif',-1))
print(img)	
sha_signature = encrypt_string(img)
print(sha_signature)
'''
