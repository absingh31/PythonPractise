
a = [1,2,3,4,5,7,8,9,10,6,12]

def missing(arr):
    sum1=0
    sum2=0
    for x in arr:
        sum1 ^= x
    for i in range(1, len(arr)+2):
        sum2^=i
    print(sum1^sum2)

if __name__ == '__main__':
    missing(a)