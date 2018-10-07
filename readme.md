# Guitar Tabs to MIDI
A program that converts Guitar Tabs into MIDI files.

<center><img src="/media/tabs.jpg" height=80 width=480></center>
<br>
<center><img src="/media/output.gif" height=200></center>



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
The initial note of each string (open string notes) are mapped to the MIDI pitch as shown in fig. The subsequent notes on the fretboard is the shift from the intial note on that string.
<center>`note pitch = inital pitch + fret number`</center>
<center><img src="/media/mapping.jpg" height=200 width=650></center>
<center><h6><i>Mapping of the fretboard and MIDI pitch</i></h6></center>

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
