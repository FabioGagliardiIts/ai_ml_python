import sys
import pandas as pd


if __name__ == '__main__':
    # argv è l'array di comandi passati 
    # da linea di comando.
    # argv[0]: è il nome stesso dello script
    # argv[n]: tutti gli indici dopo lo zero 
    #          riportano la serie dei comandi
    # es.
    # python test_cl.py "filename.csv"
    #        argv[0]    argv[1]
    filename = sys.argv[1]
    pd.read_csv(filename)
