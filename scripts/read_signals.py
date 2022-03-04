#!/usr/bin/env python

import os.path
import time

SPEECH_SIGNALS_FILENAME="/tmp/signals/speech.txt"
FACING_SIGNALS_FILENAME="/tmp/signals/face_detections.txt"

ON_WORDS = {"on", "one"}
OFF_WORDS = {"off", "of"}

is_light_on = False

while True:
    if not os.path.exists(SPEECH_SIGNALS_FILENAME):
        time.sleep(0.1)
        continue

    if os.path.exists(FACING_SIGNALS_FILENAME):
      with open(SPEECH_SIGNALS_FILENAME, "r") as speech_signals_file:
          last_sentence = speech_signals_file.read()

      if last_sentence in ON_WORDS:
          if not is_light_on:
              is_light_on = True
              print("Light on")

      if last_sentence in OFF_WORDS:
          if is_light_on:
              is_light_on = False
              print("Light off")

      os.remove(SPEECH_SIGNALS_FILENAME)
