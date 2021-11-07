from arcade.arcade_types import Point
from number_display import NumberDisplay

class MinesLeftDisplay():

    base_offset = 13 # 13px width for display segment

    def __init__(self, x_position, y_position):
        self.display_value = 0
        self.number_display_list = []
        for i in range(0,3):
            number_display = NumberDisplay(0)
            number_display.position = x_position + (self.base_offset * i), y_position
            self.number_display_list.append(number_display)

    def update_display_value(self, display_value):
        display_string = str(display_value).zfill(3)
        display_counter = 0
        for display in self.number_display_list:
            display.display_value = int(display_string[display_counter])
            display.update_sprite()
            display_counter += 1

    def get_sprite_list(self):
        return self.number_display_list