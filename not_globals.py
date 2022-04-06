# https://betterprogramming.pub/alternatives-to-using-globals-in-python-a3b2a7d5411b


# Create class
class Init:
    def __init__(self, init_: bool):
        self.init = init_


def init():
    init_.init = True
    print('Will Init')


def run():
    print('Will Run')
    if init_.init:
        print('Already initiated')
    if not init_.init:
        init()


if __name__ == '__main__':
    # Create Instance of the class
    init_ = Init(False)

    # run()
    # run()
    # run()
    run()

    # Output:
    # Will Run
    # Will Init
    # Will Run
    # Already initiated
