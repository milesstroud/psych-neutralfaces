# Neutral Faces Task

This project is a measure of affective coloring for psychological experiments. 
This task collects participant info, and then prompts participants to rate a neutral face on its likability, on a scale of 1 to 4. 60 faces display, and there is a 1.5 second time limit per face. 

## Getting Started

Simply retrieve all of the files present. You will need:
Normed_face_data.csv

* This is a csv of the norming data for each face file, from the Chicago Face Database.

matched_faces.csv

* This is a set of 60 faces separated into 15 sets of 4 grops. A, B, C, D. Faces composition is demographically accurate to the United States breakdown. Faces are matched on attractiveness, age, and image luminance. Groups are divided evenly by sex.

Neutral_Faces

* Folder with all neutral faces from the Chicago Face Database.*

faces_Practice

* Folder of faces for practice during the task. Note: these are not matched, you may want to pick matched faces that aren't used from the Neutral_Faces folder.

Faces_to_Folders.py

* Script used to separate matched faces into A, B, C, and D folders based on their group in matched_faces.csv

faces_A

faces_B

faces_C

faces_D

* Faces folder for each possible participant visit combination, pre and post session

Neutral_Faces_Task.py

* Task!

### Running the Task
To run the task, you may either:

1) Install the PsychoPy standalone GUI (https://www.psychopy.org/download.html)
From there, using the Coder view you can open the script from wherever it is located for you. 

2) Run it using Terminal.

### Prerequisites

Psychopy

```
pip install psychopy
```
os, csv, re, random

## Authors

* **Miles Stroud** - *University of Maryland* - (https://github.com/milesstroud)
*https://chicagofaces.org/default/*

## Acknowledgments

* Sasha Sommerfeldt, University of Wisconsin-Madison
