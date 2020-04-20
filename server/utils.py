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


def fusionner(path, out):
    for fic in glob.glob(path + '/*'):
        out.write(open(fic).read() + '\n\n===\n\n\n')


def convert_Convs(fic):
    out = open('../data/new' + fic.split('/')[-1], 'w', encoding='utf-8')
    print(out)
    out.write('SILENCE\n\n')
    speaker = ""
    turns = 1
    for line in open(fic, encoding='utf-8').readlines():
        turns += 1
        agent = line[8:14]
        if 'fin à la conversation' in line:
            continue
        print(agent)
        if agent == speaker:
            turns += 1
            out.write('SILENCE\n\n')
        speaker = agent
        out.write(line + '\n')
    print(turns)
    if turns % 2 == 0:
        out.write('SILENCE\n\n')


def getFile(file, path, ext):
    return open(path + ext + file.split('/')[-1], 'w', encoding='utf-8')


def fb2lida(file, path, segments=False):
    silence = '<SILENCE>'
    out = getFile(file, path, '')
    user_turn = True
    current = ""
    fic = open(file)
    first = fic.readline().rstrip().split('\t')
    print(first)
    fline = ""
    if silence in first[0]:
        user_turn = False
        current += "''\n\nbonjour, je suis _Name1_. en quoi puis je vous aider ? afin d'accélérer le traitement de votre dossier, merci de nous indiquer votre adresse email et / ou votre numéro de commande" + \
                  first[1]
    elif silence in first[1]:
        fline = "''\n\nbonjour, je suis _Name1_. en quoi puis je vous aider ? afin d'accélérer le traitement de votre dossier, merci de nous indiquer votre adresse email et / ou votre numéro de commande\n\n"
        current += first[0]
    else:
        fline = "''\n\nbonjour, je suis _Name1_. en quoi puis je vous aider ? afin d'accélérer le traitement de votre dossier, merci de nous indiquer votre adresse email et / ou votre numéro de commande\n\n" + \
               first[0]+'\n\n'
        user_turn = False
        current += first[1]
    if fline:
        out.write(fline)
    x = 1

    for line in fic.readlines():
        x += 1
        print(f'turn_nbr  {x}')
        print(f'Previous speaker = user : {user_turn}')
        line = line.rstrip().split('\t')
        # out.write(line[0] + '\n\n' + line[1] + '\n')
        # if segments:
        if silence in line[0]:
            print("user silence")
            print(f'AGENT SAYS : {line[1]}')
            current += line[1]
            user_turn = False
        elif silence in line[1]:
            print(f'USER SAYS : {line[0]}')
            print("agent silence")
            if user_turn:
                current += line[0]
            else:
                out.write(current + '\n\n')
                current = line[0]
                user_turn = True
        else:
            print("normal speaking turn")
            print(f'USER SAYS : {line[0]}')
            print(f'AGENT SAYS : {line[1]}')
            if user_turn:
                current += line[0]
                out.write(current + '\n\n')
                current = ""
            else:
                out.write(current + '\n\n' + line[0]+'\n\n')
            user_turn = False

            current = line[1]
    if user_turn :
        current += "\n\nbye"
    out.write(f'{current}')
import sys

if __name__ == '__main__':

    x  = 0
    for fic in glob.glob('../data/input/conv*'):
        print(fic)
        x += 1
        fb2lida(fic, '../data/segments/')
        if x == 500 :
            break

    out = open('../data/dialogues.txt', 'w', encoding='utf-8')
    fusionner('../data/segments', out)
