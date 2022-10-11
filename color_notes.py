from utils import *
import argparse
from os import listdir
from os.path import isfile, join
import os

def createParser():
    parser = argparse.ArgumentParser(description='Input parameters.')
    parser.add_argument ('-path', '--path2data', default="./dataset/train")
    
    return parser

if __name__ == "__main__" :

    parser = createParser()
    namespace = parser.parse_args()
    path = namespace.path2data

    dataset = [f"{path}/{file}" for file in listdir(path) if isfile(join(path, file))]

    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
 
    for i in range(len(dataset)):
        print(dataset[i])
        data_bgr = cv2.imread(dataset[i])
        data_bgr = color_notes(data_bgr)
        plt.figure(figsize=(20,20))
        plt.imshow(data_bgr)
        plt.savefig(f'{output_dir}/preprocessed_{i}.png')