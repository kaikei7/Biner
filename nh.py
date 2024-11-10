import requests
from bs4 import BeautifulSoup as bs
import shutil
from bs4 import *
import requests
import os
from zipfile import ZipFile
count = 0
# CREATE FOLDER
def folder_create(images,nm):
    
 
    # image downloading start
    download_images(images, nm)
    
 
 
# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):
   
    # initial count is zero
    
 
    # print total images found in URL
    print(f"Total {len(images)} Image Found!")
 
    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            # From image tag ,Fetch image Source URL
 
                        # 1.data-srcset
                        # 2.data-src
                        # 3.data-fallback-src
                        # 4.src
 
            # Here we will use exception handling
 
            # first we will search for "data-srcset" in img tag
            try:
                # In image tag ,searching for "data-srcset"
                image_link = image["data-srcset"]
              
                 
            # then we will search for "data-src" in img
            # tag and so on..
            except:
                try:
                    # In image tag ,searching for "data-src"
                    image_link = image["data-src"]
                except:
                    try:
                        # In image tag ,searching for "data-fallback-src"
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            # In image tag ,searching for "src"
                            image_link = image["src"]
                            
 
                        # if no Source URL found
                        except:
                            pass
 
            # After getting Image Source URL
            # We will try to get the content of image
            try:
                r = requests.get(image_link).content 
                
                try:
 
                    # possibility of decode
                    r = str(r, 'utf-8')
 
                except UnicodeDecodeError:

                    # After checking above condition, Image Download start
                    global count
                    count += 1
                    with open(f"{folder_name}/images{count}.jpg", "wb+") as f:
                        f.write(r)
 
                    # counting number of image downloaded
                    
            except Exception as e:
                print(e)
 
        # There might be possible, that all
        # images not download
        # if all images download
        if count == len(images):
            print("All Images Downloaded!")
             
        # if all images not download
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")
 
# MAIN FUNCTION START
def main(url,code):
   
    # content of URL
    r = requests.get(url)
 
    # Parse HTML Code
    soup = BeautifulSoup(r.text, 'html.parser')
 
    # find all images in URL
    images = soup.findAll('img')
    
    # Call folder creatr = requests.get(image_link).contente function
    folder_create(images,code)
    
 
 
# take url
code = str(input("code:"))
url = f"https://nhentai.net/g/{code}"
r = requests.get(url)
    # Parse HTML Code
soup = BeautifulSoup(r.text, 'html.parser')
x1 = soup.text.find("Pages")
x2= soup.text.find("Uploaded")
x = int(soup.text[x1+6:x2])
print(x)
if not code in os.listdir():
  os.mkdir(code)
for i in range(x):
  main(f"{url}/{i+1}",code)
with ZipFile(f"{code}.zip", "w") as zip:
 for x in os.listdir(code):
   zip.write(os.path.join(code,x))
shutil.rmtree(code)
  #CALL MAIN FUNCTION