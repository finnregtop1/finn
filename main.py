def on_button_pressed_b():
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
