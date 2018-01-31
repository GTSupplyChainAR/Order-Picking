import a_star as pf

class Test():

    def test_maze(self):
        a = pf.AStar()
        walls = ((0, 5), (1, 0), (1, 1), (1, 5), (2, 3),
                 (3, 1), (3, 2), (3, 5), (4, 1), (4, 4), (5, 1))
        a.init_grid(8, 10, walls, (0, 0), (6, 6))
        path = a.solve()
        
        print path

if __name__ == '__main__':
    t = Test()
    t.test_maze()