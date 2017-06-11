class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        n = len(ratings)
        results = [1] * n

        inc = 1
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                inc += 1
                results[i] = max(results[i], inc)
            else:
                inc = 1

        inc = 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                inc += 1
                results[i] = max(results[i], inc)
            else:
                inc = 1

        return sum(results)



if __name__ == '__main__':
    data = [1, 3, 5]
    print Solution().candy(data)
