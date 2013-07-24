# -*- coding: utf-8 -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, 2nd November 2011
#version 5.9.0

from PipelineManager import *

NIR = PipelineManager()
NIR.SetOutputDir('Output')

############################################################
###   XSH_MDARK
############################################################

EsorexName='xsh_mdark'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)

NIR.DeclareRecipeInputTag(SOFFileName, "DARK_NIR", "3", "-", "-")#recipe_name, InputTag, Nfiles, binning, readout
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")

NIR.EnableRecipe(SOFFileName)

############################################################
###  XSH_PREDICT
############################################################

EsorexName='xsh_predict'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)

NIR.DeclareRecipeInputTag(SOFFileName, "FMTCHK_NIR_ON", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "FMTCHK_NIR_OFF", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")

NIR.EnableRecipe(SOFFileName)

#if xsh_predict crashes: try again with another FMTCHK_ARM

############################################################
###  XSH_ORDERPOS
############################################################

EsorexName='xsh_orderpos'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)
NIR.DeclareRecipeInputTag(SOFFileName, "ORDERDEF_NIR_ON", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDERDEF_NIR_OFF", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_GUESS_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")

NIR.EnableRecipe(SOFFileName)

############################################################
###  XSH_MFLAT
############################################################

EsorexName='xsh_mflat'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)
NIR.DeclareRecipeInputTag(SOFFileName, "FLAT_SLIT_NIR_ON", "5", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "FLAT_SLIT_NIR_OFF", "5", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_CENTR_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")

NIR.EnableRecipe(SOFFileName)

############################################################
###  XSH_2DMAP
############################################################

EsorexName='xsh_2dmap'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)
NIR.DeclareRecipeInputTag(SOFFileName, "WAVE_NIR_ON", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "WAVE_NIR_OFF", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_FMT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")

NIR.EnableRecipe(SOFFileName)

NIR.SetRecipeOptions(SOFFileName, '--keep-temp=yes')#Used for test-scripts

#if xsh_predict crashes: try again with another FMTCHK_ARM



############################################################
###  XSH_WAVECAL
############################################################

EsorexName='xsh_wavecal'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)
NIR.DeclareRecipeInputTag(SOFFileName, "ARC_SLIT_NIR_ON", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ARC_SLIT_NIR_OFF", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")

#NIR.EnableRecipe(SOFFileName)


############################################################
###  XSH_FLEXCOMP
############################################################

EsorexName='xsh_flexcomp'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)
NIR.DeclareRecipeInputTag(SOFFileName, "AFC_ATT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ARC_LINE_LIST_AFC_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_NIR", "1", "-", "-")

#NIR.EnableRecipe(SOFFileName)




############################################################
###  XSH_RESPON_SLIT_OFFSET
############################################################

EsorexName='xsh_respon_slit_offset'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)

NIR.DeclareRecipeInputTag(SOFFileName, "STD_FLUX_SLIT_OFFSET_NIR", "1..n", "-", "-")#recipe_name, InputTag, Nfiles, binning, readout
NIR.DeclareRecipeInputTag(SOFFileName, "SKY_SLIT_NIR", "1..n", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_NIR", "1", "-", "-")#?????
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_NIR", "?", "-" ,"-")
NIR.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName,"HIGH_ABS_WIN_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SLIT_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "WAVE_MAP_NIR", "?", "-", "-")

#NIR.EnableRecipe(SOFFileName)


############################################################
###  XSH_RESPON_SLIT_NOD (telluric)
############################################################

EsorexName='xsh_respon_slit_nod'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)

NIR.DeclareRecipeInputTag(SOFFileName, "STD_TELL_SLIT_NOD_NIR", "1..n", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_AFC_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "FLUX_STD_CATALOG_NIR", "?", "-" ,"-")
NIR.DeclareRecipeInputTag(SOFFileName, "ATMOS_EXT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SKY_SUB_BKPTS_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName, "HIGH_ABS_WIN_NIR", "?", "-" , "-")

#NIR.EnableRecipe(SOFFileName)

############################################################
###  XSH_RESPON_SLIT_STARE
############################################################

EsorexName='xsh_respon_slit_stare'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)

NIR.DeclareRecipeInputTag(SOFFileName, "STD_FLUX_SLIT_STARE_NIR", "1..n", "-", "-")#recipe_name, InputTag, Nfiles, binning, readout
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_NIR", "1", "-", "-")#?????
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_NIR", "?", "-" ,"-")
NIR.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName,"HIGH_ABS_WIN_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SLIT_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "WAVE_MAP_NIR", "?", "-", "-")

#NIR.EnableRecipe(SOFFileName)
#NIR.SetRecipeOptions(SOFFileName,'--sky-subtract=FALSE')
#NIR.SetRecipeOptions(SOFFileName, "--sky-method=MEDIAN")

############################################################
###  XSH_SCIRED_SLIT_NOD
############################################################

EsorexName='xsh_scired_slit_nod'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)
NIR.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_NOD_NIR", "1..n", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_NIR", "?", "-" ,"-")
NIR.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_NIR", "1", "-", "-")
#NIR.EnableRecipe(SOFFileName)

############################################################
###  XSH_SCIRED_SLIT_STARE
############################################################

EsorexName='xsh_scired_slit_stare'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)
NIR.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_STARE_NIR", "1..n", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_NIR", "?", "-" ,"-")
NIR.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_NIR", "1", "-", "-")
#NIR.EnableRecipe(SOFFileName)

#NIR.SetRecipeOptions(SOFFileName, "--sky-method=MEDIAN")#MEDIAN is more stable than bspline
#NIR.SetRecipeOptions(SOFFileName, "--sky-bspline-order=4")
#NIR.SetRecipeOptions(SOFFileName, "--sky-subtract=FALSE")

#options from Stefan and Sune (these options might give better sky-subtraction):
#NIR.SetRecipeOptions(SOFFileName, "--background-nb-y=50 --background-radius-y=40 --background-method=median --rectify-bin-lambda=.05 --rectify-bin-slit=.2 --removecrhsingle-niter=3 --extract-method=FULL --compute-map=TRUE --rectify-conserve-flux=FALSE --sky-subtract=TRUE --sky-bspline-nbkpts-first=500 --sky-bspline-nbkpts-second=500 --sky-method=MEDIAN  --rectify-radius=1 --mergeord-method=0")

############################################################
###  XSH_SCIRED_SLIT_OFFSET
############################################################

EsorexName='xsh_scired_slit_offset'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)
NIR.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_OFFSET_NIR", "1..n", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SKY_SLIT_NIR", "1..n", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_NIR", "?", "-" ,"-")
NIR.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_NIR", "1", "-", "-")
#NIR.EnableRecipe(SOFFileName)

############################################################
###  INPUT-FILES
############################################################

#CALIB and RAW

NIR.SetFiles('MASTER_BP_MAP_NIR',['/home/ms/KU/Observations/GRB070802_host/MASTER_BP_MAP_NIR.fits'])
NIR.SetFiles('DARK_NIR',['/home/ms/KU/Observations/111008/CALIB/DARKNIR/XSHOO.2011-10-09T12:44:02.290.fits','/home/ms/KU/Observations/111008/CALIB/DARKNIR/XSHOO.2011-10-09T12:54:11.048.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T12:33:52.866.fits'])
NIR.SetFiles('FMTCHK_NIR_OFF',['/home/ms/KU/Observations/111008/CALIB/FMTCHK/XSHOO.2011-10-09T11:34:04.174.fits'])
NIR.SetFiles('FMTCHK_NIR_ON',['/home/ms/KU/Observations/111008/CALIB/FMTCHK/XSHOO.2011-10-09T11:32:59.075.fits'])
NIR.SetFiles('FLAT_SLIT_NIR_OFF',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T09:52:42.842.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T09:54:20.622.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T09:55:58.397.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T09:57:36.170.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T09:59:11.944.fits'])
NIR.SetFiles('FLAT_SLIT_NIR_ON',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T09:51:53.287.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T09:53:31.068.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T09:55:08.842.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T09:56:46.616.fits','/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T09:58:22.390.fits'])
NIR.SetFiles('ORDERDEF_NIR_ON',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T11:40:45.061.fits'])
NIR.SetFiles('ORDERDEF_NIR_OFF',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T11:40:56.398.fits'])
NIR.SetFiles('WAVE_NIR_ON',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T11:42:56.504.fits'])
NIR.SetFiles('WAVE_NIR_OFF',['/home/ms/KU/Observations/111008/CALIB/XSHOO.2011-10-09T11:43:25.279.fits'])



#NIR.SetFiles('RESPONSE_MERGE1D_SLIT_NIR',['/home/ms/KU/Observations/GRB070802_host/Reduction110705/NIR_STDSTAR/Output/xsh_respon_slit_offset_RESPONSE_MERGE1D_SLIT_NIR_NIR_x_.fits'])

#NIR.SetFiles('SKY_SLIT_NIR',['/home/ms/KU/Observations/GRB070802_host/HostGalaxy/2010_10/086.B-0954A2001/086.B-0954A/2010-10-29/CALIB/XSHOO.2010-10-29T23_45_01.091.fits'])
#NIR.SetFiles('OBJECT_SLIT_OFFSET_NIR',['/home/ms/KU/Observations/GRB070802_host/HostGalaxy/2010_10/086.B-0954A2001/086.B-0954A/2010-10-29/CALIB/XSHOO.2010-10-29T23_39_11.507.fits'])




#REF-files
NIR.SetFiles("SPECTRAL_FORMAT_TAB_NIR",['/home/ms/calibrations/calib/xsh-1.3.0/cal/SPECTRAL_FORMAT_TAB_NIR.fits'])
NIR.SetFiles('ARC_LINE_LIST_NIR',['/home/ms/calibrations/calib/xsh-1.3.7/cal/penray_nir_custom_air_ext_paul.fits'])
#NIR.SetFiles("ARC_LINE_LIST_NIR",['/home/ms/calibrations/calib/xsh-1.3.0/cal/ThAr_nir_custom_air_ext.dat.fits'])
NIR.SetFiles("XSH_MOD_CFG_TAB_NIR",['/home/ms/calibrations/calib/xsh-1.3.0/cal/xs_nir_def_com4.fits'])
NIR.SetFiles("FLUX_STD_CATALOG_NIR",['/home/ms/calibrations/calib/xsh-1.3.0/cal/xsh_star_catalog_nir.fits'])
NIR.SetFiles('ATMOS_EXT_NIR',['/home/ms/calibrations/calib/xsh-1.3.0/cal/xsh_paranal_extinct_nir.fits'])
NIR.SetFiles('HIGH_ABS_WIN_NIR',['/home/ms/calibrations/calib/xsh-1.3.0/cal/xsh_high_abs_window_nir.fits'])

#Run
NIR.RunPipeline()
