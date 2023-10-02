import cv2


class ColorAnalyzerCv:
    def extract_image_from_caramel_grid(self, image_path, rows, cols):
        # Leer la imagen utilizando OpenCV
        image = cv2.imread(image_path)

        # Obtener las dimensiones de la imagen
        height, width, _ = image.shape

        # Calcular el tamaño de cada espacio en la cuadrícula
        cell_width = width // cols
        cell_height = height // rows

        # Lista para almacenar los píxeles extraídos
        color_matrix = [['' for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                # Calcular las coordenadas del píxel a 5 píxeles a la izquierda del centro
                center_x = col * cell_width + cell_width // 2
                center_y = row * cell_height + cell_height // 2
                if row > 6:
                    center_y = center_y + 7
                if row == 3 or row == 4 or row == 5:
                    center_y = center_y + 3
                if row == 6:
                    center_y = center_y + 5

                # Extraer la imagen en las coordenadas especificadas
                if row == 0 and col == 3:
                    left_image = image[center_y - 30:center_y + 25, center_x - 25:center_x - 5]
                    right_image = cv2.flip(left_image, 1)
                    extracted_image_size = cv2.hconcat([left_image, right_image])
                    extracted_image = cv2.resize(extracted_image_size, (50, 55))
                elif row == 0 and col == 4:
                    right_image = image[center_y - 30:center_y + 25, center_x:center_x + 25]
                    left_image = cv2.flip(right_image, 1)
                    extracted_image = cv2.hconcat([left_image, right_image])
                else:
                    extracted_image = image[center_y - 30:center_y + 25, center_x - 25:center_x + 25]

                # guardar la imagen extraida en la carpeta assets/extracted
                cv2.imwrite('assets/extracted/extracted_image_' + str(row) + '_' + str(col) + '.png', extracted_image)

                # Rutas de las imágenes a comparar
                referencia = 'assets/extracted/extracted_image_' + str(row) + '_' + str(col) + '.png'
                imagen1 = 'assets/references/blue_candy.png'
                imagen2 = 'assets/references/red_candy.png'
                imagen3 = 'assets/references/green_candy.png'
                imagen4 = 'assets/references/purpule_candy.png'
                imagen5 = 'assets/references/yellow_candy.png'
                imagen6 = 'assets/references/orange_candy.png'

                # Establecer un umbral de similitud
                umbral = 2000.0

                # Calcular la similitud de color entre las dos imágenes
                similitud_color1 = self.color_similarity(referencia, imagen1)
                similitud_color2 = self.color_similarity(referencia, imagen2)
                similitud_color3 = self.color_similarity(referencia, imagen3)
                similitud_color4 = self.color_similarity(referencia, imagen4)
                similitud_color5 = self.color_similarity(referencia, imagen5)
                similitud_color6 = self.color_similarity(referencia, imagen6)

                if similitud_color1 < umbral:
                    color_matrix[row][col] = [('b', 1), (center_x + 568, center_y + 203)]
                elif similitud_color2 < umbral:
                    color_matrix[row][col] = [('r', 1), (center_x + 568, center_y + 203)]
                elif similitud_color3 < umbral:
                    color_matrix[row][col] = [('g', 1), (center_x + 568, center_y + 203)]
                elif similitud_color4 < umbral:
                    color_matrix[row][col] = [('p', 1), (center_x + 568, center_y + 203)]
                elif similitud_color5 < umbral:
                    color_matrix[row][col] = [('y', 1), (center_x + 568, center_y + 203)]
                elif similitud_color6 < umbral:
                    color_matrix[row][col] = [('o', 1), (center_x + 568, center_y + 203)]
                else:
                    imagen1 = 'assets/references/blue_vertical_candy.png'
                    imagen2 = 'assets/references/red_vertical_candy.png'
                    imagen3 = 'assets/references/green_vertical_candy.png'
                    imagen4 = 'assets/references/purpule_vertical_candy.png'
                    imagen5 = 'assets/references/yellow_vertical_candy.png'
                    imagen6 = 'assets/references/orange_vertical_candy.png'

                    similitud_color1 = self.color_similarity(referencia, imagen1)
                    similitud_color2 = self.color_similarity(referencia, imagen2)
                    similitud_color3 = self.color_similarity(referencia, imagen3)
                    similitud_color4 = self.color_similarity(referencia, imagen4)
                    similitud_color5 = self.color_similarity(referencia, imagen5)
                    similitud_color6 = self.color_similarity(referencia, imagen6)

                    if similitud_color1 < umbral:
                        color_matrix[row][col] = [('b', 4), (center_x + 568, center_y + 203)]
                    elif similitud_color2 < umbral:
                        color_matrix[row][col] = [('r', 4), (center_x + 568, center_y + 203)]
                    elif similitud_color3 < umbral:
                        color_matrix[row][col] = [('g', 4), (center_x + 568, center_y + 203)]
                    elif similitud_color4 < umbral:
                        color_matrix[row][col] = [('p', 4), (center_x + 568, center_y + 203)]
                    elif similitud_color5 < umbral:
                        color_matrix[row][col] = [('y', 4), (center_x + 568, center_y + 203)]
                    elif similitud_color6 < umbral:
                        color_matrix[row][col] = [('o', 4), (center_x + 568, center_y + 203)]
                    else:
                        imagen1 = 'assets/references/blue_horizontal_candy.png'
                        imagen2 = 'assets/references/red_horizontal_candy.png'
                        imagen3 = 'assets/references/green_horizontal_candy.png'
                        imagen4 = 'assets/references/purpule_horizontal_candy.png'
                        imagen5 = 'assets/references/yellow_horizontal_candy.png'
                        imagen6 = 'assets/references/orange_horizontal_candy.png'

                        similitud_color1 = self.color_similarity(referencia, imagen1)
                        similitud_color2 = self.color_similarity(referencia, imagen2)
                        similitud_color3 = self.color_similarity(referencia, imagen3)
                        similitud_color4 = self.color_similarity(referencia, imagen4)
                        similitud_color5 = self.color_similarity(referencia, imagen5)
                        similitud_color6 = self.color_similarity(referencia, imagen6)

                        if similitud_color1 < umbral:
                            color_matrix[row][col] = [('b', 3), (center_x + 568, center_y + 203)]
                        elif similitud_color2 < umbral:
                            color_matrix[row][col] = [('r', 3), (center_x + 568, center_y + 203)]
                        elif similitud_color3 < umbral:
                            color_matrix[row][col] = [('g', 3), (center_x + 568, center_y + 203)]
                        elif similitud_color4 < umbral:
                            color_matrix[row][col] = [('p', 3), (center_x + 568, center_y + 203)]
                        elif similitud_color5 < umbral:
                            color_matrix[row][col] = [('y', 3), (center_x + 568, center_y + 203)]
                        elif similitud_color6 < umbral:
                            color_matrix[row][col] = [('o', 3), (center_x + 568, center_y + 203)]
                        else:
                            imagen1 = 'assets/references/blue_bolsa_candy.png'
                            imagen2 = 'assets/references/red_bolsa_candy.png'
                            imagen3 = 'assets/references/green_bolsa_candy.png'
                            imagen4 = 'assets/references/purpule_bolsa_candy.png'
                            imagen5 = 'assets/references/yellow_bolsa_candy.png'
                            imagen6 = 'assets/references/orange_bolsa_candy.png'

                            similitud_color1 = self.color_similarity(referencia, imagen1)
                            similitud_color2 = self.color_similarity(referencia, imagen2)
                            similitud_color3 = self.color_similarity(referencia, imagen3)
                            similitud_color4 = self.color_similarity(referencia, imagen4)
                            similitud_color5 = self.color_similarity(referencia, imagen5)
                            similitud_color6 = self.color_similarity(referencia, imagen6)

                            if similitud_color1 < umbral:
                                color_matrix[row][col] = [('b', 6), (center_x + 568, center_y + 203)]
                            elif similitud_color2 < umbral:
                                color_matrix[row][col] = [('r', 6), (center_x + 568, center_y + 203)]
                            elif similitud_color3 < umbral:
                                color_matrix[row][col] = [('g', 6), (center_x + 568, center_y + 203)]
                            elif similitud_color4 < umbral:
                                color_matrix[row][col] = [('p', 6), (center_x + 568, center_y + 203)]
                            elif similitud_color5 < umbral:
                                color_matrix[row][col] = [('y', 6), (center_x + 568, center_y + 203)]
                            elif similitud_color6 < umbral:
                                color_matrix[row][col] = [('o', 6), (center_x + 568, center_y + 203)]
                            else:
                                imagen1 = 'assets/references/especial_candy.png'

                                similitud_color1 = self.color_similarity(referencia, imagen1)

                                if similitud_color1 < umbral or similitud_color1 < 3500:
                                    color_matrix[row][col] = [('e', 8), (center_x + 568, center_y + 203)]
                                else:
                                    color_matrix[row][col] = [('x', 0), (center_x + 568, center_y + 203)]

        return color_matrix

    def color_similarity(self, image1, image2):
        # Leer las imágenes
        img1 = cv2.imread(image1)
        img2 = cv2.imread(image2)

        # Convertir las imágenes al espacio de color LAB
        lab1 = cv2.cvtColor(img1, cv2.COLOR_BGR2LAB)
        lab2 = cv2.cvtColor(img2, cv2.COLOR_BGR2LAB)

        # Calcular la diferencia de color utilizando la distancia CIELAB Delta E
        delta_e = cv2.norm(lab1, lab2, cv2.NORM_L2)

        return delta_e
