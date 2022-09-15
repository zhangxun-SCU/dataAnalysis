def polynomial(nums):
    """

    :param nums:
    :return:
    """
    len_ = len(nums)

    def f(x):
        _sum = 0
        for i in range(len_):
            _sum += nums[i] * x ** (len_ - i - 1)
        return _sum

    return lambda x: f(x)