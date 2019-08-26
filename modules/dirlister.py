import os
def run(**args):

	print(" [+] In DirLister Modules. ")
	files = os.listdir(".")

	return str(files)


