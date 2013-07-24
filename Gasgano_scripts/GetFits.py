#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, 2nd November 2011
#version 5.9.0


import sys, commands, os.path



#your desktop destination
TMP_FILE_DIR = '/tmp/'

if os.path.exists(TMP_FILE_DIR) == False:
    print 'Please set TMP_FILE_DIR i GetFits.py... exiting'
    sys.exit('Please set TMP_FILE_DIR i GetFits.py... exiting')

Files = {}

for i in range(1,len(sys.argv)):
    if i%2 == 1:
        if sys.argv[i+1] not in Files.keys():
            Files[sys.argv[i+1]] = [sys.argv[i]]
        else:
            Files[sys.argv[i+1]].append(sys.argv[i])

d="""'"""# string: '

SetFileCommand = ""

for Arm in ['UVB','VIS','NIR', 'UNCLAS']:
    for key in Files.keys():
        if Arm not in key:
            continue

        SetFileCommand += Arm+".SetFiles("+d+key + d+',['
        FirstFile=True
            
        for File in Files[key]:
            if FirstFile == True:
                FirstFile = False 
            else:
                SetFileCommand += ','
            SetFileCommand += d + File +d
        
        SetFileCommand += '])\n\n'



print SetFileCommand


OutFileName = TMP_FILE_DIR + 'GetFitsOutput.txt'
f = file(OutFileName,'w')
f.write(SetFileCommand)
f.close()


commands.getoutput('zenity --text-info --filename='+OutFileName+' --height=700 --width=1200 --editable')
#    commands.getoutput('zenity --text-info --filename='+OutFileName+' --height=700 --width=1200 --editable')
