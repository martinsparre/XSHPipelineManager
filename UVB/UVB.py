#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, 2nd November 2011
#version 5.9.0

from PipelineManager import *

UVB = PipelineManager()
#UVB.SetOutputDir('Output')

############################################################
###   XSH_MBIAS (loop over all readout and binning-combinations)
############################################################

for ReadOut_match in ["100","400"]:
    for Binning in [["1","1"],["1","2"],["2","2"]]:
        BinX_match = Binning[0]
        BinY_match = Binning[1]

        #define the recipes (copy from the pipeline-manual)
        EsorexName='xsh_mbias'
        SOFFileName='xsh_mbias_'+BinX_match+'x'+BinY_match+'_'+ReadOut_match
        
        UVB.DeclareNewRecipe(EsorexName,SOFFileName, BinX_match, BinY_match, ReadOut_match )#write the name of the Esorex-recipe
        UVB.DeclareRecipeInputTag(SOFFileName, "BIAS_UVB", "5", "any", "100k/400k")#recipe_name, InputTag, Nfiles, binning, readout
        UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")

        UVB.EnableRecipe(SOFFileName)

############################################################
###  XSH_PREDICT
############################################################

EsorexName='xsh_predict'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)

UVB.DeclareRecipeInputTag(SOFFileName, "FMTCHK_UVB", "1", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "?", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "1x1", "400k")

UVB.EnableRecipe(SOFFileName)

#try this option if condition failed: ordersize > deg_poly:
#UVB.SetRecipeOptions('xsh_predict','--detectarclines-ordertab-deg-y=1')
#UVB.SetRecipeOptions('xsh_predict','--detectarclines-min-sn=5.0 --detectarclines-clip-niter=10 --model-maxit=5000')


#if xsh_predict crashes: try again with another FMTCHK_ARM

############################################################
###  XSH_ORDERPOS
############################################################

EsorexName='xsh_orderpos'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)
UVB.DeclareRecipeInputTag(SOFFileName, "ORDERDEF_D2_UVB", "1", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName, "ORDERDEF_QTH_UVB", "1", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_GUESS_UVB", "1", "1x1", "any")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "?", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "1x1", "400k")

UVB.EnableRecipe(SOFFileName)

############################################################
###  XSH_MFLAT (loop over all readout and binning-combinations)
############################################################

for ReadOut_match in ["100","400"]:
    for Binning in [["1","1"],["1","2"],["2","2"]]:
        BinX_match = Binning[0]
        BinY_match = Binning[1]

        EsorexName='xsh_mflat'
        SOFFileName='xsh_mflat_'+BinX_match+'x'+BinY_match+'_'+ReadOut_match
        
        UVB.DeclareNewRecipe(EsorexName,SOFFileName, BinX_match, BinY_match, ReadOut_match )
        UVB.DeclareRecipeInputTag(SOFFileName, "FLAT_D2_SLIT_UVB", "5", "any", "100k/400k")
        UVB.DeclareRecipeInputTag(SOFFileName, "FLAT_QTH_SLIT_UVB", "5", "match", "match")
        UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
        UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_CENTR_UVB", "1", "1x1", "any")
        UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "1", "match", "match")
        UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")
        
        UVB.EnableRecipe(SOFFileName)

############################################################
###  XSH_2DMAP
############################################################

EsorexName='xsh_2dmap'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)
UVB.DeclareRecipeInputTag(SOFFileName, "WAVE_UVB", "1", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_FMT_UVB", "1", "1x1", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")

UVB.SetRecipeOptions(SOFFileName, '--keep-temp=yes')

UVB.EnableRecipe(SOFFileName)


############################################################
###  XSH_WAVECAL
############################################################

EsorexName='xsh_wavecal'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)
UVB.DeclareRecipeInputTag(SOFFileName, "ARC_SLIT_UVB", "1", "any", "400k")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_UVB", "?", "1x1", "400k")

#UVB.EnableRecipe(SOFFileName)


############################################################
###  XSH_FLEXCOMP
############################################################

EsorexName='xsh_flexcomp'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)
UVB.DeclareRecipeInputTag(SOFFileName, "AFC_ATT_UVB", "1", "any", "400k")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_AFC_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")

#UVB.EnableRecipe(SOFFileName)



############################################################
###  XSH_RESPON_SLIT_STARE
############################################################

EsorexName='xsh_respon_slit_stare'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)

UVB.DeclareRecipeInputTag(SOFFileName, "STD_FLUX_SLIT_STARE_UVB", "1..n", "1x1", "100k")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")                                          
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")  
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "1", "match", "match")                                         
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_UVB", "1", "match", "match")                                              
UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "match", "match")                                                                                        
UVB.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_UVB", "1", "1x1", "400k")                                   
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?+", "match", "match")                                           
UVB.DeclareRecipeInputTag(SOFFileName, "FLUX_STD_CATALOG_UVB", "?", "-", "-")                                       
UVB.DeclareRecipeInputTag(SOFFileName, "ATMOS_EXT_UVB", "?", "-", "-")                               
UVB.DeclareRecipeInputTag(SOFFileName, "SLIT_MAP_UVB", "?", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName, "WAVE_MAP_UVB", "?", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName,"HIGH_ABS_WIN_UVB", "?", "-" , "-")

#UVB.EnableRecipe(SOFFileName)

############################################################
###  XSH_RESPON_SLIT_OFFSET
############################################################

EsorexName='xsh_respon_slit_offset'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)

UVB.DeclareRecipeInputTag(SOFFileName, "STD_FLUX_SLIT_OFFSET_UVB", "1..n", "1x1", "100k")
UVB.DeclareRecipeInputTag(SOFFileName, "SKY_SLIT_UVB", "1..n", "1x1", "100k")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_UVB", "1", "1x1", "100k")
UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "?", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_UVB", "?", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_UVB", "?", "-" ,"-")
UVB.DeclareRecipeInputTag(SOFFileName,"HIGH_ABS_WIN_UVB", "?", "-" , "-")
UVB.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_UVB", "?", "-" , "-")
UVB.DeclareRecipeInputTag(SOFFileName, "SLIT_MAP_UVB", "?", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName, "WAVE_MAP_UVB", "?", "1x1", "400k")

#UVB.EnableRecipe(SOFFileName)

############################################################
###  XSH_RESPON_SLIT_NOD (flux std)
############################################################

EsorexName='xsh_respon_slit_nod'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)

UVB.DeclareRecipeInputTag(SOFFileName, "STD_FLUX_SLIT_NOD_UVB", "1", "any", "any")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_UVB", "?", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_AFC_UVB", "?", "-", "-")#?????
UVB.DeclareRecipeInputTag(SOFFileName, "FLUX_STD_CATALOG_UVB", "?", "-" ,"-")
UVB.DeclareRecipeInputTag(SOFFileName, "ATMOS_EXT_UVB", "?", "-" , "-")
UVB.DeclareRecipeInputTag(SOFFileName, "HIGH_ABS_WIN_UVB", "?", "-" , "-")
UVB.DeclareRecipeInputTag(SOFFileName, "SKY_SUB_BKPTS_UVB", "?", "-" , "-")

#UVB.EnableRecipe(SOFFileName)

#UVB.SetRecipeOptions(SOFFileName, "--sky-method=MEDIAN") #MEDIAN is more stable than bspline
#UVB.SetRecipeOptions(SOFFileName, "--sky-subtract=FALSE")



############################################################
###  XSH_SCIRED_SLIT_OFFSET
############################################################

EsorexName='xsh_scired_slit_offset'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)
UVB.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_OFFSET_UVB", "1..n", "any", "100k")
UVB.DeclareRecipeInputTag(SOFFileName, "SKY_SLIT_UVB", "1..n", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_UVB", "?", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_UVB", "?", "-" ,"-")
UVB.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_UVB", "?", "-" , "-")
UVB.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_UVB", "?", "-" , "-")

#UVB.EnableRecipe(SOFFileName)

############################################################
###  XSH_SCIRED_SLIT_NOD
############################################################

EsorexName='xsh_scired_slit_nod'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)
UVB.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_NOD_UVB", "1..n", "any", "100k")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_UVB", "?", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_UVB", "?", "-" ,"-")
UVB.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_UVB", "?", "-" , "-")
UVB.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_UVB", "?", "-" , "-")

#UVB.EnableRecipe(SOFFileName)

############################################################
###  XSH_SCIRED_SLIT_STARE
############################################################

EsorexName='xsh_scired_slit_stare'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)
UVB.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_STARE_UVB", "1", "any", "100k")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_UVB", "?", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_UVB", "?", "-" ,"-")
UVB.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_UVB", "?", "-" , "-")
UVB.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_UVB", "?", "-" , "-")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_UVB", "1", "-", "-")

#UVB.EnableRecipe(SOFFileName)

############################################################
###  INPUT-FILES
############################################################

#CALIB and RAW
UVB.SetFiles('BIAS_UVB',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-08T10:45:56.801.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-08T10:47:24.729.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-08T10:48:52.656.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-08T10:50:20.583.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-08T10:51:48.510.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:39:16.406.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:41:59.950.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:44:43.502.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:47:27.056.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:50:10.619.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:52:57.273.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:53:41.646.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:54:26.020.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:55:10.383.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:55:54.737.fits'])
UVB.SetFiles('FMTCHK_UVB',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T11:31:29.430.fits'])
UVB.SetFiles('ORDERDEF_D2_UVB',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T11:36:54.547.fits'])
UVB.SetFiles('ORDERDEF_QTH_UVB',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T11:38:01.232.fits'])
UVB.SetFiles('FLAT_D2_SLIT_UVB',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:02:04.955.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:02:50.328.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:03:35.962.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:04:21.246.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:05:07.240.fits'])
UVB.SetFiles('FLAT_QTH_SLIT_UVB',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:06:17.926.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:07:05.410.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:07:50.923.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:08:38.147.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:09:26.141.fits'])
UVB.SetFiles('WAVE_UVB',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T11:41:33.059.fits'])

#UVB.SetFiles('OBJECT_SLIT_NOD_UVB',['/home/ms/KU/Observations/GRB070802_host/HostGalaxy/2010_10/086.B-0954A2001/086.B-0954A/2010-10-29/SCIENCE/XSHOO.2010-10-30T03_54_09.018.fits','/home/ms/KU/Observations/GRB070802_host/HostGalaxy/2010_10/086.B-0954A2001/086.B-0954A/2010-10-29/SCIENCE/XSHOO.2010-10-30T04_25_43.825.fits','/home/ms/KU/Observations/GRB070802_host/HostGalaxy/2010_10/086.B-0954A2001/086.B-0954A/2010-10-29/SCIENCE/XSHOO.2010-10-30T04_58_05.875.fits','/home/ms/KU/Observations/GRB070802_host/HostGalaxy/2010_10/086.B-0954A2001/086.B-0954A/2010-10-29/SCIENCE/XSHOO.2010-10-30T05_29_41.881.fits'])
#UVB.SetFiles('RESPONSE_MERGE1D_SLIT_UVB',['/home/ms/KU/Observations/GRB070802_host/Reduction110705/UVB_STDSTAR/Output/xsh_respon_slit_offset_RESPONSE_MERGE1D_SLIT_UVB_UVB_1x1_100k.fits'])

#REF-files:
UVB.SetFiles("SPECTRAL_FORMAT_TAB_UVB",["/home/ms/calibrations/calib/xsh-1.3.0/cal/SPECTRAL_FORMAT_TAB_UVB.fits"])
UVB.SetFiles("ARC_LINE_LIST_UVB",["/home/ms/calibrations/calib/xsh-1.3.0/cal/ThAr_uvb_custom.fits"])
UVB.SetFiles("XSH_MOD_CFG_TAB_UVB",["/home/ms/calibrations/calib/xsh-1.3.0/cal/xs_uvb_def_com4.fits"])
UVB.SetFiles("FLUX_STD_CATALOG_UVB",['/home/ms/calibrations/calib/xsh-1.3.0/cal/xsh_star_catalog_uvb.fits'])
UVB.SetFiles("ATMOS_EXT_UVB",['/home/ms/calibrations/calib/xsh-1.3.0/cal/xsh_paranal_extinct_uvb.fits'])
UVB.SetFiles("SKY_LINE_LIST_UVB",['/home/ms/calibrations/calib/xsh-1.3.0/cal/SKY_LINE_LIST_UVB.fits'])
UVB.SetFiles('HIGH_ABS_WIN_UVB',['/home/ms/calibrations/calib/xsh-1.3.0/cal/xsh_high_abs_window_uvb.fits'])

#Run
UVB.RunPipeline()
