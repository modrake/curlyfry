import sys
import subprocess


if (len(sys.argv) <= 2):
    print ("Usage: ")
    print ("python curlyfry <filename> <command-name>")

else:
    inFile = open (sys.argv[1], "r")

    for line in inFile:
        subprocess.call([sys.argv[2] + " " + line], shell=True)

    inFile.close()
