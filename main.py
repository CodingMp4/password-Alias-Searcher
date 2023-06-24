#first load the IDE
#then add your imports
import random
from colorama import Fore, Back, Style
import requests
import time

#put the independency 
#this includes lower letters and others
lower = "abcdefghijk" "coding"
upper = "ABCDEFGHIJK" "coding"
words = "help" "ear" "dies" "minecratf" "yes" "no" "lol"
numbers = "1234567890"

#combines everything
all = lower + upper + words + numbers
#length of the combination
length = 6

#makes thw output
password = "".join(random.sample(all, length))

#prints "generated"
print (Fore.GREEN + "[+] generated!                                                                                    ") 


#prints the password
print ("[+] your password = " + password)

#prints the thank you message
print(Fore.GREEN + '                                                            [+] thanks for using!')
#coded by coding.mp4 on yt

print ("                                                            [+] do you want to exit? Y for Yes and N for No.                                                       ")

option = input (" [+] option: ")
if  option == "Y":
 exit()
 
elif  option == "N":
  print("""

  _____     __       _      _  __  
 / ___/_ __/ /  ____(_)__  | |/_/  
/ /__/ // / _ \/ __/ / _ \_>  <    
\___/\_, /_.__/_/ /_/\___/_/|_|    
    /___/                          

    """)

username = input("[+] Enter Alias: ")
print("[+] Finding",Style.BRIGHT+Fore.YELLOW+username+Style.RESET_ALL+"'s accounts")

def main(username):
    sites = ['https://www.facebook.com/',
            'https://www.instagram.com/',
            'https://www.youtube.com/@',
            'https://www.twitter.com/']
            
    for i in sites:
        r = requests.get(i+"{}".format(username))
        if r.status_code == 200:
            print("[+] "+i+"{} --> ".format(username) + Fore.GREEN + "Valid"+ Style.RESET_ALL)
        else:
            print("[+] "+i+"{} --> ".format(username) + Fore.RED + "Not Valid"+ Style.RESET_ALL)

main(username) 

time.sleep (5)