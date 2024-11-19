import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
       i = Runner("test")
       for _ in range(10):
           i.walk()
       self.assertEqual(i.distance, 50)

    def test_run(self):
        j = Runner("test2")
        for _ in range(10):
            j.run()
        self.assertEqual(j.distance, 100)

    def test_challenge(self):
        ii = Runner("test3")
        jj = Runner("test4")
        for _ in range(10):
            ii.walk()
            jj.run()
        self.assertNotEqual(ii.distance, jj.distance)


if __name__ == '__main__':
    unittest.main()

"""
Если в классе Runner сменить дистанцию или в классе RunnerTest range и/или сравниваемую дистанцию, 
то тест будет провален - условие будет ложным (AssertionError)
"""