#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:00:13 2019

@author: loued
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor
still need to add
1.Serial commands
2.subject number DONE
3.trigger DONE 
4.would be nice to have functions
5.Add thank you slide DONE
6.Embed photo DONE
7.Instructions DONE


"""
import os
import numpy as np
import glob
import random
import pandas as pd
from psychopy import visual, core, event, sound, logging#import some libraries from PsychoPy
from psychopy.hardware import keyboard
from psychopy.visual import form as Form





def RelationshipAssessmentScale(outputPath, subjectNum, questPath):

    
    questformPath = '/Users/loued/Documents/PythonScripts/Experiment1_Scripts/QuestionnaireForms_PsychoPy/'
    os.chdir(questformPath)
    
        
    #Timing 
    clock = core.Clock()
    #Keyboard
    kb = keyboard.Keyboard()
    kb.clock.reset()
    
    #Screen
    mywin = visual.Window([900,900], [0, 0], monitor="testMonitor", units="height", allowStencil=True)
    
    x = pd.read_csv('RAS.csv')
    y = [x.T.to_dict()]
    
    #survey = Form.Form(mywin, items=y, size=(1.0, 0.7), pos=(0.0, 0.0))
    Instructions = visual.TextStim(win=mywin, text=("Les questions qui suivent portent sur votre satisfaction de couple (0 à 4).\nVeuillez répondre en cochant la case qui vous convient le mieux."),
    font='', height = 0.04, pos=(0, 0.85), units = 'norm', wrapWidth = 2)
    
    survey = Form.Form(mywin, items='RAS.csv', size=(1.0, 0.7), pos=(0.0, 0.0),  autoLog=True)
    
    
    while not survey.formComplete():
        Instructions.draw()
        survey.draw()
        mywin.flip()
    #    key = event.waitKeys()
        mouse = event.Mouse()
    #    keys = event.getKeys()
        buttons = mouse.getPressed()
        buttons, times = mouse.getPressed(getTime=True)
    #for i in range(1,30):
    #    keys = event.waitKeys()
    #    Resp[i] = str(keys[0])
    #    print(keys)
    #    
    #for i in range(1,30):
    #    rate = survey.getData()
    #    Resp[i] = str(keys[0])
    #    print(keys)
    
    x = survey.getData() 
       
    Questions = pd.DataFrame(list(x.get('questions')))
    Questions = Questions.rename (columns={0:'Questions'})
    
    Answers = pd.DataFrame(list(x.get('ratings')))
    Answers  = Answers.rename(columns={0:'Answers'})
    Answers = Answers.astype('int32')
    
    revScore = [3,6]
    Answers.iloc[revScore] =np.negative(Answers.iloc[revScore])
    
    Questions = pd.concat([Questions, Answers], axis = 1)
    
    Questions = Questions.append({'Questions' : 'Total' , 'Answers' : Questions.Answers.sum()} , ignore_index=True)
 
    os.chdir(questPath)
    Questions.to_csv(subjectNum + 'RAS_Scale_Response.csv')
    mywin.close()





