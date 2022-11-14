import io
#from pyexpat.errors import XML_ERROR_RECURSIVE_ENTITY_REF
from os import path

# defining preprocessors
change_to='IfNotPresent'

#change imagepullpolicy tag 
def addtag(content,i):
    s1=content[i+1].index('imagePullPolicy')
                
    content[i+1]=' '*s1+"imagePullPolicy: "+change_to+"\n"
    return content[i+1]

#insert imagepukpolicy tag
def inserttag(content,i):
    ab=' '*s+"imagePullPolicy: "+change_to+"\n"
    res=content.insert(i+1,ab)
    return res





# getting user input for the file to do changes to
abc=input("")

# getting the output file name where user wants to store the changes
output=input("")

# if input is in file format or not and if it exists 
while path.isfile(abc) == False:
    print("Cannot not find the file at "+str(abc)+'. Please check the directory path, spelling, and try again.: ')
    break;
    
file = open(abc)

# read the content of the file opened
content = file.readlines()
length=len(content)

#content browse 
for i in range(length):
    if "image:" in content[i]:
        ###split for path
        content[i]=content[i].rstrip()
        s=content[i].index('image:')
        path=content[i][s+6:]
        content[i]+='\n'
       

        # if image doesn't have a path
        if(path.count('.')<3):
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