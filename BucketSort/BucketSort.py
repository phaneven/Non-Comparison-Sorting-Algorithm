class Solution:
    def __init__(self, A):
        self.A = A

    def bucket_sort(self, n):
        B = [[] for i in range(n)]
        for i in range(len(self.A)):
            B[self.A[i]//10].append(self.A[i])
        for i in range(n):
            B[i].sort()
        l = []
        for i in range(n):
            for j in range(len(B[i])):
                l.append(B[i][j])
        print(l)
        return l


def main():
    A = [29, 25, 3, 49, 9, 37, 21, 43]
    print(A)
    sol = Solution(A)
    sol.bucket_sort(10)

if __name__ == '__main__':
    main()
