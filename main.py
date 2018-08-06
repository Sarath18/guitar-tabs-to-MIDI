#!/usr/bin/python3
from read_tabs import Tabs
from midi_generator import *
import os

def main():
    fname = "/home/sarath/tabs_to_midi/tab.txt"
    t = Tabs(fname)
    t.preprocess()
    t.displayTabs()
    t.convertNotes()


    outputTrack = Track()
    outputTrack.midiGenerator(t.a)
    command = "timidity output.mid"
    os.system(command)

if __name__ == '__main__':
    main()
