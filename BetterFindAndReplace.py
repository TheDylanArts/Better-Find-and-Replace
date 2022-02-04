import json
#Take inputs
fileToCopy="Test_item_frame.json"#input("Enter the file name of the file you want to copy: ")
fileToOutput="Tested_item_frame.json"#input("Enter the file name of the file you would like to output: ")
while fileToOutput==fileToCopy:
    print("The file output you input is the same as the file you input!")
    fileToOutput=input("Enter the file name of the file you would like to output: ")

#Open Files
fileIn=open(fileToCopy,"r")
fileOut=open(fileToOutput,"w")

#Initiate variables
count=1

#Write read input file line by line and print to output file
for line in fileIn:
    fileOut.write(str(line))
    count+=1

#Close both files!
fileIn.close()
fileOut.close()

#Show file output is done
print("Done!")
