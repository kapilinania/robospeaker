import pyttsx3
if __name__ == '__main__':
    while True:
        print("Welcome to Robo Speaker: Create By Kapil Inania")
        x = input("Enter what you want me to speak: ")
        if x == "q":
            break

        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()

        # Get the current speech rate
        current_rate = engine.getProperty('rate')

        # Set a slower speech rate (adjust the value as needed)
        engine.setProperty('rate', current_rate - 100)

        # Speak the provided text
        engine.say(x)

        # Wait until speech is complete
        engine.runAndWait()
