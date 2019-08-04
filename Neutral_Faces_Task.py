#We used demographics data gathered from
#https://www.census.gov/quickfacts/fact/table/US/PST045218 to match faces accurately
#Author: Miles Stroud, University of Maryland College Park
from psychopy import visual, core, event, gui, clock
import os
import csv
import re
import random
#Function to display each individual face picture, must pass a facepic file to initiate
def show_face(facepic):
        img = visual.ImageStim(win=win, image=facepic, units="pix", size=[600,400], interpolate=True)
        img.draw()
        win.flip()
#Create slide with instructions text, press "Space" button to progress
def show_instructions():
        instructions.draw()
        ratingScale.draw()
        win.flip()
        event.waitKeys(keyList=['space'])
#Display "practice" variable, text stim that holds text for pre-practice slide
def show_practice_instructions():
        practice.draw()
        win.flip()
        event.waitKeys(keyList=['space'])
#Display the rating scale as well as accompanying text above, displays until participant response
def show_ratingscale():
        while ratingScale.noResponse:
                #while there is no response, draw the text above rating scale, rating scale, and display slide
                textStim.draw()
                ratingScale.draw()
                win.flip()
                if event.getKeys(['escape']):
                        core.quit()
#Complete 5 practice trials 
def run_practice_trials():
    p=0
    while p < 5:
            src ="faces_Practice"
            for root, dirs, files in os.walk(src):
                    for file in files:
                            path = os.path.join(root, file)
                            facepic2 = file
                            facepic = path
                            timer = core.CountdownTimer(1.5)
                            x, y = ratingScale.win.size
                            img = visual.ImageStim(win=win, image=facepic, units="pix", size=[600,400], interpolate=True,pos=[0, y//7])
                            while ratingScale.noResponse:
                                    textStim.draw()
                                    img.draw()
                                    ratingScale.draw()
                                    win.flip()
                                    if event.getKeys(['escape']):
                                            core.quit()
                                    if timer.getTime() <= 0:
                                            break
                            p+=1
                            ratingScale.reset()
                            if p == 5:
                                    break
#Function to activate the slide between practice and real task
def transition_slide():
        transition.draw()
        win.flip()
        event.waitKeys(keyList=['space'])
#THE TASK, runs for 60 faces, pipes data to a csv in "data" folder 
def run_trials():
    n=0
    trialnumber = 1
    while n < 60:
            if set_label == 'A':
                    src = 'faces_A'
            if set_label == 'B':
                    src = 'faces_B'
            if set_label == 'C':
                    src = 'faces_C'
            if set_label == 'D':
                    src = 'faces_D'
            for root, dirs, files in os.walk(src):
                    for file in files:
                            filename = random.choice(os.listdir(src))
                            path = os.path.join(root, filename)
                            if filename == '.DS_Store':
                                    break
                            facepic2 = filename
                            if (facepic2 in random_faces):
                                    break
                            random_faces.append(facepic2)
                            facepic = path
                            x, y = ratingScale.win.size
                            img = visual.ImageStim(win=win, image=facepic, units="pix", size=[600,400], interpolate=True,pos=[0, y//7])
                            timer = core.CountdownTimer(1.5)
                            while ratingScale.noResponse:
                                    textStim.draw()
                                    img.draw()
                                    ratingScale.draw()
                                    win.flip()
                                    if event.getKeys(['escape']):
                                            core.quit()
                                    if timer.getTime() <= 0:
                                            break
                            decisionTime = ratingScale.getRT()
                            rating = ratingScale.getRating()
                            if timer.getTime() <= 0:
                                    rating = ' '
                            data.append(rating)
                            data.append(decisionTime)
                            print(data)
                            #Regex expression for finding race/sex + photo number (AF-200)
                            match = re.search(r'\w\w-\d\d\d', facepic2)
                            #Match = RACESEX--PHOTO##
                            if match:
                                    matchedfile = match.group()
                            #Opening normed face CSV
                            with open('Normed_face_data.csv', mode='rU') as csvnormed:
                                    reader = csv.reader(csvnormed, delimiter=',')
                                    for row in reader:
                                            if row[0] == matchedfile:
                                                    matchedrow = row
                                            else:
                                                    continue
                            #Defining the row to be added --> [subjID, timep, TSSTsession, trialnumber, rating, reaction time, filename, SUBJID_TIMEP_PRE/POST, attractiveness, threatening, trustworthiness
                            row = [ok_data[0], ok_data[1], ok_data[2], trialnumber, rating, decisionTime, facepic2]
                            for i in matchedrow:
                                    row.append(i)
                            #Opening individual's participant csv
                            writer.writerow(row)
                            #Add 1 to trialnumber variable and initiator (n)
                            trialnumber+=1
                            n+=1
                            #Reset the rating scale for each participant, within loop
                            ratingScale.reset()
                            #Break entire loop at 50, conclusion
                            if n == 60:
                                    break
#Conclusion, waits until researcher presses "Space" to close window
def conclusion_slide():
        conclusion_text = visual.TextStim(win, text='The task is now complete. A researcher will be with you shortly.')
        conclusion_text.draw()
        win.flip()
        event.waitKeys(keyList=['space'])
#Initial dialogue box to get participant information
myDlg = gui.Dlg(title="Participant Information")
myDlg.addText("Subject Information")
myDlg.addField(label='Subject ID')
myDlg.addField(label='Timepoint:', choices=["T1", "T2"])
myDlg.addField(label='Pre or Post TSST:', choices=["Pre", "Post"])
myDlg.addField(label='Set:', choices=['A', 'B', 'C', 'D'])
ok_data = myDlg.show()
#ok_data contains a list with the responses, in order (subject ID, timepoint, pre/post TSST)
subjID = ok_data[0]
print(subjID)
timep = ok_data[1]
TSSTsession = ok_data[2]
set_label = ok_data[3]
print(timep)
print(TSSTsession)
#Creating Window that will contain instructions and pictures
label = ['1', '2', '3', '4']
scales = "1= Not at all, 4=Very much"
#Creating Window that will contain instructions and pictures
win = visual.Window(fullscr=True, units="pix")
ratingScale = visual.RatingScale(win, scale=scales, low=1, high=4, precision=1, labels=label, tickMarks=label, markerStart=1, singleClick=True, showAccept=False, mouseOnly=True, pos=[0,-200])
#Instructions page text
instructions = visual.TextStim(win, text="In this activity, you will see a series of faces. An image and a rating scale will appear on the screen. After viewing the image, decide how much you like or dislike each face by choosing a point on the rating scale. Rate how much you would like or dislike this person if you saw them in real life. Don't overthink it. Just give your honest gut response.")
#Practice page text
practice = visual.TextStim(win, text="Now you will complete 5 practice faces to confirm you understand the task.")
#Text stimulus to display above rating scale for each picture
textStim = visual.TextStim(win, text="How much do you like this person?", pos=(0.0, 0.0), color="Black")
#Rating scale variables
label = ['1', '2', '3', '4']
scales = "1= Not at all, 4=Very much"
#Rating scale variable on a scale of 1 to 4
ratingScale = visual.RatingScale(win, scale=scales, low=1, high=4, precision=1, labels=label, tickMarks=label, markerStart=1, singleClick=True, showAccept=False, mouseOnly=True, pos=[0,-200])                      
#Slide between practice and the actual task
transition = visual.TextStim(win, text="Remember, don't spend a lot of time thinking about the rating. Just give your honest gut response. Now, you will begin the actual task.")
data =[]
subid_string = str(subjID)
d=0
#Write the header for the participant's CSV data file
header = ['SubjID', 'Timepoint', 'TSST Session', 'TrialNumber', 'Rating', 'ReactionTime', 'Filename', 'Face', 'Race', 'Sex', 'Age', 'NumberofRaters', 'Female_prop', 'Male_prop', 'Asian_prop', 'Black_prop', 'Latino_prop', 'Multi_prop', 'Other_prop', 'White_prop', 'Afraid', 'Angry', 'Attractive', 'Babyface', 'Disgusted', 'Dominant', 'Feminine', 'Happy', 'Masculine', 'Prototypic', 'Sad', 'Suitability', 'Surprised', 'Threatening', 'Trusthworthy', 'Unusual', 'Luminance_median', 'Nose_Width', 'Nose_Length', 'Lip_Thickness', 'Face_Length', 'R_Eye_H', 'L_Eye_H', 'Avg_Eye_Height', 'R_Eye_W', 'L_Eye_W', 'Avg_Eye_Width', 'Face_Width_Cheeks', 'Face_Width_Mouth', 'Forehead', 'Pupil_Top_R', 'Pupil_Top_L', 'Asymmetry_pupil_top', 'Pupil_Lip_R', 'Pupil_Lip_L', 'Asymmetry_pupil_lip', 'BottomLip_Chin', 'Midcheek_Chin_R', 'Midcheek_Chin_L', 'Cheeks_avg', 'Midbrow_Hairline_R', 'Midbrow_Hairline_L', 'Faceshape', 'Heartshapeness', 'Noseshape', 'LipFullness', 'EyeShape', 'EyeSize', 'UpperHeadLength', 'MidfaceLength', 'ChinLength', 'ForeheadHeight', 'CheekboneHeight', 'CheekboneProminence', 'FaceRoundness', 'fWHR']
#Store the CSV in the "data" folder on the computer
CSVdir = 'data'
#Creating the path to the 'data' folder and titling each csv according to the participant information entered
datapath = os.path.join(CSVdir, '%s_%s_%s.csv' % (subid_string, timep, TSSTsession))
datacsv = open(datapath, 'a')
writer = csv.writer(datacsv)
writer.writerow(header)
#To prevent random faces from showing more than once, append each file to empty list
random_faces = []

show_instructions()
show_practice_instructions()
run_practice_trials()
transition_slide()
run_trials()
conclusion_slide()
