def print_cube_v3():
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

    # 定义斜二测画法的投影函数
    def isometric_project(vertex, scale=5):
        x, y, z = vertex
        # 透视投影，y坐标乘以0.5
        projected_x = (x - y) * scale
        projected_y = ((x + y) / 2 - z) * scale * 0.5  # 注意这里
        return projected_x, projected_y

    # 计算投影后的顶点（缩小scale）
    projected_vertices = np.array([isometric_project(v) for v in vertices])

    # 创建一个更小的画布
    width, height = 40, 20
    canvas = [[' ' for _ in range(width)] for _ in range(height)]

    # 将投影后的顶点映射到画布上
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
    print_cube_v3()
