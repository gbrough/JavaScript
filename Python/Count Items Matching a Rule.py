#Leetcode Count Items Matching a Rule

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dict = {'type': 0, 'color': 1, 'name': 2}
        count = 0
        for item in items:
            if item [dict[ruleKey]] == ruleValue:
                count += 1
        return count

