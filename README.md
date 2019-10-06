# Guitar Tabs to MIDI
A program that converts Guitar Tabs into MIDI files.

<p align="center">
    <img src="https://drive.google.com/uc?export=view&id=1qUSIVaDX1dRctiqukE79_FbHTousfKcq" height=80 width=480>
    <br><br>
    <img src="https://drive.google.com/uc?export=view&id=1R801JQLlXE_corwf24JJHebBqVCXYYuN" height=260>
</p>


### Working
- Reads the file from the location specified by the user
- Preprocesses the file
    - Removes unwanted characters
    - Maps the notes in the tabs to MIDI pitch information
- Converts the preprocessed output into `.mid` file
    - Sets the tempo and instrument for the track
    - Places the notes into the MIDI file
- Plays the `.mid` file

<br>

##### Mapping
The initial note of each string (open string notes) are mapped to the MIDI pitch as shown in fig. The subsequent notes on the fretboard is the shift from the intial note on that string. `note pitch = inital pitch of string + fret number`
<p align="center">
    <img src="https://drive.google.com/uc?export=view&id=1sTFLfT9__clt_XI-Tg_2G9JIik1Y9WuL" height=200 width=650><br>
    <b><i>Mapping of the fretboard and MIDI pitch</i></b>
</p>

### Requirements
- Python3
- MIDIUtil
- Timidity

### Installation
Install the required files to run on your local system:

- Cloning the repository

      git clone https://github.com/Sarath18/guitar-tabs-to-MIDI

- MIDIUtil

      pip3 install MIDIUtil

- Timidity

      sudo apt-get install timidity

### How to use
Run the program by typing the following in terminal:

    python3 main.py
