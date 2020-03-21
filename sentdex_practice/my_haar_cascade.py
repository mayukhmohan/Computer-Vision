import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    pic_num = 1
    
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i,"neg/"+str(pic_num)+'.jpg')
            img = cv2.imread("neg/"+str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite("neg/"+str(pic_num)+'.jpg',resized_image)
            pic_num += 1
        
        except Exception as e:
            print(str(e))
    
    

def find_uglies():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type) + '/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print("gotacha!! You Ugly")
                        print(current_image_path)
                        os.remove(current_image_path)
                    
                    
                except Exception as e:
                    print(str(e))


# find_uglies()
                    
def create_pos_n_neg():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type + '/' + img +'\n'
                with open ('bg.txt','a') as f:
                    f.write(line)
                    
            elif file_type == 'pos':
                line = file_type + '/' + img +'1 0 0 50 50\n'
                with open ('info.dat','a') as f:
                    f.write(line)    
                    
       
'''
lec - 20
under opencv workspace we should have now bg.txt, neg, opencv, watch.jpg
data stores the haarcascade training data, info stores the positive images 
mkdir data, mkdir info
opencv_createsamples -img watch.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -num 1950

opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20
nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20 &

### CHECK TUTS ###
'''             
# create_pos_n_neg()                    
# find_uglies()
# store_raw_images()
