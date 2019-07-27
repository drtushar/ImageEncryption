from stegano import lsb
#secret = lsb.hide("/home/tushar/Desktop/8.png", "Never Mind")
#secret.save("/home/tushar/Desktop/8s.png")

clear_message = lsb.reveal("/home/tushar/Desktop/8s.png")
print(str(clear_message))