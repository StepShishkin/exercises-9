class TrafficLight:

    permissible_values = ['зеленый', 'желтый', 'красный']

    def __init__(self, current_signal='зеленый'):
        self.current_signal = current_signal

    def next_signal(self):
        """
        Method that changes the traffic light signal
        """
        current_index = TrafficLight.permissible_values.index(self.current_signal)
        if current_index < 2:
            self.current_signal = TrafficLight.permissible_values[current_index + 1]
        else:
            current_index = 0
            TrafficLight.permissible_values.reverse()
            self.current_signal = TrafficLight.permissible_values[current_index + 1]

    def __str__(self):
        return f'{self.current_signal}'

traffic_light = TrafficLight()
traffic_light.next_signal()
print(traffic_light)