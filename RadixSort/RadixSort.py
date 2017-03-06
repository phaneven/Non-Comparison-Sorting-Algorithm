# LSD
# BucketSort orders up these 'buckets' and appends them into one array.
# However, RadixSort appends the buckets without further sorting and 're-buckets'
# it based on the second digit (ten's place) of the numbers.
# Hence, BucketSort is more efficient for 'Dense' arrays,
# while RadixSort can handle sparse (well, not exactly sparse, but spaced-out) arrays well. (from Stackoverflow)
class Solution:
    # A is the list, MAX is the largest
    def __init__(self, A, MAX):
        self.A = A
        self.MAX = 100

    # n is bucket number
    def radix_sort(self, n):
        radix = 1
        while (radix < self.MAX):
            B = [[] for i in range(n)]
            for i in range(len(self.A)):
                B[(self.A[i]//radix)%10].append(self.A[i])
            radix *= 10
            self.A = []
            for i in range(n):
                for j in range(len(B[i])):
                    self.A.append(B[i][j])

        print(self.A)
        return


def main():
    A = [33, 11, 72, 61, 22, 39, 43, 55, 67, 12, 8, 14]
    sol = Solution(A, 3)
    sol.radix_sort(10)

if __name__ == "__main__":
    main()
