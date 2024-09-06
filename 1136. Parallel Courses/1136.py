from collections import deque
"""
topological sort
len(relations) = m
time: O(m+n)
space: O(m+n)
"""
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        inDegreeMap = {}
        prereqMap = {}

        for i in range(1, n+1):
            inDegreeMap[i] = 0
            prereqMap[i] = set()
        
        for relation in relations:
            prevCourse = relation[0]
            nextCourse = relation[1]

            inDegreeMap[nextCourse] += 1
            prereqMap[prevCourse].add(nextCourse)

        minSem = 1
        remainingCourses = n

        queue = collections.deque([])

        for key, value in inDegreeMap.items():
            if value == 0:
                queue.append([key, 1])

        while len(queue) > 0:
            item = queue.popleft()
            prereq = item[0]
            semester = item[1]

            minSem = max(minSem, semester)

            remainingCourses -= 1

            for course in prereqMap[prereq]:
                inDegreeMap[course] -= 1
                if inDegreeMap[course] == 0:
                    queue.append([course, semester + 1])

        if remainingCourses > 0:
            return -1
        else:
            return minSem
        
"""
inDegreeMap: {nodeNum: in-degree}
prerequisiteMap: {nodeNum: set(courses that has nodeNum as prerequisite)}
queue = [[nodeNum with in-degree 0 , semester]]
minSem
remainingCourses 
"""
