import arcade

arcade.open_window(600, 600, "Drawing Example")

#background color of the room
arcade.set_background_color(arcade.csscolor.LIGHT_GRAY)

arcade.start_render()

#outline rectangle for the monitor
arcade.draw_lrtb_rectangle_filled(210, 410, 400, 250, arcade.csscolor.BLACK)

#white screen inside monitor
arcade.draw_lrtb_rectangle_filled(220, 400, 390, 260, arcade.csscolor.WHITE)

#math problem showed on monitor
arcade.draw_text("3X + 6 = 0. What is X?", 240,325, arcade.csscolor.BLACK, 10)

#monitor stand
arcade.draw_line(310, 250, 310, 210, arcade.csscolor.BLACK, 20)
arcade.draw_line(310, 210, 245, 195, arcade.csscolor.BLACK, 10)
arcade.draw_line(310, 210, 375, 195, arcade.csscolor.BLACK, 10)

#Wood table and legs
arcade.draw_lrtb_rectangle_filled(20, 580, 200, 100, arcade.csscolor.BURLYWOOD)
arcade.draw_lrtb_rectangle_filled(30, 40, 100, 0, arcade.csscolor.BURLYWOOD)
arcade.draw_lrtb_rectangle_filled(560, 570, 100, 0, arcade.csscolor.BURLYWOOD)
arcade.draw_lrtb_rectangle_filled(50, 60, 100, 50, arcade.csscolor.BURLYWOOD)
arcade.draw_lrtb_rectangle_filled(540, 550, 100, 50, arcade.csscolor.BURLYWOOD)

#Window with night sky
arcade.draw_lrtb_rectangle_filled(150, 450, 550, 450, arcade.csscolor.WHITE)
arcade.draw_lrtb_rectangle_filled(160, 440, 545, 455, arcade.csscolor.BLACK)
arcade.draw_circle_filled(400, 500, 20, arcade.csscolor.WHITE)

#Paper on desk
arcade.draw_lrtb_rectangle_filled(270, 360, 190, 105, arcade.csscolor.WHITE)

#Answer to math problem on paper
arcade.draw_text("X = -2", 295, 145, arcade.csscolor.BLACK, 10)

#pencil body
arcade.draw_line(400, 170, 380, 130, arcade.csscolor.YELLOW, 8)

#pencil eraser
arcade.draw_line(395, 170, 403, 166, arcade.csscolor.DEEP_PINK, 8)

#tip of pencil
arcade.draw_triangle_filled(376, 125, 376, 131, 384, 129, arcade.csscolor.BLACK)

arcade.finish_render()
arcade.run()