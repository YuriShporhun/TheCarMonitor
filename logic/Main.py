#!/usr/env python3
# -*- coding: utf-8 -*-

from numpy import mean
from numpy import std

from ml.GradientDescent import *
from logic import DataConvertor, Parser

URL_COPYPASTE_AVTOVAZ_TEST = 'http://spb.am.ru/all/search/?p465=87&p1009=1602&p1129ge=1900&p1129le=2014&p2le=9000000&p1145[]=13,29'

def feature_normalize(data):
    mileage_mean = mean([int(x) for x in data['mileage']])
    mileage_sigma = std([int(x) for x in data['mileage']])
    data['mileage'] = [(int(x) - mileage_mean) / mileage_sigma for x in data['mileage']]

    price_mean = mean([int(x) for x in data['price']])
    price_sigma = std([int(x) for x in data['price']])
    data['price'] = [(int(x) - price_mean) / price_sigma for x in data['price']]

def feature_scaling(data):
    mileage_max = max([int(x) for x in data['mileage']])
    data['mileage'] = [(int(x) - mileage_max / 2.0) / mileage_max for x in data['mileage']]
    price_max = max([int(x) for x in data['price']])
    data['price'] = [(int(x) - price_max / 2.0) / price_max for x in data['price']]

def main():
    auto_name = 'VAZ'
    page_parser = Parser('http://msk.am.ru/all/search/?p465=87&p1009=1602&p739=1%2C2')
    data = page_parser.parse_auto()
    data_convertor = DataConvertor(data)
    # features_normalize(data)
    data_convertor.print_data(True)
    data_convertor.save_data('C:\\data\\' + auto_name, False)
    feature_matrix = data_convertor.convert_features_into_matrix()
    answer_matrix = data_convertor.convert_answers_into_matrix()
    theta_matrix, history = GradientDescent(feature_matrix, answer_matrix, 0.01, 1000)
    print(theta_matrix)

if __name__ == '__main__':
    main()

