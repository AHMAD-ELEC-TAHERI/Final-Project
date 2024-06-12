# این تابع عملیات کانولوشن را بر روی دو لیست انجام می‌دهد.
def convolution(signal, filter):
    # یک لیست خالی برای ذخیره نتیجه ایجاد می‌کنیم.
    convolved = []
    
    # حلقه برای محدوده طول ترکیب سیگنال و فیلتر.
    for i in range(len(signal) + len(filter) - 1):
        # یک صفر به لیست نتیجه اضافه می‌کنیم.
        convolved.append(0)
        
        # حلقه برای محدوده طول سیگنال.
        for j in range(len(signal)):
            # بررسی می‌کنیم که آیا شاخص فعلی در محدوده فیلتر است یا خیر.
            if i - j < len(filter) and i - j >= 0:
                # محصول سیگنال فعلی و مقدار فیلتر را به نتیجه اضافه می‌کنیم.
                convolved[i] += signal[j] * filter[i - j]
    
    # لیست نتیجه را برمی‌گردانیم.
    return convolved

# این تابع یک فیلتر پایین‌گذر ایجاد می‌کند.
def create_filter(cutoff, fs, order):
    # یک لیست خالی برای ذخیره فیلتر ایجاد می‌کنیم.
    filter = []
    
    # حلقه برای محدوده سفارش.
    for i in range(order):
        # فرکانس برش را تقسیم بر نیم فرکانس نمونه‌برداری به فیلتر اضافه می‌کنیم.
        filter.append(cutoff / (0.5 * fs))
    
    # لیست فیلتر را برمی‌گردانیم.
    return filter

# فرکانس نمونه‌برداری را تعیین می‌کنیم.
fs = 30.0

# فرکانس برش را تعیین می‌کنیم.
cutoff = 3.667

# با استفاده از تابع create_filter یک فیلتر ایجاد می‌کنیم.
filter = create_filter(cutoff, fs, 5)

# سیگنال را تعریف می‌کنیم.
signal = [0.1, 0.2, 0.3, 0.4]

# با استفاده از تابع کانولوشن ،فیلتر را بر روی سیگنال اعمال میکنیم
filtered_signal = convolution(signal, filter)

# هر مقدار در سیگنال فیلتر شده را چاپ می‌کنیم.
with open('D:\Video Editor.txt', 'w') as file:
    for value in filtered_signal:
        print(value)
        file.write(str(value) + '\n')
