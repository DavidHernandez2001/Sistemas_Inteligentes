# main.py
from open_program import ProgramOpener
from capture_colors import ColorCapture
from analyze_colors_cv import ColorAnalyzerCv
from ia_cv import IaCv

import time


def main():
    program_path = "/Users/avhernandez/Downloads/ruffle-nightly-2023_08_28-macos-universal/Ruffle.app"
    opener = ProgramOpener()
    opener.open_program(program_path)

    # Espera 5 segundos y luego realiza clic en las coordenadas (x, y) del botón
    opener.click_button_with_delay(1002, 450, 1)
    opener.click_button_with_delay(714, 390, 1)
    opener.click_button_with_delay(1223, 599, 1)
    opener.click_button_with_delay(1016, 531, 1)

    capture = ColorCapture()
    capture.capture_active_window_after_delay(24)

    tiempo_inicio = time.time()
    duracion = 4 * 60 + 5

    while True:
        image_path = "/Users/avhernandez/Documents/Universidad/Sistemas_inteligentes/candy/captura.png"
        rows, cols = 9, 9

        analyzer = ColorAnalyzerCv()
        color_matrix = analyzer.extract_image_from_caramel_grid(image_path, rows, cols)

        # Contar la cantidad de elementos 'x' en la lista
        count_x = sum(1 for row in color_matrix for item in row if item[0][0] == 'x')
        print(count_x)

        # Verificar si la cantidad es mayor que 10
        while count_x > 25:
            capture.capture_active_window_after_delay(0.2)
            color_matrix = analyzer.extract_image_from_caramel_grid(image_path, rows, cols)
            count_x = sum(1 for row in color_matrix for item in row if item[0][0] == 'x')
            print(count_x)

        ia = IaCv()
        possible_moves = ia.find_moves_to_connect(color_matrix)
        ia.send_move(possible_moves)

        capture.capture_active_window_after_delay(0.8)

        tiempo_actual = time.time()

        tiempo_transcurrido = tiempo_actual - tiempo_inicio

        if tiempo_transcurrido >= duracion:
            break


if __name__ == "__main__":
    main()
