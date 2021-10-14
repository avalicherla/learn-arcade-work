import arcade
arcade.open_window(650, 650, "Drawing Example")
arcade.set_background_color(arcade.csscolor.WHITE)
arcade.start_render()

#code for the sunset background
arcade.draw_lrtb_rectangle_filled(0, 650, 650, 150, (235, 70, 21, 150))

#code for sunset colored sun
arcade.draw_circle_filled(500, 550, 40, (184, 67, 20, 130))
arcade.draw_line(500, 550, 420, 550, (184, 67, 20, 130), 3)
arcade.draw_line(500, 550, 580, 550, (184, 67, 20, 130), 3)
arcade.draw_line(500, 550, 500, 470, (184, 67, 20, 130), 3)
arcade.draw_line(500, 550, 500, 630, (184, 67, 20, 130), 3)
arcade.draw_line(500, 550, 550, 600, (184, 67, 20, 130), 3)
arcade.draw_line(500, 550, 550, 500, (184, 67, 20, 130), 3)
arcade.draw_line(500, 550, 450, 600, (184, 67, 20, 130), 3)
arcade.draw_line(500, 550, 450, 500, (184, 67, 20, 130), 3)

#code for drawing sand
arcade.draw_lrtb_rectangle_filled(0, 650, 150, 0, (222, 192, 124, 150))

#code for drawing cactus
arcade.draw_rectangle_filled(100, 150, 30, 70, arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(540, 130, 30, 70, arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(320, 100, 30, 70, arcade.color.DARK_GREEN)

arcade.finish_render()
arcade.run()