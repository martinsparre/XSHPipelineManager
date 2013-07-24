#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, 2nd November 2011
#version 5.9.0

import commands
import os.path
import pickle
import sys
import pyfits

#some standard esorex-options:
ESOREX_EXE = 'esorex'
ESOREX_OPTIONS ='--suppress-prefix=FALSE' #'--suppress-prefix=FALSE' is necessary. If it is removed the output-products will not be detected
RECIPE_OPTIONS = ''#'--keep-temp=yes' #This is optional (for quality checks...)


#Use this on (some) DARK-computers:
#ESOREX_OPTIONS += #""" --recipe-dir='/local/opt/pipe/pipe/lib/esopipes-plugins/xsh-1.2.2'"""

def SaveToRestartFile(PickleFile,Object):
    f=open(PickleFile, 'wb')
    pickle.dump(Object,f)
    f.close()

def LoadRestartFile(PickleFile):
    f=open(PickleFile, 'rb')
    Object = pickle.load(f)
    f.close()
    return Object


def GetFiles(InputFiles, BinX, BinY, ReadOut):
    """
    GetFiles(InputFiles, BinX, BinY, ReadOut)

    InputFiles: a list with files with different binnings and readouts
    BinX: the correct X-binning (as a string)
    BinY: the correct Y-binning (as a string)
    ReadOut: the correct readout

    Return Value: a list with the files with correct Binning and readout"""

    List = []

    if BinX == 'DoesntMatter' and BinY == 'DoesntMatter' and ReadOut == 'DoesntMatter':
        for F in InputFiles:#append all files
            List.append(F)

    elif BinX == 'DoesntMatter' and BinY == 'DoesntMatter' and ReadOut != 'DoesntMatter':
        for F in InputFiles:
            if ReadOut in F.GetReadOut():#append files with correct readout
                List.append(F)

    elif BinX != 'DoesntMatter' and BinY != 'DoesntMatter' and ReadOut == 'DoesntMatter':
        for F in InputFiles:
            if(BinX in F.GetBinX() and BinY in F.GetBinY()):#append files with correct binning
                List.append(F)

    elif BinX != 'DoesntMatter' and BinY != 'DoesntMatter' and ReadOut != 'DoesntMatter':
        for F in InputFiles:
            if BinX in F.GetBinX() and BinY in F.GetBinY() and ReadOut in F.GetReadOut():#append files with correct binning and readout
                List.append(F)

    else:
        print "Something is wrong... 329846fsd"#this is not supposed to happen

    return List


#The Recipe class
class Recipe:
    """
    The Recipe class contain the information necessary to execute the esorex-recipes.

    Recipe(RecipeName,LoopOption)

    RecipeName: Name of the esorex-recipe. e.g. xsh_mbias
    LoopOption: '' or 'LoopOverBinningAndReadOut' (for bias, dark and flat).
    """
    def __init__(self,Manager, EsorexRecipeName, RecipeName, BinX_match, BinY_match, ReadOut_match):
        self.EsorexRecipeName = EsorexRecipeName
        self.RecipeName = RecipeName
        self.InputTags = []
        self.BinX_match = BinX_match
        self.BinY_match = BinY_match
        self.ReadOut_match = ReadOut_match
        self.RecipeOptions = ''
        self.EsorexOptions = ''
        self.DisableEsorex = False
        self.StopAfterRecipe = False
        self.Arm = ''
        self.Manager = Manager

    def SetDisableEsorex(self, Boolean):
        self.DisableEsorex = Boolean

    def GetDisableEsorex(self):
        return self.DisableEsorex

    def SetStopAfterRecipe(self, Boolean):
        self.StopAfterRecipe = Boolean

    def GetStopAfterRecipe(self):
        return self.StopAfterRecipe


    def AddRecipeOptions(self, Option):
        self.RecipeOptions = Option + self.RecipeOptions

    def SetRecipeOptionsA(self, Option):#"A" in the function name is used to distinguish from a function in the Pipeline-manager-class
        self.RecipeOptions = Option

    def SetEsorexOptionsA(self, Option):#"A" in the function name is used to distinguish from a function in the Pipeline-manager-class
        self.EsorexOptions = Option

    def GetRecipeOptions(self):#"A" in the function name is used to distinguish from a function in the Pipeline-manager-class
        return self.RecipeOptions

    def GetEsorexOptions(self):#"A" in the function name is used to distinguish from a function in the Pipeline-manager-class
        return self.EsorexOptions

    def DeclareInputTag(self, InputTagName, Nfiles, Binning, ReadOut):
        if self.InputTags == []:
            Type = 'RAW'
        else:
            Type = ''

        
        self.InputTags.append(InputTag(InputTagName, Nfiles, Binning, ReadOut,Type))

    def GetRecipeName(self):
        return self.RecipeName

    def GetEsorexRecipeName(self):
        return self.EsorexRecipeName

    def GetBinX_match(self):
        return self.BinX_match

    def GetBinY_match(self):
        return self.BinY_match

    def GetReadOut_match(self):
        return self.ReadOut_match

    def GetInputTags(self):
        return self.InputTags

    def GetArm(self):
        return self.Arm

    def Execute(self,Files):
        #set Arm:
        if 'UVB' in Files.keys()[0]:
            Arm = 'UVB'
        elif 'VIS' in Files.keys()[0]:
            Arm = 'VIS'
        elif 'NIR' in Files.keys()[0]:
            Arm = 'NIR'
        else:
            Arm = 'Arm'
            print '\tcouldnt determine ARM. Files.keys()[0]=', Files.keys()[0]
            
        self.Arm = Arm

        #Determine Set BinX_match, BinY_match, ReadOut_match
        if self.GetBinX_match() == '' and self.GetBinY_match() == '' and self.GetReadOut_match() == '':
            for Tag in self.GetInputTags():
                if Tag.GetType() == 'RAW' or Tag.GetType() == 'raw':
                    if Tag.GetTagName() not in Files.keys():
                        print "\t --Error: Tag: "+Tag.GetTagName()+" not defined\n\n"
                        return None
                    BinX_match = Files[Tag.GetTagName()][0].GetBinX()
                    BinY_match = Files[Tag.GetTagName()][0].GetBinY()
                    ReadOut_match = Files[Tag.GetTagName()][0].GetReadOut()
        elif self.GetBinX_match() != '' and self.GetBinY_match() != '' and self.GetReadOut_match() != '':
            BinX_match = self.GetBinX_match()
            BinY_match = self.GetBinY_match()
            ReadOut_match = self.GetReadOut_match()
            
        else:
            print '\tSyntax Error: 98w734bkfs'

        CurrentSOFName = self.Manager.GetOutputDir() + self.GetRecipeName()+'_'+Arm+'.sof'
        CurrentSOF = open( CurrentSOFName ,'w')

        #Determine binning and readout, and write Tag to sof-file
        RunEsorex = True
        for Tag in self.GetInputTags():

            #find readout for the current tag
            if 'match' in Tag.GetReadOut():
                CurrentReadOut = ReadOut_match
            elif '400k' == Tag.GetReadOut():
                CurrentReadOut = '400k'
            elif '100k' == Tag.GetReadOut():
                CurrentReadOut = '100k'
            elif '-' in Tag.GetReadOut():
                CurrentReadOut = 'DoesntMatter'
            elif '100k/400k' == Tag.GetReadOut() or '100/400k' == Tag.GetReadOut() or 'any'==Tag.GetReadOut():
                if Tag.GetType() == 'raw' or Tag.GetType() == 'RAW':
                    CurrentReadOut = ReadOut_match
                else:
                    CurrentReadOut = 'DoesntMatter'
            else:
                print '\t Warning: could not determine CurrentReadOut 12987347'
                print '\t'+Tag.GetReadOut()+" should be match, any,100k,400k.100/400k or 100k/400k"

            #find binning for the current tag
            if 'match' in Tag.GetBinning():
                CurrentBinX = BinX_match
                CurrentBinY = BinY_match
            elif '1x1' in Tag.GetBinning():
                CurrentBinX = '1'
                CurrentBinY = '1'
            elif '1x2' in Tag.GetBinning():
                CurrentBinX = '1'
                CurrentBinY = '2'
            elif '2x1' in Tag.GetBinning():
                CurrentBinX = '2'
                CurrentBinY = '1'
                print '\tWarning: Binning 2x1 is not allowed. 6578694dsfsds'
            elif '2x2' in Tag.GetBinning():
                CurrentBinX = '2'
                CurrentBinY = '2'
            elif 'any' in Tag.GetBinning():
                if Tag.GetType() == 'raw' or Tag.GetType() == 'RAW':
                    CurrentBinX = BinX_match
                    CurrentBinY = BinY_match
                else:
                    CurrentBinX = 'DoesntMatter'
                    CurrentBinY = 'DoesntMatter'
            elif '-' in Tag.GetBinning():
                    CurrentBinX = 'DoesntMatter'
                    CurrentBinY = 'DoesntMatter'
            else:
                print '\twarning: could not determine binning. suylpoih9'

            if Tag.GetTagName() not in Files.keys():
                if '?' not in Tag.GetNFiles():
                    print '\n\tA necessary file is missing for tag '+Tag.GetTagName() + '. Esorex disabled.'
                    RunEsorex = False
                else:
                    print '\n\tAn optional file is missing for tag '+Tag.GetTagName() + '.\n'
                continue

            if len(Files[Tag.GetTagName()])==0:
                if '?' not in Tag.GetNFiles():
                    print '\n\tA necessary file is missing for tag '+Tag.GetTagName() + '. Esorex disabled.'
                    RunEsorex = False
                else:
                    print '\n\tAn optional file is missing for tag '+Tag.GetTagName() + '.\n' 
                continue

            #write to sof-file:
            TempFileList = GetFiles(Files[Tag.GetTagName()], CurrentBinX, CurrentBinY, CurrentReadOut)
            if len(TempFileList) == 0 and '?' not in Tag.GetNFiles():
                print '\n\tA necessary file is missing for tag '+Tag.GetTagName() + '. Esorex disabled.'
                RunEsorex = False
            else:
                FilesWritten = 0
                for F in TempFileList:
                    if  FilesWritten < Tag.GetFilesNeeded():
                        CurrentSOF.write(F.GetFitsName()+'\t'+Tag.GetTagName()+'\n')
                        FilesWritten += 1
        CurrentSOF.close()

        print '\tSOF-file '+CurrentSOFName+' created.'
        #execute esorex if all necessary files are available:

        if RunEsorex == False and self.GetDisableEsorex() == False:
            print "\tesorex will not be executed for this recipe, since some necessary files are missing."
            if self.GetEsorexRecipeName() =='xsh_mbias' or self.GetEsorexRecipeName() =='xsh_mflat':
                print '\tDont worry about the warning above if you dont need '+self.GetEsorexRecipeName() + ' to be executed for binning '+ self.GetBinX_match() +'x'+self.GetBinY_match() + ' and readout ' + self.GetReadOut_match() +'.\n'
                print '\tIf you need this recipe to be executed the missing files should be provided (use the SetFiles(...) function).'
                
        if self.GetDisableEsorex() == True:
            print "\tYou have disabled esorex for this recipe. Esorex will not be executed."
            RunEsorex = False


        if RunEsorex == True:
            EsorexCommand = ESOREX_EXE + ' ' + ESOREX_OPTIONS + ' ' + self.GetEsorexOptions() + ' ' + self.GetEsorexRecipeName() + ' ' + RECIPE_OPTIONS + ' ' + self.GetRecipeOptions() + ' ' + CurrentSOFName
            print '\tExecuting: '+EsorexCommand
            commands.getoutput(EsorexCommand)
            print "\tEsorex completed.\n"

            #rename and insert into dictionary
            Output_string=commands.getoutput('ls out_*.fits')
            if 'ls:' in Output_string:
                print '\tError: No output-files from recipe. Recipe ('+self.GetRecipeName()+') crashed.\n\n'
                Output_string = ''
            else:
                print '\tRenaming Outputfiles:'

            for OutputFile in Output_string.split():
                OutputFileHeader =  pyfits.getheader(OutputFile)
                if 'ESO PRO CATG' in OutputFileHeader.keys():
                    NewSofTag = OutputFileHeader['ESO PRO CATG']
                else:
                    print 'Something wrong when determining ESO PRO CATG... u8q3209ejncvsd'
                    sys.exit()
                
                FitsFileName = self.Manager.GetOutputDir() + self.GetRecipeName() +'_' + NewSofTag + '_' + Arm + '_' + BinX_match + 'x' + BinY_match + '_' + ReadOut_match + '.fits'
                commands.getoutput('mv '+OutputFile+' '+FitsFileName)

                print '\t'+OutputFile+' -> '+FitsFileName
                
                #put the fits-file into the Files-dictionary
                if NewSofTag not in Files.keys():
                    Files[NewSofTag] = [TFile(FitsFileName,NewSofTag)]
                else:
                    #the file is inserted at index 0, so it will replace the old file in case of '*'
                    Files[NewSofTag].insert(0,TFile(FitsFileName,NewSofTag))

                print '\tFile '+FitsFileName+' with tag '+ NewSofTag + ' added.'
            if os.path.exists('esorex.log') == True:
                commands.getoutput('mv esorex.log ' + self.Manager.GetOutputDir() + 'esorex_'+self.GetRecipeName()+'_'+Arm+'.log')
                print '\n\tEsorex-log saved: '+self.Manager.GetOutputDir() +'esorex_'+self.GetRecipeName()+'_'+Arm+'.log'
            commands.getoutput('mv *.paf ' + self.Manager.GetOutputDir() + '/.')
        return Files


#The Pipeline Manager class
class PipelineManager:
    def __init__(self):
        self.Files = {} #A dictionary with all  files (class "TFile")
        self.Recipes = {} #A dictionary containing all recipes
        self.RecipeOrder = []#A list with the order in which the recipes has to be run
        self.CurrentRecipe = ''#Name of current Recipe (used to start from restart file)
        self.OutputDir = 'Output/'

    def SetFiles(self, SofTag, Files):
        List = []
        for i in Files:
            List.append(TFile(i,SofTag))
            if SofTag.rstrip('_ON').rstrip('_OFF')[-3:] != List[-1].GetARM() and List[-1].GetARM() != '':
                sys.exit(SofTag+ ': Inconsistent arm in SetFiles(). File is from '+ List[-1].GetARM() + '-arm. Will now exit...')

        if SofTag in self.Files:
            print 'Warning: File(s) with Tag '+SofTag+' is already defined. Old tag replaced.'

        self.Files[SofTag] = List

    def DeclareNewRecipe(self, EsorexRecipeName, RecipeName = '', BinX_match  = '', BinY_match  = '', ReadOut_match = ''):
        if RecipeName=='':
            RecipeName = EsorexRecipeName

        if RecipeName in self.Recipes:
            print 'Warning: Recipe with name '+RecipeName+' is already defined. Old recipe replaced.'

        self.Recipes[RecipeName] = Recipe(self, EsorexRecipeName, RecipeName, BinX_match, BinY_match, ReadOut_match)


    def DeclareRecipeInputTag(self, RecipeName, InputTagName, Nfiles, Binning, ReadOut):
        self.Recipes[RecipeName].DeclareInputTag(InputTagName, Nfiles, Binning, ReadOut)


    def SetOutputDir(self, OutputDir):
        OutputDir = OutputDir.rstrip('//')+'/'
        self.OutputDir = OutputDir

    def GetOutputDir(self):
        return self.OutputDir

    def SetRecipeOptions(self, RecipeName, Options):
        self.Recipes[RecipeName].SetRecipeOptionsA(Options)

    def SetEsorexOptions(self, RecipeName, Options):
        self.Recipes[RecipeName].SetEsorexOptionsA(Options)

    def EnableRecipe(self, RecipeName):
        self.RecipeOrder.append(RecipeName)

    def DisableEsorex(self, RecipeName):
        self.Recipes[RecipeName].SetDisableEsorex(True)

    def StopAfterRecipe(self, RecipeName):
        self.Recipes[RecipeName].SetStopAfterRecipe(True)
        
    def ResetAllRecipes(self):
        self.Recipes = {}
        self.RecipeOrder = []
        self.CurrentRecipe = ''

    def PrintFilesInDictionary(self):
        for tag in self.Files.keys():
            print tag
            print '\t','SOF-tag','Fitsfile','BinX','BinY','Readout','Arm'
            for f in self.Files[tag]:
                print '\t',f.GetSofTag(),f.GetFitsName(),f.GetBinX(),f.GetBinY(),f.GetReadOut(), f.GetARM()


    def RunPipeline(self):
        #self.CurrentRecipe is set '' from start. It can have another
        #value if the pipeline was started from a restart file
        print 'PipelineManager, by Martin Sparre, Dark Cosmology Centre, 2011.\n'

        if os.path.exists(self.OutputDir) == False:
            print 'Directory with name '+self.OutputDir+' does not exist.'
            commands.getoutput('mkdir '+self.OutputDir)
            print 'Directory with name '+ self.OutputDir +' has now been created.\n'
            


        print 'Pipeline started.'
        if self.CurrentRecipe == '':
            if len(self.RecipeOrder) == 0:
                print 'Error: No recipes are enabled. 798uyhgg'
                return 0

            #Set current recipe to be the first recipe and execute
            self.CurrentRecipe = self.Recipes[self.RecipeOrder[0]]
            print "\nStart:", self.CurrentRecipe.GetRecipeName()
            self.Files = self.CurrentRecipe.Execute(self.Files)

            SaveToRestartFile(self.OutputDir + self.CurrentRecipe.GetRecipeName()+'_'+ self.CurrentRecipe.GetArm() +'.restart',self)#save to pickle-file       
            print '\tRestartfile saved: ' + self.OutputDir + self.CurrentRecipe.GetRecipeName()+'_'+ self.CurrentRecipe.GetArm() +'.restart'
            print "End:", self.CurrentRecipe.GetRecipeName()+'\n'

            if self.CurrentRecipe.GetStopAfterRecipe() == True:
                sys.exit('Execution stopped because StopAfterRecipe() was called by the user.')

        for NameOfCurrentSofFile in self.RecipeOrder:
            if self.RecipeOrder.index(NameOfCurrentSofFile) > self.RecipeOrder.index(self.CurrentRecipe.GetRecipeName()):
                self.CurrentRecipe = self.Recipes[NameOfCurrentSofFile]
                print "\nStart:", self.CurrentRecipe.GetRecipeName()
                self.Files = self.CurrentRecipe.Execute(self.Files)

                SaveToRestartFile(self.OutputDir + self.CurrentRecipe.GetRecipeName()+'_'+ self.CurrentRecipe.GetArm() +'.restart',self)#save to pickle-file       
                print '\tRestartfile saved: ' + self.OutputDir + self.CurrentRecipe.GetRecipeName()+'_'+ self.CurrentRecipe.GetArm() +'.restart'
                print "End:", self.CurrentRecipe.GetRecipeName()+'\n'

                if self.CurrentRecipe.GetStopAfterRecipe() == True:
                    sys.exit('Execution stopped because StopAfterRecipe() was called by the user.')

        print 'Pipeline finished.'

#datafiles
class TFile:
    def __init__(self, FitsName, SofTag):
        if os.path.isfile(FitsName) != True:
            print 'File:\t'+FitsName+'\tdoes not exist'

        self.SofTag = SofTag
        self.FitsName = FitsName
        
        ThisHeader =  pyfits.getheader(FitsName)
        
        #Binning X
        if 'ESO DET WIN1 BINX' in ThisHeader.keys():
            self.BinX = str(ThisHeader['ESO DET WIN1 BINX'])
        else:
            #print "Warning: ESO DET WIN1 BINX not in header"
            self.BinX = ""

        #Binning Y
        if 'ESO DET WIN1 BINY' in ThisHeader.keys():
            self.BinY = str(ThisHeader['ESO DET WIN1 BINY'])
        else:
            #print "Warning: ESO DET WIN1 BINY not in header"
            self.BinY = ""

        #Arm
        if 'ESO SEQ ARM' in ThisHeader.keys():
            self.ARM = str(ThisHeader['ESO SEQ ARM'])
        else:
            #print FitsName
            #print "Warning: ESO SEQ ARM not in header"
            self.ARM = ""
            #sys.exit()
            
        
        #Readout
        if 'ESO DET READ CLOCK' in ThisHeader.keys():
            self.ReadOut = str(ThisHeader['ESO DET READ CLOCK']).split('/')[0]
        else:
            #print "Warning: ESO DET READ CLOCK not in header"
            self.ReadOut = ""
            
        
    def GetSofTag(self):
        return self.SofTag

    def GetFitsName(self):
        return self.FitsName

    def GetBinX(self):
        return self.BinX

    def GetBinY(self):
        return self.BinY

    def GetARM(self):
        return self.ARM

    def GetReadOut(self):
        return self.ReadOut


class InputTag:
    def __init__(self, TagName, NFiles, Binning, ReadOut, Type):
        self.TagName = TagName
        self.NFiles = NFiles
        self.Binning = Binning
        self.ReadOut = ReadOut
        self.Type = Type

    def GetTagName(self):
        return self.TagName

    def GetNFiles(self):
        return self.NFiles

    def GetFilesNeeded(self):
        if '?' not in self.NFiles and '..n' not in self.NFiles:
            FilesNeeded = int(self.NFiles)
        elif '?' in self.NFiles:
            FilesNeeded = 1#just use the first file in the dictionary-array!
        else:
            FilesNeeded = 10000#10000 is the same as infinity. Append everything.

        return FilesNeeded

    def GetBinning(self):
        return self.Binning

    def GetReadOut(self):
        return self.ReadOut

    def GetType(self):
        return self.Type
