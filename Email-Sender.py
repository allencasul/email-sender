import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import easygui
import smtplib


easygui.msgbox("\n\nEmail Sender - is a software that allow users to send emails powered by Artificial Intelligence. \n\n\nDate created: Dec. 5, 2021\n\nWritten in Python\nDeveloper: Allen Charls P. Casul\n\nEnjoy!\n\n\nFollow me on: \n\nhttps://www.facebook.com/miracle.928\nhttps://www.instagram.com/miracle.928\nhttps://www.youtube.com/channel/UCvmfCUT96uFTCHYIhqkLboQ/videos", title = "Email Sender v.1.0  by: Charls Allen Casul")


print(Fore.YELLOW + "\nWelcome to Email Sender :)")
print(Fore.YELLOW + "\nSend an email now!")

sender = input(str("\n\n\nEnter Your Email: "))
password = input(str("\nEnter Your Password: "))
reciever = input(str("\n\nWho do you want me to send? : "))
message = input(str("\nWrite Your Message: "))

if not sender:
	print(Fore.GREEN + "\n\nOops!, your email is required, please try again!")
if not password:
	print(Fore.GREEN + "\nPlease enter your authentic gmail password.")
if not reciever:
	print(Fore.GREEN + "\nReciever Email is required!")
if not message:
	print(Fore.GREEN + "\nYour Message is required!")

else:
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(sender, password)
	print(Fore.GREEN + '\n\nSending....')
	print(Fore.GREEN + "\n\nYour account has been successfully verified :)")
	server.sendmail(sender, reciever, message)
	print(Fore.YELLOW + "\nYour email message has been successfully sent to", reciever)
	server.quit()