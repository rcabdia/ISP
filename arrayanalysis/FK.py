#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 06:37:45 2017

@author: robertocabieces
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import Normalize
import obspy
from obspy.core import UTCDateTime
import numpy as np
from obspy.core import read
from obspy.core import UTCDateTime
from obspy.core.util import AttribDict
from obspy.signal.invsim import corn_freq_2_paz
from obspy.signal.array_analysis import array_processing
#from obspy.geodetics.base import gps2dist_azimuth
#from scipy.signal import argrelextrema as pks
from obspy.signal.array_analysis import get_geometry
import pandas as pd
import os

#import matplotlib.dates as mdates

def FK(path,path_coords,stime,DT,fmin,fmax,slim,sres,win_len,win_frac):
    path=path+"/*.*"
    path_coords=path_coords+"/"+"coords.txt"
    currentpath=os.getcwd()
    st = read(path)
    maxstart = np.max([tr.stats.starttime for tr in st])
    minend =  np.min([tr.stats.endtime for tr in st])
    st.trim(maxstart, minend)
    #st.plot(outfile="FKseismigram_Analysis",handle=False)    
    
    #dt=maxstart
    #nr = st.count() #count number of channels

    print("Reading Seismograms")
    print("Loading Array Coordinates ")
    df=pd.read_csv(path_coords,sep='\t')
    n=df.Name.count()

    for i in range(n):

        st[i].stats.coordinates = AttribDict({'latitude': df.loc[i].Lat,'elevation': 0.0,'longitude': df.loc[i].Lon})

    #coord =get_geometry(st, coordsys='lonlat', return_center=True, verbose=True) 
    tr = st[0]
    delta = tr.stats.delta
    fs=1/delta
    stime=UTCDateTime(stime)
    etime=stime+DT
    #stime=tr.stats.starttime+20
    #etime=tr.stats.starttime+(4*60-20)
    
    print("Computing FK")
    kwargs = dict(
        # slowness grid: X min, X max, Y min, Y max, Slow Step
        sll_x=-1*slim, slm_x=slim, sll_y=-1*slim, slm_y=slim, sl_s=sres,
        # sliding window properties
        win_len=win_len, win_frac=win_frac,
        # frequency properties
        frqlow=fmin, frqhigh=fmax, prewhiten=0,
        # restrict output
        semb_thres=-1e9, vel_thres=-1e9, timestamp='mlabday',
        stime=stime, etime=etime)

    nsamp = int(win_len * fs)
    nstep = int(nsamp * win_frac)
    out = array_processing(st, **kwargs)    
         
    xlocator = mdates.AutoDateLocator()
    
    T = out[:,0]
    relpower =  out[:,1]
    AZ=out[:,3]
    AZ[AZ < 0.0] += 360
    Slowness=out[:,4]
    #st.plot(outfile="FKseismigram_Analysis") 
    st.plot() 
    return   relpower,AZ,Slowness,T
        
#relpower,AZ,Slowness,T=FK(path,fmin,fmax,slim,sres,win_len,win_frac)        
        
        
        