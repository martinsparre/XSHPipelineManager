#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, 2nd November 2011
#version 5.9.0

from PipelineManager import *

VIS = PipelineManager()
#VIS.SetOutputDir('Output')

############################################################
###   XSH_MBIAS (loop over all readout and binning-combinations)
############################################################

for ReadOut_match in ["100","400"]:
    for Binning in [["1","1"],["1","2"],["2","2"]]:
        BinX_match = Binning[0]
        BinY_match = Binning[1]

        EsorexName='xsh_mbias'
        SOFFileName='xsh_mbias_'+BinX_match+'x'+BinY_match+'_'+ReadOut_match
        
        VIS.DeclareNewRecipe(EsorexName,SOFFileName, BinX_match, BinY_match, ReadOut_match )
        VIS.DeclareRecipeInputTag(SOFFileName, "BIAS_VIS", "5", "any", "100k/400k")#recipe_name, InputTag, Nfiles, binning, readout
        VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")

        VIS.EnableRecipe(SOFFileName)


############################################################
###  XSH_PREDICT
############################################################

EsorexName='xsh_predict'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)

VIS.DeclareRecipeInputTag(SOFFileName, "FMTCHK_VIS", "1", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "1x1", "400k")

VIS.EnableRecipe(SOFFileName)

#changing detectarclines-min-sn can help if xsh_predict crashes
#VIS.SetRecipeOptions('xsh_predict','--detectarclines-min-sn=2.5')

#if xsh_predict crashes: try again with another FMTCHK_ARM

############################################################
###  XSH_ORDERPOS
############################################################

EsorexName='xsh_orderpos'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)
VIS.DeclareRecipeInputTag(SOFFileName, "ORDERDEF_VIS", "1", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_GUESS_VIS", "1", "1x1", "any")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "1x1", "400k")

VIS.EnableRecipe(SOFFileName)

############################################################
###  XSH_MFLAT (loop over all readout and binning-combinations)
############################################################

for ReadOut_match in ["100","400"]:
    for Binning in [["1","1"],["1","2"],["2","2"]]:
        BinX_match = Binning[0]
        BinY_match = Binning[1]

        EsorexName='xsh_mflat'
        SOFFileName='xsh_mflat_'+BinX_match+'x'+BinY_match+'_'+ReadOut_match
        
        VIS.DeclareNewRecipe(EsorexName,SOFFileName, BinX_match, BinY_match, ReadOut_match )
        VIS.DeclareRecipeInputTag(SOFFileName, "FLAT_SLIT_VIS", "5", "any", "100k/400k")
        VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
        VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_CENTR_VIS", "1", "1x1", "any")
        VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "1", "match", "match")
        VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")
        
        VIS.EnableRecipe(SOFFileName)

############################################################
###  XSH_2DMAP
############################################################

EsorexName='xsh_2dmap'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)
VIS.DeclareRecipeInputTag(SOFFileName, "WAVE_VIS", "1", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_FMT_VIS", "1", "1x1", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")

VIS.SetRecipeOptions(SOFFileName, '--keep-temp=yes')

VIS.EnableRecipe(SOFFileName)


############################################################
###  XSH_WAVECAL
############################################################

EsorexName='xsh_wavecal'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)
VIS.DeclareRecipeInputTag(SOFFileName, "ARC_SLIT_VIS", "1", "any", "400k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_VIS", "?", "1x1", "400k")

#VIS.EnableRecipe(SOFFileName)


############################################################
###  XSH_FLEXCOMP
############################################################

EsorexName='xsh_flexcomp'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)
VIS.DeclareRecipeInputTag(SOFFileName, "AFC_ATT_VIS", "1", "any", "400k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_AFC_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")

#VIS.EnableRecipe(SOFFileName)



############################################################
###  XSH_RESPON_SLIT_OFFSET
############################################################

EsorexName='xsh_respon_slit_offset'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)

VIS.DeclareRecipeInputTag(SOFFileName, "STD_FLUX_SLIT_OFFSET_VIS", "1..n", "1x1", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "SKY_SLIT_VIS", "1..n", "1x1", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_VIS", "1", "1x1", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "?", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_VIS", "?", "-" ,"-")
VIS.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_VIS", "?", "-" , "-")
VIS.DeclareRecipeInputTag(SOFFileName,"HIGH_ABS_WIN_VIS", "?", "-" , "-")

#VIS.EnableRecipe(SOFFileName)


############################################################
###  XSH_RESPON_SLIT_STARE
############################################################

EsorexName='xsh_respon_slit_stare'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)

VIS.DeclareRecipeInputTag(SOFFileName, "STD_FLUX_SLIT_STARE_VIS", "1..n", "1x1", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")                                          
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")  
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "1", "match", "match")                                         
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_VIS", "1", "match", "match")                                              
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "match", "match")                                                                                        
VIS.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_VIS", "1", "1x1", "400k")                                   
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?+", "match", "match")                                           
VIS.DeclareRecipeInputTag(SOFFileName, "FLUX_STD_CATALOG_VIS", "?", "-", "-")                                       
VIS.DeclareRecipeInputTag(SOFFileName, "ATMOS_EXT_VIS", "?", "-", "-")                               
VIS.DeclareRecipeInputTag(SOFFileName, "SLIT_MAP_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName, "WAVE_MAP_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName,"HIGH_ABS_WIN_VIS", "?", "-" , "-")

#VIS.EnableRecipe(SOFFileName)

############################################################
###  XSH_RESPON_SLIT_NOD (telluric)
############################################################

EsorexName='xsh_respon_slit_nod'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)

VIS.DeclareRecipeInputTag(SOFFileName, "STD_TELL_SLIT_NOD_VIS", "1..n", "any", "any")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_AFC_VIS", "?", "-", "-")#?????
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_VIS", "1", "-", "-")#?????
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName, "FLUX_STD_CATALOG_VIS", "?", "-" ,"-")
VIS.DeclareRecipeInputTag(SOFFileName, "ATMOS_EXT_VIS", "?", "-" , "-")
VIS.DeclareRecipeInputTag(SOFFileName, "SKY_SUB_BKPTS_VIS", "?", "-" , "-")
VIS.DeclareRecipeInputTag(SOFFileName, "HIGH_ABS_WIN_VIS", "?", "-" , "-")

#VIS.EnableRecipe(SOFFileName)

############################################################
###  XSH_SCIRED_SLIT_NOD
############################################################

EsorexName='xsh_scired_slit_nod'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)
VIS.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_NOD_VIS", "1..n", "any", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_VIS", "?", "-" ,"-")
VIS.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_VIS", "?", "-" , "-")
VIS.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_VIS", "?", "-" , "-")

#VIS.EnableRecipe(SOFFileName)

#VIS.SetRecipeOptions(SOFFileName,'--rectify-bin-lambda=0.025')

############################################################
###  XSH_SCIRED_SLIT_STARE
############################################################

EsorexName='xsh_scired_slit_stare'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)
VIS.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_STARE_VIS", "1..n", "any", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_VIS", "?", "-" ,"-")
VIS.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_VIS", "?", "-" , "-")
VIS.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_VIS", "?", "-" , "-")

#VIS.EnableRecipe(SOFFileName)


############################################################
###  XSH_SCIRED_SLIT_OFFSET
############################################################

EsorexName='xsh_scired_slit_offset'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)
VIS.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_OFFSET_VIS", "1..n", "any", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "SKY_SLIT_VIS", "1..n", "match", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_VIS", "?", "-" ,"-")
VIS.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_VIS", "?", "-" , "-")
VIS.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_VIS", "?", "-" , "-")

#VIS.EnableRecipe(SOFFileName)

############################################################
###  INPUT-FILES
############################################################

#CALIB and RAW

VIS.SetFiles('BIAS_VIS',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-08T10:46:35.375.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-08T10:48:03.302.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-08T10:49:31.229.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-08T10:50:59.156.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-08T10:52:27.083.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:40:27.392.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:43:10.945.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:45:54.498.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:48:38.051.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:51:21.614.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:53:17.034.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:54:01.397.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:54:45.772.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:55:30.125.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:56:14.489.fits'])
VIS.SetFiles('FMTCHK_VIS',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T11:31:34.581.fits'])
VIS.SetFiles('ORDERDEF_VIS',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T11:38:58.377.fits'])
VIS.SetFiles('FLAT_SLIT_VIS',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:10:16.335.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:11:16.140.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:12:16.155.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:13:13.889.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T10:14:11.934.fits'])
VIS.SetFiles('WAVE_VIS',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T11:41:38.170.fits'])

#VIS.SetFiles('OBJECT_SLIT_NOD_VIS',['/home/ms/KU/Observations/GRB070802_host/HostGalaxy/2010_10/086.B-0954A2001/086.B-0954A/2010-10-29/SCIENCE/XSHOO.2010-10-30T03_54_14.158.fits','/home/ms/KU/Observations/GRB070802_host/HostGalaxy/2010_10/086.B-0954A2001/086.B-0954A/2010-10-29/SCIENCE/XSHOO.2010-10-30T04_25_48.975.fits','/home/ms/KU/Observations/GRB070802_host/HostGalaxy/2010_10/086.B-0954A2001/086.B-0954A/2010-10-29/SCIENCE/XSHOO.2010-10-30T04_58_11.035.fits','/home/ms/KU/Observations/GRB070802_host/HostGalaxy/2010_10/086.B-0954A2001/086.B-0954A/2010-10-29/SCIENCE/XSHOO.2010-10-30T05_29_47.082.fits'])
#VIS.SetFiles('RESPONSE_MERGE1D_SLIT_VIS',['/home/ms/KU/Observations/GRB070802_host/Reduction110705/VIS_STDSTAR/Output/xsh_respon_slit_offset_RESPONSE_MERGE1D_SLIT_VIS_VIS_1x1_100k.fits'])

##REF-files:
VIS.SetFiles('ATMOS_EXT_VIS',['/home/ms/calibrations/calib/xsh-1.3.0/cal/xsh_paranal_extinct_vis.fits'])
VIS.SetFiles('FLUX_STD_CATALOG_VIS',['/home/ms/calibrations/calib/xsh-1.3.0/cal/xsh_star_catalog_vis.fits'])
VIS.SetFiles('ARC_LINE_LIST_VIS',['/home/ms/calibrations/calib/xsh-1.3.0/cal/ThAr_vis_custom.fits'])
VIS.SetFiles('SPECTRAL_FORMAT_TAB_VIS',['/home/ms/calibrations/calib/xsh-1.3.0/cal/SPECTRAL_FORMAT_TAB_VIS.fits'])
VIS.SetFiles('XSH_MOD_CFG_TAB_VIS',['/home/ms/calibrations/calib/xsh-1.3.0/cal/xs_vis_def_com4.fits'])
VIS.SetFiles('HIGH_ABS_WIN_VIS',['/home/ms/calibrations/calib/xsh-1.3.0/cal/xsh_high_abs_window_vis.fits'])

#Run
VIS.RunPipeline()
