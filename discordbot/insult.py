import os
import sys
import random

adjSet = ['Lazy', 'Stupid', 'Insecure', 'Idiotic', 'Slimey', 'Slutty', 'Smelly',
                'Pompous', 'Communist', 'Dick-nose', 'Pie-eating', 'Racist', 'Elitist',
                'White trash', 'Drug-loving', 'Butterface', 'Tone deaf', 'Ugly', 'Creepy']

modSet = ['douche', 'ass', 'turd', 'rectum', 'butt', 'cock', 'shit', 'crotch', 'bitch',
          'prick','slut', 'taint', 'fuck', 'dick', 'boner', 'shart', 'nut', 'sphincter']

nounSet = ['pilot', 'canoe', 'captain', 'pirate', 'hammer', 'knob', 'box', 'jockey',
           'nazi', 'waffle', 'goblin', 'blossum', 'biscuit', 'clown', 'socket',
           'monster', 'hound', 'dragon', 'balloon']

def insult():
    randAdj = random.randint(0,(len(adjSet)-1))
    randMod = random.randint(0,(len(modSet)-1))
    randNoun = random.randint(0,(len(nounSet)-1))

    insult = []

    adj = adjSet[randAdj]
    insult.append(adj)
    
    mod = modSet[randMod]
    insult.append(mod)
    
    noun = nounSet[randNoun]
    insult.append(noun)
    
    return insult
