import pyttsx3
import logging
import config

class TexttoSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    # Setting the
    def set_rate(self):
        rate = self.engine.getProperty('rate')  # getting details of current speaking rate
        logging.info(f"The current rate is {rate}")  # logging current voice rate
        self.engine.setProperty('rate', config.RATE_OF_SPEAKING)  # setting up new voice rate
        logging.info(f"Rate is set to {config.RATE_OF_SPEAKING}")

    # Setting the voice in which the audiobook will be recorded
    def set_volume(self):
        volume = self.engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        logging.info(f"The current volume is {volume}")  # logging current volume level
        self.engine.setProperty('volume', config.VOLUME)  # setting up volume level  between 0 and 1
        logging.info(f"The volume is set to {config.VOLUME}")

    # Setting whether the audiobook will be recorded in MALE or FEMALE voice
    def set_voice(self):
        voices = self.engine.getProperty('voices')  # getting details of current voice
        if config.MALE_VOICE:
            self.engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        else:
            self.engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
        logging.info("The voice has been set to the required voice")

    # Saving the voice to a file finally after all the properties has been set
    def text_to_speech(self, file_contents):
        self.engine.save_to_file(file_contents, config.PATH_OF_AUDIOBOOK)
        self.engine.runAndWait()
        logging.info(" Book to audio-book complete, exiting")
        return