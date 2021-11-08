from digit_display import DigitDisplay

class MultiDigitDisplay():

    def __init__(self, number_of_digits, x_position, y_position):
        self.display_value = 0
        self.number_of_digits = number_of_digits
        self.number_display_list = []

        for i in range(0, self.number_of_digits):
            number_display = DigitDisplay("0")
            number_display.update_sprite()
            number_display.scale = 2
            number_display.position = x_position + (number_display.width // 2) + (number_display.width * i), y_position
            self.number_display_list.append(number_display)

        self.width = self.number_of_digits * self.number_display_list[0].width

    def update_display_value(self, display_value):
        display_string = str(display_value).zfill(self.number_of_digits)
        display_counter = 0
        for display in self.number_display_list:
            display.display_value = str(display_string[display_counter])
            display.update_sprite()
            display_counter += 1

    def get_sprite_list(self):
        return self.number_display_list