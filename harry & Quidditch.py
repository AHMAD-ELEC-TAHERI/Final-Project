# این تابع میدان الکتریکی را در نقطه O محاسبه می‌کند.
from cmath import cos, sin
from math import atan2


def calculate_field(game_field):
    # متغیرهایی برای ذخیره مقادیر میدان الکتریکی در جهت‌های x و y
    Ex, Ey = 0, 0
    
    # حلقه برای پیمایش تمام خانه‌های زمین بازی
    for i in range(len(game_field)):
        for j in range(len(game_field[0])):
            # اگر خانه فعلی بار دارد یا نقطه O نیست
            if game_field[i][j] != 'O' and game_field[i][j] != 0:
                # محاسبه فاصله تا نقطه O
                r = ((5-i)**2 + (5-j)**2)**0.5
                # محاسبه میدان الکتریکی ناشی از بار خانه فعلی
                E = game_field[i][j] / r**2
                # محاسبه زاویه بین خط مستقیم از خانه فعلی به نقطه O و محور x
                theta = atan2(5-i, 5-j)
                # اضافه کردن مقدار میدان الکتریکی در جهت x و y
                Ex += E * cos(theta)
                Ey += E * sin(theta)
    # برگرداندن مقادیر میدان الکتریکی در جهت‌های x و y
    return [Ex, Ey]

# این تابع میدان الکتریکی در فاصله یک متری از وسط یک خط صاف 50 متری را محاسبه می‌کند.
def calculate_field_line(charge_density):
    # متغیر برای ذخیره مقدار میدان الکتریکی
    E = 0
    # حلقه برای پیمایش تمام نقاط خط
    for x in range(-250, 251):
        x = x / 10.0  # تقسیم بر 10 برای دستیابی به 500 نقطه در بازه -25 تا 25
        # محاسبه فاصله تا نقطه فعلی
        r = (1**2 + x**2)**0.5
        # محاسبه میدان الکتریکی ناشی از بار در نقطه فعلی
        dE = charge_density / r**2
        # محاسبه زاویه بین خط مستقیم از نقطه فعلی به نقطه مورد نظر و محور x
        if x < 0:
            theta = 3.14159 - 3.14159 * (r - 1) / (2 * r)
        else:
            theta = 3.14159 * (r - 1) / (2 * r)
        # اضافه کردن مقدار میدان الکتریکی
        E += dE * cos(theta)
    # برگرداندن مقدار میدان الکتریکی
    return E

# تعریف فرکانس نمونه‌برداری و فرکانس برش
fs = 30.0
cutoff = 3.667

# تعریف زمین بازی
game_field = [
    [2, 0, 0],
    [0, 0, 'O'],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 2],
    [0, 0, 0],
    [3, 0, 1],
    [0, 0, 1],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 5],
    [0, 0, 0]
]

# تعریف چگالی یکسان بار C1
charge_density = 1e-6  # C/m

# محاسبه میدان‌های الکتریکی
field_game = calculate_field(game_field)
field_line = calculate_field_line(charge_density)

# چاپ میدان الکتریکی در نقطه O و در فاصله یک متری از وسط خط
print('میدان الکتریکی در نقطه O: ', field_game)
print('میدان الکتریکی در فاصله یک متری از وسط خط: ', field_line)