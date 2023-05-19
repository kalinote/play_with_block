def print_cube_v5():
    import numpy as np
    import math

    # 定义立方体的顶点
    vertices = np.array([
        [1, 1, 1],
        [1, 1, -1],
        [1, -1, 1],
        [1, -1, -1],
        [-1, 1, 1],
        [-1, 1, -1],
        [-1, -1, 1],
        [-1, -1, -1]
    ])

    # 定义旋转函数
    def rotate_y(vertex, theta):
        rotation_matrix = np.array([
            [math.cos(theta), 0, -math.sin(theta)],
            [0, 1, 0],
            [math.sin(theta), 0, math.cos(theta)]
        ])
        return np.dot(rotation_matrix, vertex)

    # 旋转立方体
    vertices = np.array([rotate_y(v, -math.pi / 8) for v in vertices])  # 向右旋转45度

    # 定义斜二测画法的投影函数
    def isometric_project(vertex, scale=10):
        x, y, z = vertex
        # 透视投影，y坐标乘以0.5
        projected_x = (x - y) * scale
        projected_y = ((x + y) / 2 - z) * scale * 0.5  # 注意这里
        return projected_x, projected_y

    # 定义立方体的边
    edges = [
        (0, 1), (0, 2), (0, 4),
        (3, 1), (3, 2), (3, 7),
        (5, 1), (5, 4), (5, 7),
        (6, 2), (6, 4), (6, 7)
    ]

    # 定义 Bresenham 算法
    def draw_line(canvas, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        sx = -1 if x1 > x2 else 1
        sy = -1 if y1 > y2 else 1

        if dx > dy:
            err = dx / 2.0
            while x != x2:
                canvas[y][x] = '*'
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y2:
                canvas[y][x] = '*'
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy

        return canvas

    # 计算投影后的顶点（缩小scale）
    projected_vertices = np.array([isometric_project(v) for v in vertices])

    # 创建一个画布
    width, height = 64, 26
    canvas = [[' ' for _ in range(width)] for _ in range(height)]

    # 将投影后的顶点映射到画布上，并绘制边
    for edge in edges:
        vertex1 = projected_vertices[edge[0]]
        vertex2 = projected_vertices[edge[1]]
        x1, y1 = int(vertex1[0] + width / 2), int(vertex1[1] + height / 2)
        x2, y2 = int(vertex2[0] + width / 2), int(vertex2[1] + height / 2)

        # 检查顶点是否在画布的范围内
        if 0 <= x1 < width and 0 <= y1 < height and 0 <= x2 < width and 0 <= y2 < height:
            canvas = draw_line(canvas, (x1, y1), (x2, y2))

    # 将投影后的顶点映射到画布上，并绘制顶点
    for vertex in projected_vertices:
        x, y = vertex
        x = int(x + width / 2)
        y = int(y + height / 2)

        if 0 <= x < width and 0 <= y < height:
            canvas[y][x] = '+'

    # 打印画布
    for row in canvas:
        print(''.join(row))


if __name__ == '__main__':
    print_cube_v5()
