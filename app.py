from googletrans import Translator
from pyautogui import press
from pyperclip import paste, copy

press("c")
copy(Translator().translate(paste(), src='ja', dest='en').text)
press("v")
