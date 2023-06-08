import pyautogui
import time


class autoFisher():
    def __init__(self):
        self.time_tick = 0
        self.items_caught = 0

        self.confidence = 0.725
        self.coordinates = (750, 150, 1110, 500)

    def reel(self):
        """
        Clicks the right button in the right sequence to reel in and rethrow a fishing hook.
        """
        pyautogui.click(button='right')
        time.sleep(0.5)
        pyautogui.click(button='right')
        time.sleep(3)

    
    def displayMessage(self, message):
        """
        Prints a log message to the terminal, 
        containing the info for the current status and catch count.
        """ 
        icon = "".join(["▰" for i in range(self.time_tick)] +
                       ["▱" for i in range(3-self.time_tick)])

        print(f"\r{icon} | {message} | Count: {self.items_caught}", end='', flush=True)
    
    
    
    def loop(self):
        """
        The main loop of the program. Tries to detect the bobber as given in bobber.png.
        If there is not one detected, it's presumed to be dragged down by a fish, so a reel action is executed.
        """ 
        while True:  
            if pyautogui.locateOnScreen('bobber.png',
                                        confidence = self.confidence,
                                        region = self.coordinates):
                self.displayMessage("Awaiting catch")
            
            else:
                self.displayMessage("Catch detected")
                self.items_caught += 1
                self.reel()

            time.sleep(0.4)
            self.time_tick = (self.time_tick + 1) % 4



if __name__ == '__main__':
    fisher = autoFisher()
    fisher.loop()
