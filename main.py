import sys
import colorama
import random
import numpy as np
import math

colorama.init(autoreset=True)

class Graphic():
    """
    Материнский класс галаграфа
    """
    def __init__(self, char, width, height, func, levels):
        """
        Инициирование класса

        Atr:
            char (str) - символ который будет исполльзоваться  в галаграфе
            width (int) - ширина галаграфа
            height (int) - высота галаграфа
            func (lambda function) - лямбда функция, по которой будет рисоваться галаграф
            levels (int) - количество цветов в галаграфе
        """
        self.char = char
        self.width = width
        self.height = height
        self.func = func
        self.levels = levels
        
class Picture(Graphic):
    """
    Дочерний класс создания матриц и рисования пиксельных пикчей
    """
    
    def randomize(self):
        """
        Функция для создания рандомных матриц

        Return:
            self.picture_matrix - сгенерированная рандомная матрица
        """
        self.picture_matrix = np.random.randint(1, self.levels + 1, size=(self.width, self.height))
        return self.picture_matrix
    
    def change_matrix(self):
        """
        Функция для генерирования матриц по лямбда-функции

        Return:
            self.picture_matrix - сгенерированная матрица функции
        """
        y, x = np.mgrid[0:self.height, 0:self.width]
        v = np.asarray(self.func(x, y))
        self.picture_matrix = (v % self.levels) + 1
        return self.picture_matrix
    
    def draw(self):
        """
        Функция рисования галаграфов по матрице

        Return:
            Рисует в консоли галаграф по матрице
        """
        self.drawed_picture_matrix = []
        for row in range(len(self.picture_matrix)):
            for element in range(len(self.picture_matrix[row])):
                match self.picture_matrix[row][element]:
                    case 1:
                        self.drawed_picture_matrix.append(colorama.Back.GREEN + colorama.Fore.GREEN + self.char + colorama.Style.RESET_ALL)
                    case 2:
                        self.drawed_picture_matrix.append(colorama.Back.RED + colorama.Fore.RED + self.char + colorama.Style.RESET_ALL)
                    case 3:
                        self.drawed_picture_matrix.append(colorama.Back.BLUE + colorama.Fore.BLUE + self.char + colorama.Style.RESET_ALL)
                    case 4:
                        self.drawed_picture_matrix.append(colorama.Back.YELLOW + colorama.Fore.YELLOW + self.char + colorama.Style.RESET_ALL)
                    case 5:
                        self.drawed_picture_matrix.append(colorama.Back.WHITE + colorama.Fore.WHITE + self.char + colorama.Style.RESET_ALL)
                        
        self.drawed_picture_matrix = [self.drawed_picture_matrix[i*self.width:(i+1)*self.width] for i in range(self.height)]
        for row in self.drawed_picture_matrix:
            print(' '.join(row))
        
# [list(self.drawed_picture_matrix[i*self.width:(i+1)*self.width]) for i in range(self.height)]

scalar_function = lambda x, y: (int(((math.sin(0.22*x) + math.sin(0.17*y) + math.sin(0.13*(x + y))) + 3.0) / 6.0 * 5.0) % 5) + 1

function = np.vectorize(scalar_function, otypes=[int])

picture = Picture('*', 35, 35, function, 5)
print(picture.levels)
print(picture.randomize())
print(picture.draw())