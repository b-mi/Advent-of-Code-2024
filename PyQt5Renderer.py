# import sys
# import numpy as np
# from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QLabel
# from PyQt5.QtGui import QImage, QPixmap, QColor, QFont, QPainter
# from PyQt5.QtCore import Qt, QPoint


# class MatrixRenderer:
#     def __init__(self, matrix, colors, cell_size=20, fps=30, font_size=20, window_size=(800, 600)):
#         """
#         Inicializuje renderer pre NumPy maticu so znakmi.

#         Args:
#             matrix (numpy.ndarray): 2D NumPy pole obsahujúce písmená.
#             cell_size (int): Veľkosť jednej bunky v pixeloch.
#             colors (dict): Slovník mapujúci písmená na (pozadie, text).
#             fps (int): Počet snímok za sekundu (tu nepoužité).
#             font_size (int): Veľkosť písma pre znaky.
#             window_size (tuple): Počiatočné rozmery okna (šírka, výška).
#         """
#         self.matrix = matrix
#         self.colors = colors
#         self.cell_size = cell_size
#         self.fps = fps
#         self.font_size = font_size
#         self.height, self.width = matrix.shape

#         # Inicializácia PyQt aplikácie
#         self.app = QApplication(sys.argv)
#         self.window = QMainWindow()
#         self.window.setWindowTitle("NumPy Matrix Renderer")
#         self.window.resize(*window_size)

#         # Scrollovacia plocha
#         self.scroll_area = QScrollArea()
#         self.label = PanLabel(cell_size=self.cell_size, callback=self._show_coordinates)  # Správne inicializované s argumentmi
#         self.scroll_area.setWidget(self.label)
#         self.scroll_area.setWidgetResizable(True)
#         self.window.setCentralWidget(self.scroll_area)

#         # Vytvorenie statického obrazu
#         self.image = self._generate_image()
#         self.label.setPixmap(QPixmap.fromImage(self.image))


#     def _show_coordinates(self, x, y):
#         """Zobrazí súradnice bunky."""
#         if 0 <= x < self.width and 0 <= y < self.height:  # Kontrola hraníc
#             self.set_caption(f"(y,x)({y}, {x})")

#     def _generate_image(self):
#         """Vytvorí QImage na základe matice s 1-pixelovými medzerami."""
#         # Pridáme 1 pixel na každú medzeru medzi bunkami
#         img_width = self.width * (self.cell_size + 1) - 1
#         img_height = self.height * (self.cell_size + 1) - 1
#         image = QImage(img_width, img_height, QImage.Format_RGB32)
#         painter = QPainter(image)

#         # Vyplní pozadie čiernou farbou (alebo inou podľa potreby)
#         painter.fillRect(image.rect(), QColor('#000000'))

#         font = QFont("Consolas", self.font_size)
#         painter.setFont(font)

#         for y in range(self.height):
#             for x in range(self.width):
#                 char = self.matrix[y, x]
#                 bg_color, text_color = self.colors.get(char, ('#000000', '#FFFFFF'))

#                 # Vykreslí pozadie bunky
#                 rect_x = x * (self.cell_size + 1)
#                 rect_y = y * (self.cell_size + 1)
#                 rect = (rect_x, rect_y, self.cell_size, self.cell_size)
#                 painter.fillRect(*rect, QColor(bg_color))

#                 # Vykreslí text (symbol)
#                 painter.setPen(QColor(text_color))
#                 painter.drawText(*rect, Qt.AlignCenter, char)

#         painter.end()
#         return image

#     def render(self):
#         """Spustí PyQt aplikáciu a zobrazí okno."""
#         self.window.show()
#         self.app.exec_()

#     def update_matrix(self, new_matrix):
#         """Aktualizuje maticu a prekreslí obraz."""
#         self.matrix = new_matrix
#         self.image = self._generate_image()
#         self.label.setPixmap(QPixmap.fromImage(self.image))

#     def set_caption(self, title):
#         """Zmení titulok okna."""
#         self.window.setWindowTitle(title)

#     def close(self):
#         """Zatvorí PyQt aplikáciu."""
#         self.window.close()


# class PanLabel(QLabel):
#     """QLabel s podporou posúvania (pan) myšou a zobrazením súradníc."""
#     def __init__(self, cell_size, callback=None):
#         super().__init__()
#         self.setMouseTracking(True)
#         self._last_mouse_pos = QPoint()
#         self.cell_size = cell_size  # Veľkosť bunky
#         self.callback = callback  # Funkcia na odoslanie súradníc
#         self.setAlignment(Qt.AlignLeft | Qt.AlignTop)

#     def mousePressEvent(self, event):
#         """Ukladá počiatočnú pozíciu myši pri stlačení tlačidla."""
#         if event.button() == Qt.LeftButton:
#             self._last_mouse_pos = event.globalPos()

#     def mouseMoveEvent(self, event):
#         """Aktualizuje posun podľa pohybu myši a odosiela súradnice."""
#         if event.buttons() == Qt.LeftButton:
#             # Vypočíta rozdiel medzi aktuálnou a poslednou pozíciou
#             delta = event.globalPos() - self._last_mouse_pos
#             self._last_mouse_pos = event.globalPos()

#             # Posunie obsah scrollovacej oblasti
#             scroll_area = self.parent().parent()
#             scroll_area.horizontalScrollBar().setValue(scroll_area.horizontalScrollBar().value() - delta.x())
#             scroll_area.verticalScrollBar().setValue(scroll_area.verticalScrollBar().value() - delta.y())

#         # Zobrazenie súradníc bunky
#         pos = event.pos()
#         cell_x = pos.x() // (self.cell_size + 1)  # Prepočet X
#         cell_y = pos.y() // (self.cell_size + 1)  # Prepočet Y

#         if self.callback:
#             self.callback(cell_x, cell_y)

# # Príklad použitia
# # if __name__ == "__main__":
# #     # Vytvorenie matice a farieb
# #     matrix = np.random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), (141, 141))
# #     colors = {char: ('#202020', '#FFFFFF') for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

# #     # Spustenie rendereru
# #     renderer = MatrixRenderer(matrix, colors, cell_size=10, window_size=(800, 600))
# #     renderer.render()
