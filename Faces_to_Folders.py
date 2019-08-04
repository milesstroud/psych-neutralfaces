###########
#         #
# IMPORTS #
###########
#Author: Miles Stroud, University of Maryland
import re
import os
import csv
import shutil
import random
#Setting source file to be a single file containing all neutral faces
#Neutral Faces downloaded from https://chicagofaces.org/default/
src = 'Neutral Faces'
#Empty lists to sort files into that will make up individual sets 
faces_A = []
faces_B = []
faces_C = []
faces_D = []
for root, dirs, files in os.walk(src):
        #Every file in the "Neutral Faces" folder
        for file in files:
                path = os.path.join(root, file)
                facepic2 = file
                #Regex to find "AF-200" pattern in file names
                match = re.search(r'\w\w-\d\d\d', facepic2)
                if match:
                        matchedfile = match.group()
                        #Open CSV with neutral faces matched for attractiveness, age,
                        #and image luminance
                        #Available within this Github repository
                        with open('matched_faces.csv', mode='r') as csvFile:
                                reader = csv.reader(csvFile, delimiter=',')
                                for row in reader:
                                        #If "AF-200" matches the third column ('Target')
                                        #in the CSV, sort the file path into proper list
                                        if row[2] == matchedfile:
                                                print(row[1])
                                                #if second column (group: A, B, C, D) matches
                                                if row[1] == 'A':
                                                        faces_A.append(path)
                                                if row[1] == 'B':
                                                        faces_B.append(path)
                                                if row[1] == 'C':
                                                        faces_C.append(path)
                                                if row[1] =='D':
                                                        faces_D.append(path)
                                #Sort the faces from each face list into folders accordingly
                                for i in faces_A:
                                        dst = 'faces_A'
                                        shutil.copy(i, dst)
                                for i in faces_B:
                                        dst = 'faces_B'
                                        shutil.copy(i, dst)
                                for i in faces_C:
                                        dst = 'faces_C'
                                        shutil.copy(i, dst)
                                for i in faces_D:
                                        dst = 'faces_D'
                                        shutil.copy(i, dst)
        
