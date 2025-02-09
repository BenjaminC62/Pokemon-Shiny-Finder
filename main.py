import os

import pyautogui
import time
import cv2
import numpy as np
import platform
import locale
from mouseinfo import screenshot
from pyautogui import press

key_skip = "shift"
endroit_a_check = (277, 250, 365, 279) # (X, Y, Largeur, Hauteur)
starter_reference = cv2.imread("pokemon.png", cv2.IMREAD_GRAYSCALE)
game = "https://www.fandesjeux.com/jouer/pokemon-noir"
cord_play = (468,600)
cord_play_download = (468,820)

def load_savestate():
    """loads the savestate of the game"""
    pyautogui.keyDown("shift") # hold shift
    pyautogui.press("f4")
    pyautogui.keyUp("shift")
    time.sleep(2)
    pyautogui.click(242, 341)

def create_savestate():
    """creates a savestate of the game"""
    pyautogui.keyDown("shift") # hold shift
    pyautogui.press("f2")
    pyautogui.keyUp("shift")
    time.sleep(2)
    pyautogui.click(465, 535)
    time.sleep(2)


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

    if np.all(screenshot == 0) or np.all(screenshot == 255):
        print("L'écran est tout noir ou tout blanc.")
        return False


    result = cv2.matchTemplate(screenshot, starter_reference, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    if max_val == 1:
        print("L'écran est tout blanc. val 1")
        return False

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


def click_play(cord):
    """clicks the play button"""
    pyautogui.click(cord)
    time.sleep(10)

def open_firefox_and_game():
    """Open firefox and type in the search bar the url of the game"""
    if platform.system() == "Windows":
        pyautogui.hotkey('win', 'r')
    else:
        pyautogui.hotkey('ctrl', 'alt', 't')
    time.sleep(1)
    pyautogui.typewrite('firefox\n')
    time.sleep(2)
    if locale.getlocale()[0] == "fr_FR":
        pyautogui.typewrite(game + '\n')
    time.sleep(3)

def main():
    """execute the main program, which is a while loop that takes screenshots and saves them to a folder of a non shiny pokemon on the first run
    then it will compare the screenshots to the original image to see if the pokemon is shiny or not, then repeat the process if the pokemon is not shiny"""
    # Cheat shiny 521A96D0 1C221C39

    open_firefox_and_game()
    click_play(cord_play)
    click_play(cord_play_download)

    pyautogui.moveTo(cord_play)

    time.sleep(15)

    start_time = time.time()
    while not is_starter_screen_visible():
        pyautogui.keyDown("shift")
        time.sleep(0.2)
        pyautogui.keyUp("shift")
        print("Voci les sec = ", time.time() - start_time)
        if time.time() - start_time > 10:
            create_savestate()
            time.sleep(2)
            pyautogui.keyDown("s")
            time.sleep(444)
            pyautogui.keyUp("s")


    time.sleep(5)

    chose_starter()


if __name__ == "__main__":
        main()
