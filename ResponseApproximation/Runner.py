from ResponseApproximation.Handlers.StatHandler import StatHandler
from ResponseApproximation.Handlers.Analysis import Analysis

stat = StatHandler
analysis = Analysis

data = StatHandler.getData()
analysis.plotGraph(data, 2)
