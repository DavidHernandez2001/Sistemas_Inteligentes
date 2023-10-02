# analyze_colors.py
from PIL import Image, ImageOps


class ColorAnalyzer:
    def extract_pixels_from_grid(self, image_path, rows, cols, distance_from_center=5):
        # Abre la imagen utilizando PIL
        image = Image.open(image_path)

        # Obtiene las dimensiones de la imagen
        width, height = image.size

        # Calcula el tamaño de cada espacio en la cuadrícula
        cell_width = width // cols
        cell_height = height // rows

        # Lista para almacenar los píxeles extraídos
        extracted_pixels = []

        for row in range(rows):
            for col in range(cols):
                # Calcula las coordenadas del píxel a 5 píxeles a la izquierda del centro
                center_x = col * cell_width + cell_width // 2
                center_y = row * cell_height + cell_height // 2
                pixel_x = center_x - distance_from_center
                pixel_y = center_y

                # Obtiene el color del píxel en las coordenadas especificadas
                pixel_color = image.getpixel((pixel_x, pixel_y))

                # Añade el color del píxel extraído a la lista
                extracted_pixels.append((pixel_color, (pixel_x + 568, pixel_y + 203)))

        return extracted_pixels

    def classify_colors_as_matrix(self, colors_list, rows, cols):
        # Inicializa una matriz para almacenar la clasificación de colores
        color_matrix = [['' for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                # Obtiene el índice correspondiente en la lista de colores
                index = row * cols + col

                # Obtiene el color del píxel en el índice actual
                pixel_color = colors_list[index][0]

                # Analiza el color del píxel
                r, g, b = pixel_color[:3]
                #print(pixel_color[:3])

                # Ajusta el umbral de detección para cada color
                threshold_red = 200
                threshold_blue = 200
                threshold_green = 200  # Nuevo umbral para el verde

                # Detección de colores
                if r > threshold_red:
                    if g > threshold_green:
                        color_matrix[row][col] = ['y', colors_list[index][1]]
                    elif b < 60 and 120 < g < 160:
                        color_matrix[row][col] = ['o', colors_list[index][1]]
                    else:
                        color_matrix[row][col] = ['r', colors_list[index][1]]
                elif b > threshold_blue:
                    if g < 60 and 120 < r < 200:
                        color_matrix[row][col] = ['p', colors_list[index][1]]
                    else:
                        color_matrix[row][col] = ['b', colors_list[index][1]]
                elif 140 < g and 60 < r:
                    color_matrix[row][col] = ['g', colors_list[index][1]]
                # Si no se reconoce como ningún color, se devuelve un valor predeterminado
                else:
                    color_matrix[row][col] = ['E', colors_list[index][1]]
        return color_matrix

