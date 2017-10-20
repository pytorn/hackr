

# coding: utf-8

# In[ ]:

#Searching and Downloading Google Images/Image Links

#Import Libraries

#coding: UTF-8

import time       #Importing the time library to check the time of code execution
import sys    #Importing the System Library
import os
import urllib2


def get_google_images(search_keyword=["Test"], keywords=["high resolution"]):
    t0 = time.time()   #start the timer

    #Download Image Links
    i= 0
    while i<len(search_keyword):
        items = []
        iteration = "Item no.: " + str(i+1) + " -->" + " Item name = " + str(search_keyword[i])
        print (iteration)
        print ("Evaluating...")
        search_keywords = search_keyword[i]
        search = search_keywords.replace(' ','%20')
        
         #make a search keyword  directory
        try:
            os.makedirs(search_keywords)
        except OSError, e:
            if e.errno != 17:
                raise   
            # time.sleep might help here
            pass
        
        j = 0
        while j<len(keywords):
            pure_keyword = keywords[j].replace(' ','%20')
            url = 'https://www.google.com/search?q=' + search + pure_keyword + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
            raw_html =  (download_page(url))
            # time.sleep(0.1)
            items = items + (_images_get_all_items(raw_html))
            j = j + 1
        #print ("Image Links = "+str(items))
        print ("Total Image Links = "+str(len(items)))
        print ("\n")


        #This allows you to write all the links into a test file. This text file will be created in the same directory as your code. You can comment out the below 3 lines to stop writing the output to the text file.
        info = open('output.txt', 'a')        #Open the text file called database.txt
        info.write(str(i) + ': ' + str(search_keyword[i-1]) + ": " + str(items) + "\n\n\n")         #Write the title of the page
        info.close()                            #Close the file

        t1 = time.time()    #stop the timer
        total_time = t1-t0   #Calculating the total time required to crawl, find and download all the links of 60,000 images
        print("Total time taken: "+str(total_time)+" Seconds")
        print ("Starting Download...")

        ## To save imges to the same directory
        # IN this saving process we are just skipping the URL if there is any error

        k=0
        errorCount=0
        while(k<len(items)):
            from urllib2 import Request,urlopen
            from urllib2 import URLError, HTTPError

            try:
                req = Request(items[k], headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
                response = urlopen(req,None,15)
                output_file = open(search_keywords+"/"+str(k+1)+".jpg",'wb')
                
                data = response.read()
                output_file.write(data)
                response.close();

                print("completed ====> "+str(k+1))

                k=k+1;

            except IOError:   #If there is any IOError

                errorCount+=1
                print("IOError on image "+str(k+1))
                k=k+1;

            except HTTPError as e:  #If there is any HTTPError

                errorCount+=1
                print("HTTPError"+str(k))
                k=k+1;
            except URLError as e:

                errorCount+=1
                print("URLError "+str(k))
                k=k+1;

        i = i+1

    print("\n")
    print("Everything downloaded!")
    print("\n"+str(errorCount)+" ----> total Errors")


#Downloading entire Web Document (Raw Page Content)
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            # time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items



if __name__ == "__main__":
    get_google_images(["Ball"], ["high resolution"])