class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if total + num > target:
                    continue

                path.append(num)
                
                backtrack(i, path, total + num)

                path.pop()

        backtrack(0, [], 0)
        return result