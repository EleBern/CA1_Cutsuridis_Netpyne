from netpyne import sim
from neuron import gui
from netpyne.specs import Dict
# from cfg import simConfig
# from netParams import netParams
from netParams import STARTDEL, THETA, lista_CA3active

# read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='nrn_cfg.py', netParamsDefault='netParams.py')

def removeStore(simTime):
    # ECWGT = 0.001
    ECWGT = 0.0
    sim.net.modifyConns({'conds': {'label': 'EC->Pyramidal'}, 'weight': ECWGT})
    STDPDFAC = 0.0
    STDPPFAC = 0.0 
    # STDPDFAC = 0.2	# depression factor
    # STDPPFAC = 1.0	# potentiation factor
    sim.net.modifySynMechs({'conds': {'label': 'STDP'}, 'd': STDPDFAC}) #'d': STDPDFAC,
    sim.net.modifySynMechs({'conds': {'label': 'STDP'}, 'p' : STDPPFAC})
    print('Check')
    print(simTime)
    
    
# sim.createSimulateAnalyze(netParams, simConfig)
sim.create() 
CA3Gid = sim.net.pops['CA3'].cellGids[0]
for i in range(len(lista_CA3active)):
    lista_CA3active[i] += CA3Gid
    
# Turn on CA3 cells that are active in the pattern to store/recall
for cell in sim.net.cells:
    if cell.gid in lista_CA3active:
        # `hPointp` is the reference to hoc object created according to .mod file.
        # Generally, one can modify all params that passed through `netParams.popParams` when setting up the network:
        cell.hPointp.number = 1000
    
    
sim.runSimWithIntervalFunc(sim.updateInterval, removeStore) #, timeRange=[THETA*3, THETA*5])
sim.analyze()

# additional plots
#sim.analysis.plotTraces([('Pyramidal',1),('Basket',0)], saveFig=1, oneFigPer='trace', overlay=0)
# sim.analysis.plotConn(graphType='matrix', saveFig=1)
# sim.analysis.plotConn(graphType='bar', saveFig=1)
# sim.analysis.plotSpikeStats(stats = ['rate', 'isicv', 'sync', 'pairsync'], saveFig=1)
# sim.analysis.plotLFP(NFFT=256*10, noverlap=48*10, nperseg=64*10, saveFig=True)
# sim.analysis.granger(cells1=['EC'], cells2=['Pyramidal'], label1='EC', label2='Pyramidal')

# create and plot
#sim.saveData()

#sim.create()
#sim.analysis.plot2Dnet(include = ['AA', ('EC',[0,1,2]),('Pyramidal',[0,1,2]), ('CA3',[0,1,2])])
#sim.analysis.plotConn(include = ['allCells'], feature='strength', groupBy= 'pop', figSize=(9,9), showFig=True)
#sim.analysis.plotShape(includePost= ['Pyramidal','AA','Basket','BS','OLM'], showFig=True, includeAxon=True, showSyns=True)
#sim.analysis.plotRaster(include = ['CA3', lista_CA3active])
