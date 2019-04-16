import pandas as pd
import pprint
pp = pprint.PrettyPrinter(indent=4)

def startupRankLoc(location):
    startup_dict = {}
    # csv = open("START.csv","r","encoding = utf-8")
    dataset = pd.read_csv("datasets/startup_ranking.csv",delimiter=',', names = ['rank', 'startup', 'startup_logo', 'sr_score', 'description', 'location','none'])
    startupLoc = dataset[dataset.location == 'Canada'].head(10)
    startupLoc = startupLoc.to_dict('index')
    pp.pprint(startupLoc)
    return startupLoc

startupRankLoc('Canada')
