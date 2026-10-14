class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def topologicalSort(indegree, adj, numCourses):
            q = collections.deque()
            count = 0
            for i in range(len(indegree)):
                if indegree[i] == 0:
                    q.append(i)
                    count += 1
            while q:
                u = q.popleft()
                for v in adj[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
                        count += 1
            return count == numCourses

        indegree = [0] * numCourses
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        return topologicalSort(indegree, adj, numCourses)