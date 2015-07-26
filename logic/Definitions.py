# -*- coding: utf-8 -*-

new_car = 'Новый'
best_condition = 'Отличное'
good_condition = 'Хорошее'
average_condition = 'Среднее'
bad_condition = 'Плохое'
damaged_car = 'Битая'

sedan = 'Седан'
hatchback = 'Хэтчбек'
liftback = 'Лифтбек'
suv = 'Внедорожник'
roadster = 'Родстер'
coupe = 'Купе'
crossover = 'Кроссовер'
touring = '\u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0430\u043b'
van = '\u0424\u0443\u0440\u0433\u043e\u043d'
minibus = '\u041c\u0438\u043a\u0440\u043e\u0430\u0432\u0442\u043e\u0431\u0443\u0441'
pickup = 'Пикап'
fastback = '\u0424\u0430\u0441\u0442\u0431\u044d\u043a'
minivan = '\u041c\u0438\u043d\u0438\u0432\u044d\u043d'
bort = '\u0411\u043e\u0440\u0442'
convertible = 'Кабриолет'

gasoline = '\u0411\u0435\u043d\u0437\u0438\u043d'
diesel = '\u0414\u0438\u0437\u0435\u043b\u044c'
hybrid = '\u0413\u0438\u0431\u0440\u0438\u0434'

# Describes the transformation of the state of the car to the numerical mean
conditions = {
    new_car: '5',
    best_condition: '4', #Otlichnoe
    good_condition: '3', #Horoshee
    average_condition: '2', #Srednee
    bad_condition: '1', #Plohoe
    damaged_car: '0' #Bitiy
}

# Describes the body type of car
body_types = {
    sedan: '1',
    hatchback: '2',
    liftback: '3',
    suv: '4',
    roadster: '5',
    coupe: '6',
    crossover: '7',
    touring: '8',
    van: '9',
    minibus: '10',
    pickup: '11',
    fastback: '12',
    minivan: '13',
    bort: '14',
    convertible: '15'
    }

# Describes the fuel type of car
fuel_type = {
    gasoline: '1',
    diesel: '2',
    hybrid: '3'
    } 