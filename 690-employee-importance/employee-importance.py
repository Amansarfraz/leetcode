"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """

        emp_map = {e.id: e for e in employees}

        def dfs(emp_id):
            emp = emp_map[emp_id]
            total = emp.importance

            for sub_id in emp.subordinates:
                total += dfs(sub_id)

            return total

        return dfs(id)