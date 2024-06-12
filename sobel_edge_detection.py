# تعریف تصویر به عنوان یک لیست 2D (این را با تصویر واقعی خود جایگزین کنید)
image = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]

# تعریف هسته های Sobel
sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

# ایجاد لیست های خالی برای لبه ها
edges_x = [[0]*5 for _ in range(5)]
edges_y = [[0]*5 for _ in range(5)]

# اعمال هسته های Sobel به تصویر
for i in range(1, len(image)-1):
    for j in range(1, len(image[0])-1):
        for ki in range(len(sobel_x)):
            for kj in range(len(sobel_x[0])):
                edges_x[i][j] += image[i+ki-1][j+kj-1] * sobel_x[ki][kj]
                edges_y[i][j] += image[i+ki-1][j+kj-1] * sobel_y[ki][kj]

# ترکیب لبه ها در جهت های x و y
edges = [[0]*5 for _ in range(5)]
for i in range(len(edges_x)):
    for j in range(len(edges_x[0])):
        edges[i][j] = (edges_x[i][j]**2 + edges_y[i][j]**2)**0.5

# چاپ لبه ها
for row in edges:
    print(row)
