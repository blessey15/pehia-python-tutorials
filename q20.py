from typing import Any, Union


class seven:
    def __init__(self, n):
        super(seven, self).__init__()
        self.n = n

    def div_seven(self):
        for n in range(0, self.n, 7):
            yield n


for i in seven(30).div_seven():
    print(i)
