#!/usr/bin/python3
from read_tabs import Tabs
from midi_generator import *
import os
import argparse


def main():

    fname = input("Enter file location: ")
    tempo = input("Enter tempo of song: ")
    if tempo == "":
        tempo = 100

    t = Tabs(fname)
    t.preprocess()
    t.displayTabs()
    t.convertNotes()

    outputTrack = Track(int(tempo))
    outputTrack.midiGenerator(t.a)
    command = "timidity output.mid"
    os.system(command)

if __name__ == '__main__':
    main()
