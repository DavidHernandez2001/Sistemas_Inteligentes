# capture_colors.py
import pyscreenshot
import time


class ColorCapture:
    def capture_active_window_after_delay(self, delay):
        time.sleep(delay)
        image = pyscreenshot.grab(bbox=(568, 203, 1208, 765))
        image.save('captura.png')


