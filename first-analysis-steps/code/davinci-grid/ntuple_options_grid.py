from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *
from Configurables import DaVinci

# Stream and stripping line we want to use
stream = 'AllStreams'
line = 'D2hhPromptDst2D2KKLine'

# Create an ntuple to capture D*+ decays from the StrippingLine line
dtt = DecayTreeTuple('TupleDstToD0pi_D0ToKK')
dtt.Inputs = ['/Event/{0}/Phys/{1}/Particles'.format(stream, line)]
dtt.Decay = '[D*(2010)+ -> (D0 -> K- K+) pi+]CC'

# Configure DaVinci
DaVinci().UserAlgorithms += [dtt]
DaVinci().InputType = 'DST'
DaVinci().TupleFile = 'DVntuple.root'
DaVinci().PrintFreq = 1000
DaVinci().DataType = '2016'
DaVinci().Simulation = True
# Only ask for luminosity information when not using simulated data
DaVinci().Lumi = not DaVinci().Simulation
DaVinci().EvtMax = -1
DaVinci().CondDBtag = 'sim-20170721-1-vc-mu100'
DaVinci().DDDBtag = 'dddb-20171005-3'
