class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque()
        visited = set(deadends)

        q.append(["0000", 0])
        def children(lock):
            res = []
            for i in range(4):
                new_val = str((int(lock[i]) + 1)%10)
                res.append(lock[:i] + new_val + lock[i+1:])
                new_val_decrement =  str((int(lock[i]) - 1 + 10)%10)
                res.append(lock[:i] + new_val_decrement + lock[i+1:])
            return res

        while q:
            node, turns = q.popleft()
            if node == target:
                return turns
            if node not in visited:
                print(node, turns)
                visited.add(node)
                for lock in children(node):
                    q.append([lock, turns+1])
        
        return -1
                
