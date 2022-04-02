from netpyne import specs, sim
# from netParams import STARTDEL, THETA

#############################################
####		SIMULATION PARAMETERS		#####
#############################################

cfg = specs.SimConfig()

STARTDEL = 50.	# msecs
THETA = 250.	 # msecs (4 Hz)

cfg.dt = 0.05                 # Internal integration timestep to use
cfg.verbose = 0
cfg.duration = 1
#cfg.duration = STARTDEL + THETA*8
# cfg.duration = STARTDEL + THETA
cfg.recordStim = True
cfg.recordStep = 0.1             # Step size in ms to save data (e.g. V traces, LFP, etc)
sim.updateInterval = STARTDEL + THETA*4

cfg.hParams['celsius'] = 34.

cfg.filename = 'AAABBBCCC'
cfg.saveJson = True
#cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}} #, 'V_lmT':{'sec':'lm_thick1','loc':0.5,'var':'v'}}  # Dict with traces to record
#cfg.analysis['plotTraces'] = {'include': [('Pyramidal',[0,1]),('AA',0),('Basket',[0,1]),('OLM',0),('BS',0)], 'oneFigPer':'trace', 'overlay':1}
#cfg.analysis['plotRaster'] = True   # Plot a raster
#cfg.analysis['plotRaster'] = {'saveData': True, 'saveFig': True} # Plot raster
#cfg.analysis['plotRaster'] = {'saveFig': True} # Plot raster

#cfg.analysis['plot2Dnet'] = True
#cfg.analysis['plot2Dnet'] = {'include': [('AA',0),('Basket',[0,1]),('OLM',0),('BS',0)],'saveData': 'conns.json', 'saveFig': True, 'showFig': True} # Plot 2D cells and connections

cfg.saveDataInclude=['simData', 'netParams', 'simConfig','net']

# cfg.saveMat=True

# cfg.recordLFP = [[netParams.sizeX/2, netParams.sizeY*1/4, netParams.sizeZ/2], 
# 						[netParams.sizeX/2, netParams.sizeY*2/4, netParams.sizeZ/2],
# 						[netParams.sizeX/2, netParams.sizeY*3/4, netParams.sizeZ/2]]

# cfg.recordLFP = [[x,y,z] for x in range(900, netParams.sizeX, 900) for y in range(40, netParams.sizeY, 40) for z in range(40, netParams.sizeZ, 40)]

# For batch simulations
cfg.remove_EC_Conns = 0
