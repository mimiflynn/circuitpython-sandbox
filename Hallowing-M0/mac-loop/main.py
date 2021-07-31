# Just like:
# https://learn.adafruit.com/tiny-museum-tour-device/code-with-circuitpython
# but doesn't require touch to advance... will advance every 5 seconds

import board
from adafruit_slideshow import PlayBackOrder, SlideShow, PlayBackDirection
import time
import audioio
import pulseio
import touchio

# Create the slideshow object that plays through once alphabetically.
slideshow = SlideShow(board.DISPLAY, folder="/",
                      loop=True, order=PlayBackOrder.ALPHABETICAL)

# Create the touch objects on the first and last teeth
back_button = touchio.TouchIn(board.TOUCH1)
forward_button = touchio.TouchIn(board.TOUCH4)

# Setup the speaker output
a = audioio.AudioOut(board.SPEAKER)


# Helper function that takes in the file name string, splits it at the period, and keeps only the
# beginning of the string. i.e. kitten.bmp becomes kitten.
def basename(file_name):
    return file_name.rsplit('.', 1)[0]


# Helper function to handle wav file playback
def play_file(wav_file_name):
    try:
        data = open(wav_file_name, "rb")
        wav = audioio.WaveFile(data)
        a.play(wav)
        print("Playing: " + wav_file_name)
        while a.playing:
            pass
        a.stop()
    except OSError:  # Error thrown if it finds a .bmp file with no corresponding .wav file
        # Print the name of the .bmp file with no corresponding .wav file
        print("No corresponding wav file:", slideshow.current_image_name)


# Uses the basename() helper function to strip the .bmp from the file name and add .wav
wav_file = basename(slideshow.current_image_name) + ".wav"
# Uses the play_file() helper function to play the .wav name now saved to wav_file
play_file(wav_file)

while True:
    # Sets the slideshow playback direction to forward
    slideshow.direction = PlayBackDirection.FORWARD
    # Advance the slideshow to the next image
    slideshow.advance()
    # Sets wav_file to the new corresponding .wav file
    wav_file = basename(slideshow.current_image_name) + ".wav"
    # Plays back the new file with the new image
    play_file(wav_file)
    time.sleep(5)

