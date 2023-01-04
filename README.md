# Football-Data-Analysis Estimator: Project Overview

- Downloaded Data From Kaggle
- Engineered features from the Stats of Players normilized values
- Optimized Scater, Bar, Parallel-coordinets Plots

# Code and Resources Used

**Python Version:** 3.9
**Packages:** pandas, numpy, matplotlib, plotly
**Kaggle Dataset:** [https://www.kaggle.com/datasets/vivovinco/20212022-football-player-stats][https://www.kaggle.com/datasets/vivovinco/20212022-football-player-stats]

# Downloaded Data From Kaggle

Downloaded Dataset football-player-stats from Kaggle. We got the following with each Player:

- Rk
- Player
- Nation
- Pos
- Squad
- Comp
- Age
- Born
- MP
- Starts
- Min
- 90s
- Goals
- Shots
- SoT
- SoT%
- G/Sh
- G/SoT
- ShoDist
- ShoFK
- ShoPK
- PKatt
- PasTotCmp
- PasTotAtt
- PasTotCmp%
- PasTotDist
- PasTotPrgDist
- PasShoCmp
- PasShoAtt
- PasShoCmp%
- PasMedCmp
- PasMedAtt
- PasMedCmp%
- PasLonCmp
- PasLonAtt
- PasLonCmp%
- Assists
- PasAss
- Pas3rd
- PPA
- CrsPA
- PasProg
- PasAtt
- PasLive
- PasDead
- PasFK
- TB
- PasPress
- Sw
- PasCrs
- CK
- CkIn
- CkOut
- CkStr
- PasGround
- PasLow
- PasHigh
- PaswLeft
- PaswRight
- PaswHead
- TI
- PaswOther
- PasCmp
- PasOff
- PasOut
- PasInt
- PasBlocks
- SCA
- ScaPassLive
- ScaPassDead
- ScaDrib
- ScaSh
- ScaFld
- GCA
- GcaPassLive
- GcaPassDead
- GcaDrib
- GcaSh
- GcaFld
- GcaDef
- Tkl
- TklWon
- TklDef3rd
- TklMid3rd
- TklAtt3rd
- TklDri
- TklDriAtt
- TklDri%
- TklDriPast
- Press
- PresSucc
- Press%
- PresDef3rd
- PresMid3rd
- PresAtt3rd
- Blocks
- BlkSh
- BlkShSv
- BlkPass
- Int
- Tkl+Int
- Clr
- Err
- Touches
- TouDefPen
- TouDef3rd
- TouMid3rd
- TouAtt3rd
- TouAttPen
- TouLive
- DriSucc
- DriAtt
- DriSucc%
- DriPast
- DriMegs
- Carries
- CarTotDist
- CarPrgDist
- CarProg
- Car3rd
- CPA
- CarMis
- CarDis
- RecTarg
- Rec
- Rec%
- RecProg
- CrdY
- CrdR
- 2CrdY
- Fls
- Fld
- Off
- Crs
- TklW
- PKwon
- PKcon
- OG
- Recov
- AerWon
- AerLost
- AerWon%

# Data Cleaning

After downloading the data, I needed to clean it up. I made the following changes and created the following variables:

- Made column for G/A
- Made column for Goals divided by 90 min
- Made column for Assists divided by 90 min
- Parsed all values multiplied by 90 min
- Made columns for played whole season how much he got subbed

# EDA

I looked at the distributions of the data and the value counts for the various categorical variables.
