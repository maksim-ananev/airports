import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import controller


class Welcome(QDialog):
    '''
    Класс, выводящий на экран окно с выбором интересующей функции - поиск по координатам, поиск маршрутов между городами или поиск маршрутов в/из города

    '''
    def __init__(self):
        super().__init__()
        loadUi('UI/welcome.ui', self)
        self.search_airports_btn.clicked.connect(self.go_to_coordinates_filter)
        self.search_routes_by_cities_btn.clicked.connect(self.go_to_routes_by_cities)
        self.search_routes_ct_btn.clicked.connect(self.go_to_routes_in_from_city)

    def go_to_coordinates_filter(self):
        search_airports = Coordinates_filter()

        widget.addWidget(search_airports)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def go_to_routes_by_cities(self):
        search_routes_by_cities = Routes_by_cities_filter()
        widget.addWidget(search_routes_by_cities)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_to_routes_in_from_city(self):
        search_routes_to_from_city = Routes_in_from_city()
        widget.addWidget(search_routes_to_from_city)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class Coordinates_filter(QDialog):
    '''
    Класс, выводящий на экран окно с вводом координат для поиска аэропортов
    '''
    def __init__(self):
        super().__init__()
        loadUi('UI/coordinates_filter.ui', self)
        self.submin_coordinates_btn.clicked.connect(self.go_to_filtred_airports)

    def go_to_filtred_airports(self):
        if self.min_latitude.text() != '':
            min_latitude = self.min_latitude.text()
        else:
            min_latitude = '-90'
        if self.max_latitude.text() != '':
            max_latitude = self.max_latitude.text()
        else:
            max_latitude = '90'
        if self.min_longitude.text() != '':
            min_longitude = self.min_longitude.text()
        else:
            min_longitude = '-180'
        if self.max_longitude.text() != '':
            max_longitude = self.max_longitude.text()
        else:
            max_longitude = '180'

        filtred_airports = Filtred_airports(min_latitude, max_latitude, min_longitude, max_longitude)
        widget.addWidget(filtred_airports)
        widget.setCurrentIndex(widget.currentIndex() + 1)





class Filtred_airports(QDialog):
    '''
    Класс, выводящий на экран таблицу со списком отфильрованных по координатам аэропортов
    '''
    def __init__(self, min_lat, max_lat, min_lon, max_lon):
        super().__init__()
        loadUi('UI/filtred_airports.ui', self)
        self.min_lat = min_lat
        self.max_lat = max_lat
        self.min_lon = min_lon
        self.max_lon = max_lon
        self.data = controller.Controller_airports()
        self.get_filtred_airports()


    def get_filtred_airports(self):
        filtred_airports = self.data.filtred_airports(self.min_lat, self.max_lat, self.min_lon, self.max_lon)
        self.filtred_airports_tb.setRowCount(len(filtred_airports))
        self.filtred_airports_tb.setSortingEnabled(True)
        for i in range(len(filtred_airports)):
            for j in range(len(filtred_airports[i])):
                self.filtred_airports_tb.setItem(i, j, QTableWidgetItem(str(filtred_airports[i][j])))
        self.filtred_airports_tb.resizeColumnsToContents()


class Routes_by_cities_filter(QDialog):
    '''
    Класс, выводящий на экран поля ввода городов отправления и прибытия
    '''
    def __init__(self):
        super().__init__()
        loadUi('UI/routes_cities.ui', self)
        self.submin_cities_btn.clicked.connect(self.go_to_routes_by_cities_filter)

    def go_to_routes_by_cities_filter(self):
        city_from = self.departure.text()
        city_to = self.arrival.text()
        routes_by_cities = Filtred_roures_by_city(city_from, city_to)
        widget.addWidget(routes_by_cities)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Filtred_roures_by_city(QDialog):
    def __init__(self, city_from, city_to):
        super().__init__()
        loadUi('UI/filtred_routes_by_cities.ui', self)
        self.city_from = city_from
        self.city_to = city_to
        self.data = controller.Controller_airports()
        self.get_routes_by_cities()


    def get_routes_by_cities(self):
        routes_by_cities = self.data.filtred_routes_by_cities(self.city_from, self.city_to)
        self.routes_by_cities_tb.setRowCount(len(routes_by_cities))
        self.routes_by_cities_tb.setSortingEnabled(True)
        for i in range(len(routes_by_cities)):
            for j in range(len(routes_by_cities[i])):
                self.routes_by_cities_tb.setItem(i, j, QTableWidgetItem(str(routes_by_cities[i][j])))
        self.routes_by_cities_tb.resizeColumnsToContents()

class Routes_in_from_city(QDialog):
    '''
    Класс, выводящий на экран поле ввода города
    '''
    def __init__(self):
        super().__init__()
        loadUi('UI/routes_in_from_city.ui', self)
        self.submin_city_btn.clicked.connect(self.go_to_routes_in_from_city_filter)

    def go_to_routes_in_from_city_filter(self):
        city = self.city.text()
        routes_in_from_city = Filtred_routes_in_from_city(city)
        widget.addWidget( routes_in_from_city)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Filtred_routes_in_from_city(QDialog):
    def __init__(self, city):
        super().__init__()
        loadUi('UI/filtred_routes_by_cities.ui', self)
        self.city = city
        self.data = controller.Controller_airports()
        self.get_routes_in_from_city()
    #
    #
    #
    def get_routes_in_from_city(self):
        routes_in_from_city = self.data.filtred_routes_in_to_city(self.city)
        self.routes_by_cities_tb.setRowCount(len(routes_in_from_city))
        self.routes_by_cities_tb.setSortingEnabled(True)
        for i in range(len(routes_in_from_city)):
            for j in range(len(routes_in_from_city[i])):
                self.routes_by_cities_tb.setItem(i, j, QTableWidgetItem(str(routes_in_from_city[i][j])))
        self.routes_by_cities_tb.resizeColumnsToContents()
















if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Welcome()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(776)
    widget.setFixedHeight(289)
    widget.show()
    app.exec_()