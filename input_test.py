#!/usr/local/bin/python3

import sys
import os


def ReadQueue():
	text=sys.stdin.readline().strip()
	return text


def menuSelect(menuOption):
	if menuOption == 'a':
		OptionResults= GetMemoryStatus()
	elif menuOption=='b':
		OptionResults= GetDirectoryContents()
	elif menuOption=='c':
		OptionResults=GetSystemVersion()
	else: OptionResults=''
	return OptionResults


def GetMemoryStatus():
	return os.popen('free').read().split('\n')


def GetDirectoryContents():
	return os.popen('ls -la').read().split('\n')


def GetSystemVersion():
	return [sys.version,]


def main():

	while True:
		print('Choose option A, B, or C:')
		Selection=ReadQueue()
		if Selection == 'x': break
		else: Results=menuSelect(Selection)
		if Results == '':
			print('Invalid Selection, Choose Again')
			continue
		else:
			for line in Results: print(line)


if __name__ == '__main__':
	try:
		main()
	
	finally:
		print("Please don't go...\n\tThe Drones need you...\n\t\tThey look up to you...")


