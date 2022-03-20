# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:55:30 2022

@author: ely97
"""
import numpy as np
# FPATT = "Weights/pattsN100S20P0.dat"
# prova = np.loadtxt(fname=FPATT, dtype='int16')
# ciccio = np.transpose(np.loadtxt(fname=FPATT, dtype='int16'))
# Ciccio = np.transpose(np.loadtxt(fname=FPATT, dtype='int16'))
# print(prova)
# print('ciccio')
# print(ciccio)
nPyramidal=100 
nCA3=100
nEC=20 #must be equal to the active pyr cells in the pattern
nSEP=10
nOLM=1
nBS=1
nB=2
nAA=1
PATTi = 0

FPATT = "Weights/pattsN100S20P5.dat"
PATTS = np.transpose(np.loadtxt(fname=FPATT, dtype='int16'))
patts = np.transpose(np.loadtxt(fname=FPATT, dtype='int16'))


lista_EC2Pyramidal=[] #to check which pyr cells are active in the pattern

temp = FPATT[len("Weights/pattsN100S20"):-(len(".dat"))]
##each EC cell will stimulate every active pyr cell in the pattern
for i in range(20):
 	for j in range(100):
         if temp == "P0" or temp == "P1":
             if PATTS[j]:
                 lista_EC2Pyramidal.append([i,j])    
         elif PATTS[0][j]:
             lista_EC2Pyramidal.append([i,j])
             
             
             
FCONN = "Weights/wgtsN100S20P5.dat"		#weights matrix generated with matlab file
#WGTCONN = np.transpose(np.loadtxt(fname=FCONN, dtype='int16')) #each column has the weights for one pyramidal cell
WGTCONN = (np.loadtxt(fname=FCONN, dtype='int16')) #each column has the weights for one pyramidal cell

#############################
####CA3 -> INHIBITORY CELLS
############################

lista_CA3active=[]
###connect CA3 input to all pyramidal cells but with different weights according to the WGTCONN[i][j] value
lista_CA3highW=[]
lista_CA3lowW=[]

# for i in range(nCA3):
#  	if PATTS[PATTi][i]:    ##ONLY CONNECTIONS FROM ACTIVE CA3 CELLS IN THE PATTERN
#  		 lista_CA3active.append(i)
          
for i in range(nCA3):
    if temp == "P0" or temp == "P1":
        if PATTS[i]:
            lista_CA3active.append(i)    
    elif PATTS[PATTi][i]:
        lista_CA3active.append(i)              
          

# for i in lista_CA3active:  ##ONLY CONNECTIONS FROM ACTIVE CA3 CELLS IN THE PATTERN
#  	for j in range(nPyramidal):
#  			if WGTCONN[i][j]:
#  			 	lista_CA3highW.append([i,j])
#  			else: lista_CA3lowW.append([i,j])
             
             
for i in range(nCA3):  ##FULL CONNECTIVITY
 	for j in range(nPyramidal):
 			if WGTCONN[i][j]:
 				 lista_CA3highW.append([i,j])
 			else: lista_CA3lowW.append([i,j])         
             
             

postsynList=['AA','Basket','BS']
postsynDict={'AA': ['radM1','radM2','radT1', 'radT2'], 'Basket':['radM1','radM2','radT1', 'radT2'], 'BS':['radM1','radM2','radT1', 'radT2']}

cellnums={'Basket':nB, 'AA': nAA, 'BS': nBS, 'OLM': nOLM}
list=[]
connections={}

for j in postsynList:
 	num=0
 	list=[]
 	connections[j]= list
 	for i in range(cellnums[j]):
 		 for k in lista_CA3active: list.append([k,i])     
          
          
FPATT = "Weights/pattsN100S20P5.dat"	#already stored patterns: each column is a pattern. Each line is a CA1 pyramidal cell
PATTS = np.transpose(np.loadtxt(fname=FPATT, dtype='int16')) #each column is a pattern - 100 lines (one per pyramidal cell)

  

lista_CA3active=[]              
for j in range(nCA3):
    if temp == "P0" or temp == "P1":
        if PATTS[j]:
            lista_CA3active.append(j)    
    elif PATTS[PATTi][j]:
        lista_CA3active.append(j)