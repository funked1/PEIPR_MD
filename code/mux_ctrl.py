def mux_ctrl(i):
    if i == 0:
        GPIO.output(8, False)
        GPIO.output(10, False)
        GPIO.output(12, False)
    elif i == 1:
        GPIO.output(8, True)
        GPIO.output(10, False)
        GPIO.output(12, False)
    elif i == 2:
        GPIO.output(8, False)
        GPIO.output(10, True)
        GPIO.output(12, False)
    elif i == 3:
        GPIO.output(8, True)
        GPIO.output(10, True)
        GPIO.output(12, False)
    elif i == 4:
        GPIO.output(8, False)
        GPIO.output(10, False)
        GPIO.output(12, True)
    elif i == 5:
        GPIO.output(8, True)
        GPIO.output(10, False)
        GPIO.output(12, True)
    elif i == 6:
        GPIO.output(8, False)
        GPIO.output(10, True)
        GPIO.output(12, True)
    elif i == 7:
        GPIO.output(8, True)
        GPIO.output(10, True)
        GPIO.output(12, True)
