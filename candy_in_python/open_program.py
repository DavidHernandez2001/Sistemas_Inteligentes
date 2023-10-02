# open_program.py
import subprocess
import time
import pyautogui


class ProgramOpener:
    def open_program(self, program_path):
        try:
            subprocess.run(["open", "-a", program_path])
            print(f"Program {program_path} opened successfully.")
        except Exception as e:
            print("Error opening the program:", str(e))

    def click_button_with_delay(self, button_x, button_y, delay):
        time.sleep(delay)
        try:
            pyautogui.click(button_x, button_y)
            print("Clic realizado en las coordenadas:", button_x, button_y)
        except Exception as e:
            print("Error al hacer clic:", str(e))
