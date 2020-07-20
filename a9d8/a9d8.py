def get_stop_time(time, red_per, green_per):
    remainder = time % (red_per + green_per)
    if remainder < red_per:
        return red_per - remainder

    return 0


def Unmanned(L, N, track):
    s_counter = 0
    t_counter = 0

    for light in track:
        if light[0] >= L:
            return t_counter + (L - s_counter)
        diff = light[0] - s_counter
        s_counter = light[0]
        t_counter += diff
        t_counter += (get_stop_time(t_counter, light[1], light[2]))

    return t_counter + (L - s_counter)
