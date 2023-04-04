import csv
import cv2
import numpy as np

def read_file(filepath:str,columns:list):
    try:
        with open(filepath,'r') as file :
            reader = csv.reader(file)
            data = [i for i in reader]
            ret = np.array(data,dtype=float)[:,columns]
            return ret
    except Exception as e:
        print(e)

def reshape_to_image(data:list,height:int,width:int):
    data = np.reshape(data,(height,width,3))
    return data
    
def write_image(data:list,imagepath:str):
    data*=255.0/data.max() #normalize data
    cv2.imwrite(imagepath,data)

def main(ask_user:bool=True,csvfile:str='',columns:list=[],imagepath:str='',size:list=[]):
    if ask_user:
        csvfile = input('CSV File Path')
        columns = list(eval(input('Columns to assign RGB as a list in this order')))
        imagepath = input('Image Path')
        size = eval(input('Image Size HeightxWidth'))

    data = read_file(csvfile,columns)
    data = reshape_to_image(data,*size)
    write_image(data,imagepath)


if __name__=='__main__':
    main()