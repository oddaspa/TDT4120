from sys import stdin


class Record:
    value = None
    next = None

    def __init__(self, value):
        self.value = value
        self.next = None


def search(record):
    max = -1
    while record is not None:
        if record.value > max:
            max = record.value
        record = record.next
    return max


def main():
    # reading from stdin and creating a linked list
    first = None
    last = None
    for line in stdin:
        penultimate = last
        last = Record(int(line))
        if first is None:
            first = last
        else:
            penultimate.next = last

    # searching and printing out the result
    print(search(first))


if __name__ == "__main__":
    main()
