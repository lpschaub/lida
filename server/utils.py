################################################################################
# IMPORTS
################################################################################

# >>>> Native <<<<
import os
import json
from typing import Dict, List, Any, Tuple, Hashable, Iterable, Union

# >>>> Packages <<<<
from flask import Response

# >>>> Local <<<<



################################################################################
# CODE
################################################################################

def load_json_file(path: str) -> Any:
    """Loads a JSON file."""
    with open(path, "r") as f:
        content = json.load(f)
    return content


def save_json_file(obj: Any, path: str) -> None:
    """Saves a JSON file."""
    with open(path, "w") as f:
        json.dump(obj, f, indent=4)

import glob

def fusionner(path, out) :

    for fic in glob.glob(path+'/lida*') :

        out.write(open(fic).read()+'===\n\n')


def convert_Convs(fic) :

    out = open('../data/new'+fic.split('/')[-1],'w',encoding='utf-8')
    print(out)
    out.write('SILENCE\n\n')
    speaker = ""
    turns = 1
    for line in open(fic,encoding='utf-8').readlines() :
        turns += 1
        agent = line[8:14]
        if 'fin à la conversation' in line :
            continue
        print(agent)
        if agent == speaker :
            turns += 1
            out.write('SILENCE\n\n')
        speaker = agent
        out.write(line+'\n')
    print(turns)
    if turns %2 == 0 :
        out.write('SILENCE\n\n')

def getFile(file, path, ext) : 
	return open(path+ext+file.split('/')[-1], 'w', encoding='utf-8')

def fb2lida(file, path) :

	out = getFile(file, path, 'lida_')
	out.write("<SILENCE>\n\nbonjour, je suis _Name1_. en quoi puis je vous aider ? afin d'accélérer le traitement de votre dossier, merci de nous indiquer votre adresse email et / ou votre numéro de commande.\n\n")
	for line in open(file).readlines() :
		line = line.split('\t') 
		out.write(line[0]+'\n\n'+line[1]+'\n')

if __name__ == '__main__':


    for fic in glob.glob('../data/*') :
        print(fic)
        fb2lida(fic, '../data/')

    out = open('../data/dialogues.txt','w',encoding='utf-8')
    fusionner('../data', out)
