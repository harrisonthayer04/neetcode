class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()

        for index, character in enumerate(senate):
            if character == "R":
                R.append(index)
            else:
                D.append(index)
        while D and R:
            dturn = D.popleft()
            rturn = R.popleft()
            if rturn < dturn:
                R.append(rturn + len(senate))
            else:
                D.append(dturn + len(senate))
        return "Radiant" if R else "Dire"