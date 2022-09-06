logo = """
                )                      )      *        )   (    (         
  *   )      ( /(   *   )    *   )  ( /(    (  `    ( /(   )\ ) )\ )      
` )  /( (    )\())` )  /(  ` )  /(  )\())   )\))(   )\()) (()/((()/( (    
 ( )(_)))\  ((_)\  ( )(_))  ( )(_))((_)\   ((_)()\ ((_)\   /(_))/(_)))\   
(_(_())((_) __((_)(_(_())  (_(_())   ((_)  (_()((_)  ((_) (_)) (_)) ((_)  
|_   _|| __|\ \/ /|_   _|  |_   _|  / _ \  |  \/  | / _ \ | _ \/ __|| __| 
  | |  | _|  >  <   | |      | |   | (_) | | |\/| || (_) ||   /\__ \| _|  
  |_|  |___|/_/\_\  |_|      |_|    \___/  |_|  |_| \___/ |_|_\|___/|___| 
                                                                          
"""
# Create a dictionary of Morse codes
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                   'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
                   '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                   ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
                   '-': '-....-', '(': '-.--.', ')': '-.--.-'}
app_is_on = True


# Check for invalid characters
def check_chars(text):
    for ch in text:
        if ch != " " and ch not in MORSE_CODE_DICT:
            print("Please enter only english alphabet and numbers.")
            return False
    return True


print(logo)
print("Welcome to text to morse code convertor.\n"
      "Please type your message to convert of type 'exit' to close the app.")
while app_is_on:
    # Get input form user
    message = input("Please write your message:\n").upper()
    if message == "EXIT":
        app_is_on = False
        break

    morse_output = ""
    if check_chars(message):
        # Convert each char to a morse code
        for char in message:
            if char == " ":
                morse_output += " / "
            else:
                morse_output += MORSE_CODE_DICT[char] + " "
        # print output
        print(morse_output)
