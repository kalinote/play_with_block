def print_cube_v2():
    import numpy as np

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

    # 定义透视投影函数
    def project(vertex, z_offset=3, scale=10):
        x, y, z = vertex
        # 将 z 值偏移，使其为正
        z += z_offset
        # 透视投影
        projected_x = x / z * scale
        projected_y = y / z * scale
        return projected_x, projected_y

    # 计算投影后的顶点
    projected_vertices = np.array([project(v) for v in vertices])

    # 创建一个字符数组作为我们的画布
    width, height = 40, 20  # 你可以根据需要调整这两个值
    canvas = [[' ' for _ in range(width)] for _ in range(height)]

    # 将投影后的顶点映射到画布上
    for vertex in projected_vertices:
        # 将投影坐标映射到画布的索引
        x, y = vertex
        x = int(x + width / 2)  # 偏移，使立方体的中心在画布的中心
        y = int(y + height / 2)  # 偏移，使立方体的中心在画布的中心

        # 检查索引是否在画布的范围内
        if 0 <= x < width and 0 <= y < height:
            canvas[y][x] = '+'

    # 打印画布
    for row in canvas:
        print(''.join(row))


if __name__ == '__main__':
    print_cube_v2()
