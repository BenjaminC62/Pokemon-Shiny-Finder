import pyautogui
import time
import cv2
import numpy as np
from mouseinfo import screenshot

key_skip = "shift"
endroit_a_check = (277, 250, 365, 279) # (X, Y, Largeur, Hauteur)
starter_reference = cv2.imread("pokemon.png", cv2.IMREAD_GRAYSCALE)
game = "https://www.fandesjeux.com/jouer/pokemon-noir"

def load_savestate():
    """loads the savestate of the game"""
    pyautogui.keyDown("shift") # hold shift
    pyautogui.press("f4")
    pyautogui.keyUp("shift")

def is_starter_screen_visible():
    """Vérifie si l'écran de sélection du starter est affiché"""
    screenshot = pyautogui.screenshot(region=endroit_a_check)
    screenshot.save("screenshot.png")
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Verif pour ecran noir ou blanc
    if np.all(screenshot == 0):
        print("L'écran est tout noir.")
        return False

    if np.all(screenshot == 255):
        print("L'écran est tout blanc.")
        return False

    result = cv2.matchTemplate(screenshot, starter_reference, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    print(max_val > 0.8)
    print(max_val)

    return max_val > 0.8

def chose_starter():
    """chooses the starter pokemon"""
    pyautogui.keyDown("right")
    time.sleep(0.1)
    pyautogui.keyUp("right")
    pyautogui.keyDown("shift")
    time.sleep(0.1)
    pyautogui.keyUp("shift")
    pyautogui.keyDown("shift")
    time.sleep(0.1)
    pyautogui.keyUp("shift")
    time.sleep(3)
    pyautogui.keyDown("shift")
    time.sleep(0.1)
    pyautogui.keyUp("shift")

def is_shiny():
    """checks if the pokemon is shiny"""
    screenshot = pyautogui.screenshot(region=endroit_a_check)

def open_firefox_and_game():
    """Open firefox and type in the search bar the url of the game"""
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.typewrite('firefox\n')
    time.sleep(2)
    pyautogui.typewrite(game + '\n')

def main():
    """execute the main program, which is a while loop that takes screenshots and saves them to a folder of a non shiny pokemon on the first run
    then it will compare the screenshots to the original image to see if the pokemon is shiny or not, then repeat the process if the pokemon is not shiny"""
    #load_savestate()
    # Cheat shiny 521A96D0 1C221C39

    open_firefox_and_game()

    time.sleep(5)

    while not is_starter_screen_visible():
        pyautogui.keyDown("shift")
        time.sleep(0.2)
        pyautogui.keyUp("shift")

    time.sleep(5)

    chose_starter()


if __name__ == "__main__":
        main()