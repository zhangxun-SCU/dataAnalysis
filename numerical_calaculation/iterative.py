
def iterative(start, times):
    x_t = start
    for i in range(times):
        x_t1 = (x_t + 1)**(1/3)
        x_t = x_t1
    return x_t


if __name__ == '__main__':
    print(iterative(1.5, 16))

