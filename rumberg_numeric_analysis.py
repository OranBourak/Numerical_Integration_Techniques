from trapezoidal_integration import trapezoidal_integration

def rumberg(function, ranges, k):
    '''
    :param function:
    :param ranges:
    :param k:
    :param memo:
    :return:
    '''
    memo = dict()
    first_row(ranges, function, k, memo)
    for j in range(2, k+1):
        temp = [memo[(i, j-1)] + (1 /(4 ** (j-1) - 1)) * (memo[(i,j-1)] - memo[(i-1,j-1)]) for i in range(j, k+1)]
        for i,val in enumerate(temp,j):
            memo[(i,j)] = val
    return memo


def first_row(ranges, func, n, memo):
    '''
    calculates R_i_1 and puts it in a dictionary where the key is a tuple of (num of divisions of range,1)
    :param ranges: tuple of starting point and end point
    :param func: function
    :param n: number of partitions
    :return:
    '''

    temp = [trapezoidal_integration(func, ranges[0], ranges[1], 2 ** i) for i in range(0, n)]
    for i,val in enumerate(temp,1):
        memo[(i,1)] = val



