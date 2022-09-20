import threading

class Cube:
    def __init__(self, edge):
        self.edge = edge

    def cube_volume(self):
        print("Volume of the cube is: ", self.edge * self.edge * self.edge)

    def cube_all_edges(self):
        print("Sum of all cube edges is: ", 12 * self.edge)

    def run(self):
        t1 = threading.Thread(target=self.cube_all_edges)
        t2 = threading.Thread(target=self.cube_volume)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

if __name__ == "__main__":
    my_cube1 = Cube(5)
    my_cube1.run()

    my_cube2 = Cube(8)
    my_cube2.run()
