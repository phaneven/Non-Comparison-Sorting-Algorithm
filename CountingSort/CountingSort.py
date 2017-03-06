class Solution:
    def __init__(self, A, k):
        self.A = A
        self.k = k

    def counting_sort(self):
        C = [0 for i in range(self.k+1)]  # counting array
        B = [0 for i in range(len(self.A))]

        for j in range (len(self.A)):
            C[self.A[j]] += 1
        for i in range (1, self.k+1):
            C[i] += C[i-1]
        for j in range (len(self.A)-1, -1, -1):
            B[C[self.A[j]]-1] = self.A[j]
            C[self.A[j]] -= 1  # important!
        print(B)


def main():
    A = [2, 5, 3, 0, 2, 3, 0, 3, 33, 21]
    ans = Solution(A, 33)
    ans.counting_sort()

if __name__ == '__main__':
    main()


