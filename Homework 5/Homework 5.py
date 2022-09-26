import time
from multiprocessing import Pool, cpu_count
import concurrent.futures


def factorize(*number):
    start = time.time()
    result = [[] for _ in range(len(number))]
    for num in number:
        for i in range(1, num+1):
            if num % i == 0:
                result[number.index(num)].append(i)
        elapsed = time.time() - start
        print("Времени затрачено: {:.5f}s".format(elapsed))
    return result

    raise NotImplementedError()


if __name__ == '__main__':
    print('____________ Без использования потоков и процессов:___________')
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print()

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553,
                 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


    #Processes
    print('____________ С использованием процессов:___________')

    with Pool(processes=cpu_count()) as pool:
        a, b, c, d = pool.map(factorize, [128, 255, 99999, 10651060])
    print()

    a = [i for i in a[0]]
    b = [i for i in b[0]]
    c = [i for i in c[0]]
    d = [i for i in d[0]]

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553,
                 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    #Treads
    print('____________ С использованием потоков:___________')

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        a, b, c, d = executor.map(factorize, [128, 255, 99999, 10651060])

    a = [i for i in a[0]]
    b = [i for i in b[0]]
    c = [i for i in c[0]]
    d = [i for i in d[0]]

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553,
                 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]