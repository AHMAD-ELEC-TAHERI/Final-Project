# توان ترانسفورماتور را مشخص می‌کنیم (به وات)
power = 10000

# چگالی جریان را مشخص می‌کنیم (به آمپر بر متر مربع)
current_density = 3.8

# ولتاژ اولیه و ثانویه را مشخص می‌کنیم (به ولت)
primary_voltage = 230
secondary_voltage = 115

# مساحت مقطع هسته ترانسفورماتور را محاسبه می‌کنیم
core_cross_sectional_area = power / (1.1 * current_density)

# تعداد دورهای پیچش اولیه و ثانویه را محاسبه می‌کنیم
primary_turns = primary_voltage / (4.44 * 50 * core_cross_sectional_area)
secondary_turns = secondary_voltage / (4.44 * 50 * core_cross_sectional_area)

# نتایج را چاپ می‌کنیم
print("مساحت مقطع هسته ترانسفورماتور: ", core_cross_sectional_area)
print("تعداد دورهای پیچش اولیه: ", primary_turns)
print("تعداد دورهای پیچش ثانویه: ", secondary_turns)
