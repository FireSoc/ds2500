import statistics

def find_variance(x):
    if not x:
        return None
    else:
        n = len(x)
        avg = sum(x) / n
        numerator = sum((i-avg)**2 for i in x)
        return numerator


lst = [1, 2, 3, 4, 5]

print(find_variance(lst))
sample_variance = statistics.variance(lst)
print(sample_variance)