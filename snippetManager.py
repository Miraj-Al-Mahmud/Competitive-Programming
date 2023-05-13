
# Snippet Manager for Competitive Programming (For Portable Setup Only but can be used for Installation as well)
# Date of Creation -> 28-10-2022


import pyperclip,json,os, webbrowser, pyautogui, shutil, colorama, random
from send2trash import send2trash
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#os.system('mode con: cols=80 lines=30')


RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE =  F"{Fore.RED}",F"{Fore.GREEN}",F"{Fore.YELLOW}",F"{Fore.BLUE}",F"{Fore.MAGENTA}",F"{Fore.CYAN}",F"{Fore.WHITE}"
LRED,LGREEN,LYELLOW,LBLUE,LMAGENTA,LCYAN,LWHITE =  F"{Fore.LIGHTRED_EX}",F"{Fore.LIGHTGREEN_EX}",F"{Fore.LIGHTYELLOW_EX}",F"{Fore.LIGHTBLUE_EX}",F"{Fore.LIGHTMAGENTA_EX}",F"{Fore.LIGHTCYAN_EX}",F"{Fore.LIGHTWHITE_EX}"


toWrite = [
				"<snippet>",
				"	<content><![CDATA[",
				"###",
				"]]></content>",
				"	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->",
				"	<!-- Optional: Set a scope to limit where the snippet will trigger -->",
				"	<scope>source.python</scope> -->",
				"</snippet>"
			]

sublimeDirectory = "D:\\Python\\CompetitiveProgramming\\Portable\\MAVERICK\\sublime_text.exe"
directory = "D:\\Python\\CompetitiveProgramming\\Portable\\MAVERICK\\Data\\Packages\\User\\Snippets\\"
listOfFiles = os.listdir(directory)
store = []

def stuck() -> None : print(f"\n\t",end=""); os.system('pause')

def appendAllNames() -> None:
	for l in listOfFiles: store.append(l)

def display() -> None:
	print(f"",end="\n")
	for idx,s in enumerate(store):
		name = s.rsplit(".sublime-snippet")
		print(f"{LGREEN}\t{idx}{LCYAN}\t{name[0]}",end="\n")

def select() -> None:
	print(f"",end="\n")
	print(f"{LYELLOW}\t>>>\t",end="")
	nameChoice = input()
	return nameChoice


def catagorize(nameChoice: str) -> str:
	if nameChoice.isdigit(): return 'digit'
	elif nameChoice.isalnum(): return 'alpha'
	else: return "nothing"




def writeToSnippet(givenNameByMaster: str) -> None:
	print(f"\tEnter the trigger string >>> ",end="")
	tabTrigger = input()
	appendString = f"	<tabTrigger>{tabTrigger}</tabTrigger> -->"
	toWrite[4] = appendString
	with open(givenNameByMaster, "w") as f:
		for t in toWrite: f.write(f"{t}\n")
	print(f"\n\t{LCYAN}Created Successfully !!!",end="\n")
	stuck()
	os.system(f"{sublimeDirectory} {givenNameByMaster}")
	import pyautogui
	pyautogui.typewrite(['down','down','del','del','del'])


def createAFile(nameChoice: str) -> None:
	givenNameByMaster = f"{directory}{nameChoice}.sublime-snippet"
	with open(givenNameByMaster, "w") as f: pass
	writeToSnippet(givenNameByMaster)



def editFile(nameChoice: int) -> None:
	givenNameByMaster = store[int(nameChoice)]
	print(f"\n\t{LCYAN}Opening !!!",end="\n")
	stuck()
	os.system(f"{sublimeDirectory} {directory}{givenNameByMaster}")	

def send(whichTypeOfFile : str, nameChoice: str) -> None:
	# can be number / digit / nothing - space - garbage
	if whichTypeOfFile == "nothing": print(f"Please enter the correct format !!!",end="\n")
	elif whichTypeOfFile == 'alpha': createAFile(nameChoice)
	elif whichTypeOfFile == 'digit':
		print(f"",end="\n")
		print(f"\t{LGREEN}1.\tOpen",end="\n")
		print(f"\t{LMAGENTA}2.\tDelete",end="\n")
		print(f"",end="\n")
		print(f"\t>>>\t",end="")
		x = int(input())
		if x == 1: editFile(nameChoice)
		elif x == 2: send2trash(f"{directory}{store[int(nameChoice)]}")


def main():
	os.system("cls")
	appendAllNames()
	display()
	nameChoice = select()
	whichTypeOfFile = catagorize(nameChoice)
	send(whichTypeOfFile, nameChoice)
	store.clear()
	# listOfFiles.clear()
	# exit(0)
	main()

	



if __name__ == "__main__": main()











