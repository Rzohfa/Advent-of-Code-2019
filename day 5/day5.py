import intcomp as comp


def task():
    comp.load_listing('input.txt')
    comp.intcode_computer(False)


if __name__ == '__main__':
    task()