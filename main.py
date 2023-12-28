from app.entrypoints.voice_listener import VoiceListener

def main():
  while True:
    if VoiceListener.listen_for_trigger():
      pass

if __name__ == "__main__":
  main()