
import numpy as np


class Grid(object):
    def __init__(self, size, Jfactor):
        self.size = size
        self.Jfactor = Jfactor
        self.canvas = np.ones([size, size], int)

    def randomize(self):
        self.canvas = np.random.randint(0, 2, [self.size, self.size]) * 2 - 1

    def set_positive(self):
        self.canvas = np.ones([self.size, self.size], int)

    def set_negative(self):
        self.canvas = -np.ones([self.size, self.size], int)

    def left(self, x, y):
        if x < 0.5:
            return [self.size - 1, y]
        else:
            return [x - 1, y]

    def right(self, x, y):
        if x > self.size - 1.5:
            return [0, y]
        else:
            return [x + 1, y]

    def up(self, x, y):
        if y < 0.5:
            return [x, self.size - 1]
        else:
            return [x, y - 1]

    def down(self, x, y):
        if y > self.size - 1.5:
            return [x, 0]
        else:
            return [x, y + 1]

    # Calculate energies and magnetizations

    def unitE(self, x, y):
        [leftx, lefty] = self.left(x, y)
        [rightx, righty] = self.right(x, y)
        [upx, upy] = self.up(x, y)
        [downx, downy] = self.down(x, y)
        return -self.Jfactor * self.canvas[x, y] * \
            (self.canvas[leftx, lefty] + self.canvas[rightx, righty] +
             self.canvas[upx, upy] + self.canvas[downx, downy])

    def deltaE(self, x, y):
        return -4 * self.unitE(x, y)


    def totalM(self):
        return np.sum(self.canvas)

    def avrM(self):
        return self.totalM() / (self.size * self.size)

    # Cluster flip (Wolff method)
    #每一次clusterflip都生成并翻转一个cluster，返回一个clustersize
    def clusterFlip(self, temperature):
        """Cluster flip (Wolff method)"""

        # Randomly pick a seed spin

        x = np.random.randint(0, self.size)
        y = np.random.randint(0, self.size)

        sign = self.canvas[x, y]
        P_add = 1 - np.exp(-2 * self.Jfactor / temperature)
        stack = [[x, y]]
        lable = np.ones([self.size, self.size], int)
        lable[x, y] = 0

        while len(stack) > 0.5:

            # While stack is not empty, pop and flip a spin

            [currentx, currenty] = stack.pop()
            self.canvas[currentx, currenty] = -sign

            # Append neighbor spins

            # Left neighbor

            [leftx, lefty] = self.left(currentx, currenty)

            if self.canvas[leftx, lefty] * sign > 0.5 and \
                    lable[leftx, lefty] and np.random.rand() < P_add:
                stack.append([leftx, lefty])
                lable[leftx, lefty] = 0

            # Right neighbor

            [rightx, righty] = self.right(currentx, currenty)

            if self.canvas[rightx, righty] * sign > 0.5 and \
                    lable[rightx, righty] and np.random.rand() < P_add:
                stack.append([rightx, righty])
                lable[rightx, righty] = 0

            # Up neighbor

            [upx, upy] = self.up(currentx, currenty)

            if self.canvas[upx, upy] * sign > 0.5 and \
                    lable[upx, upy] and np.random.rand() < P_add:
                stack.append([upx, upy])
                lable[upx, upy] = 0

            # Down neighbor

            [downx, downy] = self.down(currentx, currenty)

            if self.canvas[downx, downy] * sign > 0.5 and \
                    lable[downx, downy] and np.random.rand() < P_add:
                stack.append([downx, downy])
                lable[downx, downy] = 0

        # Return cluster size

        return self.size * self.size - sum(sum(lable))
