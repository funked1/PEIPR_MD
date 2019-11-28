def mux_ctrl(i, pin_1, pin_2, pin_3):
    if i == 0:
        pin_1.value = False
        pin_2.value = False
        pin_3.value = False
    elif i == 1:
        pin_1.value = True
        pin_2.value = False
        pin_3.value = False
    elif i == 2:
        pin_1.value = False
        pin_2.value = True
        pin_3.value = False
    elif i == 3:
        pin_1.value = True
        pin_2.value = True
        pin_3.value = False
    elif i == 4:
        pin_1.value = False
        pin_2.value = False
        pin_3.value = True
    elif i == 5:
        pin_1.value = True
        pin_2.value = False
        pin_3.value = True
    elif i == 6:
        pin_1.value = False
        pin_2.value = True
        pin_3.value = True
    elif i == 7:
        pin_1.value = True
        pin_2.value = True
        pin_3.value = True
