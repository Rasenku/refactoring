class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered or removed.
    def registerObserver(observer):
        pass

    def removeObserver(observer):
        pass
    # This method is called to notify all observers
    # when the Subject's state (measurements) ha changed.
    def notifyObservers():
        pass

# The observer class is implemented by all observers,
# so they all have to implement the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass


# WeatherData now implements the subject interface.
class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0


    def registerObserver(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notifyObservers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()


#Implementation of Weather Data

class CurrentConditionsDisplay(Observer):
    def __init__(self, weatherData):
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("Current conditions:", self.temerature,
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)


class StatisticsDisplay(Observer):
    def __init__(self, weatherData):
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0

        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def display_stats(self):
        print(self.temerature, self.humidity, self.pressure)

    def update_stats(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display_stats()


class ForecastDisplay(Observer):

    def __init__(self, weather_data):
        self.forecast_temp = 0
        self.forecast_hum = 0
        self.forecast_pressure = 0

        self.weather_data = weather_data # save the ref in an attribute.
        weather_data.registerObserver(self) # register the observer
                                           # so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.forecast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        self.forecast_hum = humidity - 0.9 * humidity
        self.forecast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        self.display()

    def display(self):
        print("\nForecast conditions:", self.forecast_temp,
              "F degrees and", self.forecast_hum,"[%] humidity",
              "and pressure", self.forecast_pressure)


class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)

        statistics_display = StatisticsDisplay(Subject)
        forecast_display = ForecastDisplay(Subject)


        weather_data.setMeasurements(80, 65,30.4)
        weather_data.setMeasurements(82, 70,29.2)
        weather_data.setMeasurements(78, 90,29.2)

        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100,1000)

        weather_data.registerObserver(statistics_display)
        weather_data.registerObserver(forecast_display)

if __name__ == "__main__":
    w = WeatherStation()
    w.main()
