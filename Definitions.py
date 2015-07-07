new_car = '\u041d\u043e\u0432\u044b\u0439'
best_condition = '\u041e\u0442\u043b\u0438\u0447\u043d\u043e\u0435'
good_condition = '\u0425\u043e\u0440\u043e\u0448\u0435\u0435'
average_condition = '\u0421\u0440\u0435\u0434\u043d\u0435\u0435'
bad_condition = '\u041f\u043b\u043e\u0445\u043e\u0435'
damaged_car = '\u0411\u0438\u0442\u044b\u0439'

sedan = '\u0421\u0435\u0434\u0430\u043d'
hatchback = '\u0425\u0435\u0442\u0447\u0431\u044d\u043a'
liftback = '\u041b\u0438\u0444\u0442\u0431\u044d\u043a'
suv = '\u0412\u043d\u0435\u0434\u043e\u0440\u043e\u0436\u043d\u0438\u043a'
roadster = '\u0420\u043e\u0434\u0441\u0442\u0435\u0440'
coupe = '\u041a\u0443\u043f\u0435'
crossover = '\u041a\u0440\u043e\u0441\u0441\u043e\u0432\u0435\u0440'
touring = '\u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0430\u043b'
van = '\u0424\u0443\u0440\u0433\u043e\u043d'
minibus = '\u041c\u0438\u043a\u0440\u043e\u0430\u0432\u0442\u043e\u0431\u0443\u0441'
pickup = '\u041f\u0438\u043a\u0430\u043f'
fastback = '\u0424\u0430\u0441\u0442\u0431\u044d\u043a'
minivan = '\u041c\u0438\u043d\u0438\u0432\u044d\u043d'
bort = '\u0411\u043e\u0440\u0442'
convertible = '\u041a\u0430\u0431\u0440\u0438\u043e\u043b\u0435\u0442'

gasoline = '\u0411\u0435\u043d\u0437\u0438\u043d'
diesel = '\u0414\u0438\u0437\u0435\u043b\u044c'
hybrid = '\u0413\u0438\u0431\u0440\u0438\u0434'

#Describes the transformation of the state of the car to the numerical mean
conditions = {
    new_car: '5',
    best_condition: '4', #Otlichnoe
    good_condition: '3', #Horoshee
    average_condition: '2', #Srednee
    bad_condition: '1', #Plohoe
    damaged_car: '0' #Bitiy
}

#Describes the body type of car
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

#Describes the fuel type of car
fuel_type = {
    gasoline: '1',
    diesel: '2',
    hybrid: '3'
    } 