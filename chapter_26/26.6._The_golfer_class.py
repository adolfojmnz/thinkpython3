from PriorityQueue import PriorityQueue

class Golfer:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f'{self.name:16}: {self.score}'

    def __gt__(self, other):
        return self.score < other.score


queue = PriorityQueue()

tiger = Golfer("Tiger Woods", 61)
phil = Golfer("Phil Mickelson", 72)
hal = Golfer("Hal Sutton", 69)

for item in [tiger, phil, hal]:
    queue.insert(item)

while not queue.is_empty():
    print(queue.remove())

