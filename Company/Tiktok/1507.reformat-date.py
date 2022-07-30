#
# @lc app=leetcode id=1507 lang=python3
#
# [1507] Reformat Date
#

# @lc code=start
class Solution:
    def reformatDate(self, date: str) -> str:
        """
        T : O(1) 55.71% | 45ms
        S : O(1) 18.43% | 14mb
        """
        # Dictionary
        monthDict = {'Jan': '01', 'Feb': '02',
                     'Mar': '03', 'Apr': '04',
                     'May': '05', 'Jun': '06',
                     'Jul': '07', 'Aug': '08',
                     'Sep': '09', 'Oct': '10',
                     'Nov': '11', 'Dec': '12'}

        # Split by whitespace
        parser = date.split()
        day = parser[0][:-2]  # remove 'th'
        month = monthDict[parser[1]]
        year = parser[2]

        # Adds 0 to the front of day if day < 10
        if int(day) < 10:
            day = '0' + day

        return f"{year}-{month}-{day}"

# @lc code=end
