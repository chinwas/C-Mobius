import math
import time
import sys

WIDTH, HEIGHT = 90, 30
RADIUS = 12
STRIP_WIDTH = 6

FRAME_DELAY = 0.03

ROTATION_INCREMENT_Y = 0.02
ROTATION_INCREMENT_Z = 0.015

RIVER_CHARS = "~-'.` "
BANK_CHAR = '#'
BACKGROUND_CHAR = ' '

def render_mobius_strip_smooth():
    """Main function to render a smoother animated Mobius strip."""
    
    angle_y, angle_z = 0.0, 0.0
    texture_offset = 0

    try:
        while True:
            screen = [[BACKGROUND_CHAR for _ in range(WIDTH)] for _ in range(HEIGHT)]
            z_buffer = [[-float('inf') for _ in range(WIDTH)] for _ in range(HEIGHT)]

            sin_y, cos_y = math.sin(angle_y), math.cos(angle_y)
            sin_z, cos_z = math.sin(angle_z), math.cos(angle_z)

            for u_step in range(360):
                u = math.radians(u_step)
                cos_u, sin_u = math.cos(u), math.sin(u)
                cos_half_u, sin_half_u = math.cos(u/2), math.sin(u/2)

                for v_step in range(-15, 16):
                    v = v_step / 15.0 * STRIP_WIDTH

                    common_term = RADIUS + v * cos_half_u
                    x = common_term * cos_u
                    y = common_term * sin_u
                    z = v * sin_half_u

                    x_rot_z = x * cos_z - y * sin_z
                    y_rot_z = x * sin_z + y * cos_z
                    x_rot_y = x_rot_z * cos_y + z * sin_y
                    y_rot_y = y_rot_z
                    z_rot_y = -x_rot_z * sin_y + z * cos_y

                    final_x, final_y, final_z = x_rot_y, y_rot_y, z_rot_y

                    screen_x = int(WIDTH / 2 + 2 * final_x)
                    screen_y = int(HEIGHT / 2 + final_y)

                    if 0 <= screen_x < WIDTH and 0 <= screen_y < HEIGHT:
                        if final_z > z_buffer[screen_y][screen_x]:
                            z_buffer[screen_y][screen_x] = final_z

                            if abs(v_step) >= 14:
                                char = BANK_CHAR
                            else:
                                char_index = (int(u_step * 0.2) + texture_offset) % len(RIVER_CHARS)
                                char = RIVER_CHARS[char_index]
                            
                            screen[screen_y][screen_x] = char

            output = "".join("".join(row) + "\n" for row in screen)
            
            sys.stdout.write('\x1b[H' + output)
            sys.stdout.flush()

            angle_y += ROTATION_INCREMENT_Y
            angle_z += ROTATION_INCREMENT_Z
            texture_offset += 1
            
            time.sleep(FRAME_DELAY)

    except KeyboardInterrupt:
        sys.stdout.write('\x1b[?25h') 
        print("\nAnimation stopped. Goodbye!")

if __name__ == "__main__":
    sys.stdout.write('\x1b[?25l')
    render_mobius_strip_smooth()
