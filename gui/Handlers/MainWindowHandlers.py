__author__ = 'Yuri Shporhun'

class MainWindowHandler:

    @staticmethod
    def connect_to_pobeda_auto_ru():
        print("sdfdf")
        pass

    @staticmethod
    def get_handler():
        handler = {
            'pobeda_auto_clicked': MainWindowHandler.connect_to_pobeda_auto_ru
        }
        return handler
