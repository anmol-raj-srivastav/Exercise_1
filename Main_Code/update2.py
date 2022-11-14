# _*_ coding: utf-8 _*_
#
# Author = Anmol Raj Srivastav
# Copyright 2020 HPE 
# All rights reserved. Confidential

import io

from os import path

# defining preprocessors
change_to='IfNotPresent'
data_to_change='image:'

#change imagepullpolicy tag 
def addtag(content,i):
    spaces=content[i+1].index('imagePullPolicy')
                
    content[i+1]=' '*spaces+"imagePullPolicy: "+change_to+"\n"
    return content[i+1]

#insert imagepullpolicy tag
def inserttag(content,i):
    space=content[i].index(data_to_change)
    ab=' '*space+"imagePullPolicy: "+change_to+"\n"
    res=content.insert(i+1,ab)
    return res

def main(user_input, output):
    # if input is in file format or not and if it exists 
    while path.isfile(user_input) == False:
        print("Cannot not find the file at "+str(user_input)+'. Please check the directory path, spelling, and try again.: ')
        break
    # if output is not file format 
    while path.isfile(output) == False:
        print("Cannot not find the file at "+str(output)+'. Please check the directory path, spelling, and try again.: ')
        break
        
    file = open(user_input)

    # read the content of the file opened
    content = file.readlines()
    length=len(content)

    #content browse 
    for i in range(length):
        if data_to_change in content[i]:
            ###split for path
            content[i]=content[i].rstrip()
            s=content[i].index(data_to_change)
            filepath=content[i][s+6:]
            content[i]+='\n'
        

            # if image doesn't have a path
            if(filepath.count('.')<3):
                continue;
            
            # if image has a path but no imagepullPolicy or different imagepullpolicy other than IfNotPresent
            else:
                if "imagePullPolicy" in content[i+1]:
                    add=addtag(content,i)
                    

                    
                else:
                    add2=inserttag(content,i)
                    
                    
            
        else: 
            continue

    # opening and printing the output in a new YAML file
    file.close()
    ppp=''.join([i for i in content[0:]])
    f=open(output,'w+')
    f.write(ppp)

    f.close()

    fd=open(output,'r')
    co=fd.read()
    print(co)
    fd.close()


if __name__=="__main__":
    user_input=input()
    # getting the output file name where user wants to store the changes
    output=input()
    main(user_input, output)
    # getting user input for the file to do changes to


