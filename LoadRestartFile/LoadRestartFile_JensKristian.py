#!/usr/bin/python
# -*- coding: utf-8 -*-
#Jens-Kristian Krogager and Martin Sparre, DARK, December 2010
#version 5.9.0

from PipelineManager import *
AFC_Files = {}
ScienceFiles={}


ScienceFiles['DLA2_PA1']='/Users/krogager/Data/2010_11/raw/2010-11-08/SCIENCE/XSHOO.2010-11-09T05:38:42.924.fits'
AFC_Files['DLA2_PA1']='/Users/krogager/Data/2010_11/raw/2010-11-08/CALIB/XSHOO.2010-11-09T05:34:23.622.fits'

#add more files here...

for filekey in ScienceFiles.keys():
      UVB = LoadRestartFile('Output/xsh_wavecal_UVB.restart')
      UVB.ResetAllRecipes()
      print "Running on OB name: "+filekey

      ############################################################
      ###  XSH_FLEXCOMP
      ############################################################
      
      EsorexName='xsh_flexcomp'
      SOFFileName = EsorexName#+'_'+filekey
      
      UVB.DeclareNewRecipe(EsorexName)
      UVB.DeclareRecipeInputTag(SOFFileName, "AFC_ATT_UVB", "1", "any", "400k")
      UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
      UVB.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_AFC_UVB", "1", "-", "-")
      UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "1", "match", "match")
      UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "-", "-")
      UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")
      UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")
      
      UVB.EnableRecipe(SOFFileName)

      
      ############################################################
      ###  XSH_SCIRED_SLIT_STARE
      ############################################################
  
      EsorexName='xsh_scired_slit_stare'
      SOFFileName = EsorexName+'_'+filekey+'_AFC'
      
      UVB.DeclareNewRecipe(EsorexName,SOFFileName)
      UVB.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_STARE_UVB", "1", "any", "100k")
      UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
      UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_UVB", "1", "match", "match")
      UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "1", "match", "match")
      UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "match", "match")
      UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_AFC_UVB", "1", "-", "-")
      #UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")
      UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")
      UVB.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_UVB", "?", "1x1", "400k")
      UVB.DeclareRecipeInputTag(SOFFileName, "FLUX_STD_CATALOG_UVB", "?", "-" ,"-")
      UVB.DeclareRecipeInputTag(SOFFileName, "ATMOS_EXT_UVB", "?", "-" , "-")
      UVB.EnableRecipe(SOFFileName)
      
      #UVB.SetRecipeOptions(SOFFileName,'--rectify-bin-lambda=0.025 --sky-subtract=FALSE')
      UVB.SetRecipeOptions(SOFFileName,'--rectify-bin-lambda=0.025')
  
      ############################################################
      ###  SETTING FILES
      ############################################################

      UVB.SetFiles('OBJECT_SLIT_STARE_UVB',[ScienceFiles[filekey]])
      UVB.SetFiles('AFC_ATT_UVB',[AFC_Files[filekey]])
      UVB.RunPipeline()
