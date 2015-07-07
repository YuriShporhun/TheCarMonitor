import numpy as np
from Definitions import *

class DataConvertor(object):
    """This class is responsible for converting data
    also allows to save and print data.
    """
    data = None

    def __init__(self, data):
        self.data = data
        self.data['condition'] = [x.replace(x, conditions[x]) for x in self.data['condition']]
        self.data['bodytype'] = [x.replace(x, body_types[x]) for x in self.data['bodytype']]
        self.data['fueltype'] = [x.replace(x, fuel_type[x]) for x in self.data['fueltype']]

    def convert_features_into_matrix(self):
        matrix_string = ''
        for i in range(0, len(self.data['price'])):
            matrix_string += str(self.data['mileage'][i]) + ' ;'
        matrix_string = matrix_string[0:len(matrix_string) - 1]
        matrix = np.matrix(matrix_string)
        return matrix

    def convert_answers_into_matrix(self):
        matrix_string = ''
        for i in range(0, len(self.data['price'])):
            matrix_string += str(self.data['price'][i]) + ' ;'
        matrix_string = matrix_string[0:len(matrix_string) - 1]
        matrix = np.matrix(matrix_string)
        return matrix

    def print_data(self, line_numbering = False):
        for item in range(0, len(self.data['price'])):
            if line_numbering:
                print(str(item + 1), end = ' ')
            print(self.data['year'][item], end = ' ')
            print(self.data['price'][item], end = ' ')
            print(self.data['mileage'][item], end = ' ')
            print(self.data['condition'][item], end = ' ')
            print(self.data['bodytype'][item], end = ' ')
            print(self.data['fueltype'][item], end = ' ')
            print(self.data['litre'][item], end = ' ')
            print(self.data['gearboxtype'][item], end = ' ')
            print(self.data['gearing'][item])

    def save_data(self, filename, line_number = False):
        with open(filename + 'X.txt', 'w') as file:
            for item in range(0, len(self.data['year'])):
                if line_number:
                    file.write(str(item + 1) + ' ')
                file.write(str(self.data['year'][item]) + ' ')
                file.write('{0:.4f} '.format(float(self.data['mileage'][item])))
                file.write(str(self.data['condition'][item]) + ' ')
                file.write(str(self.data['bodytype'][item]) + ' ')
                file.write(str(self.data['fueltype'][item]) + ' ')
                file.write('{0:.4f} '.format(float(self.data['litre'][item])))
                '''
                file.write(data['gearboxtype'][item] + ' ')
                file.write(data['gearing'][item] + ' ')'''
                file.write('\n')
        with open(filename + 'Y.txt', 'w') as file:
            for item in self.data['price']:
                file.write(item) 
                file.write('\n')