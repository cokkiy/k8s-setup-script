import os

with open('./allimages.txt', 'r') as f:
    l=f.readline()
    while l:
        if "image:" in l:
            index=l.find("image:")
            image=l[index+6:]
            image=image.strip()
            if image:
                image=image.replace('$ARCH', 'amd64')
                #image=image[:-1]                
                #print(image)
                if 'gcr.io' in image:
                    index=image.find('/')
                    remain=image[index:]
                    if remain.startswith('/google_containers') or remain.startswith('/knative-releases'):
                        remain='gcr.azk8s.cn'+remain
                    else:
                        remain='gcr.azk8s.cn/google_containers'+remain
                          
                    rindex=image.rfind("/")
                    name=image[rindex+1:]
                    name=name.replace('@', '_')
                    name=name.replace(':', '.')+".tar"
                    if '@' in image:
                        atIndex=image.rfind('@')                        
                        image=image[:atIndex]
                    cmd="./gcr.sh "+remain+" "+image+" "+name
                    print("Execute: "+cmd)
                    os.system(cmd)                                       
                else:                   
                    rindex=image.rfind("/")
                    name=image[rindex+1:]
                    name=name.replace('@', '_')
                    name=name.replace(':', '.')+".tar"
                    cmd="./other.sh "+image+" "+name
                    print("Execute: "+cmd)
                    os.system(cmd) 
        l=f.readline()
    