import time

def my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum


sz = 10000000
testdata = range(sz)

t0 = time.process_time()
my_result = my_sum(testdata)
t1 = time.process_time()
print(f'My result: {my_result} (Processed time:{t1-t0:.4f})')

t2 = time.process_time()
their_result = sum(testdata)
t3 = time.process_time()

print(f'Their result: {their_result} (Processed time:{t3-t2:.4f}')
