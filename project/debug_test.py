

class DebugTest:
    def __init__(self):
        pass

    def hello_world(self):
        print('Put a breakpoint on this line to test breakpoints!')
        print('Hello World!')


if __name__ == "__main__":
    test_class = DebugTest()
    test_class.hello_world()

    print("Test Program Finished")
