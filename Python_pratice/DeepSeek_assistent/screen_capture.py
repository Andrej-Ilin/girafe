import mss
import numpy as np
import cv2

region = None  # Область экрана для захвата

def select_screen_region():
    global region
    with mss.mss() as sct:
        screen = np.array(sct.grab(sct.monitors[1]))  
        screen = cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)
        r = cv2.selectROI("Выберите область экрана", screen, False, False)
        cv2.destroyAllWindows()

        if r[2] > 0 and r[3] > 0:
            region = {"top": int(r[1]), "left": int(r[0]), "width": int(r[2]), "height": int(r[3])}
    return region

def capture_screen(region):
    with mss.mss() as sct:
        screen = sct.grab(region if region else sct.monitors[1])
        img = np.array(screen)[:, :, :3]  
    return img