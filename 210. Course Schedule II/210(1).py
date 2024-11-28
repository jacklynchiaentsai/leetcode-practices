"""
depth first search
n = numCourses
m = len(prerequisites)
time: O(n+m)
space: O(n+m)
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_graph = {}
        taken_set = set()
        visited_set = set()

        # initialization
        for i in range(numCourses):
            course_graph[i] = []

        for prereq_list in prerequisites:
            course, prereq = prereq_list
            course_graph[course].append(prereq)

        ordering = []

        def takeClass(curClass):
            visited_set.add(curClass)
            for prereq in course_graph[curClass]:
                if prereq not in taken_set:
                    if prereq not in visited_set:
                        if takeClass(prereq) == -1:
                            return -1
                    else:
                        return -1
            
            taken_set.add(curClass)
            ordering.append(curClass)
            return 1

        for i in range(numCourses):
            if i not in taken_set:
                if takeClass(i) == -1:
                    return []
        
        return ordering
        
"""
if there is a cycle in the graph then it is impossible to finish all classes

DFS approach
given a class we want to take all of its prerequisites before taking the class itself

course_graph = {class: [list of prequisites for the class]}
-> update using prerequisites
taken_set = set(classes that has been taken)
visited_set = set(classes that I've seen as the curClass of takeClass function)

ordering = []
takeClass(curClass){
    add curClass into visited_set
    for each prereq in course_graph[curClass]:
        if prereq not in taken_set:
            if prereq not in visited_set:
                if takeClass(prereq) == -1:
                    return -1
            else:
                return -1

    add curClass into taken_set
    update ordering
    return 1
}

A -> B
B -> A
"""
