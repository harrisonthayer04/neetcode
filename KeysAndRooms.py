class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        keys = [0]
        i = 0

        while i < len(keys):
            r = keys[i]
            for k in rooms[r]:
                if k not in visited:
                    visited.add(k)
                    keys.append(k)
            i += 1
        return len(visited) == len(rooms)



# Go to room 0
# get the keys in room 0 
# then go to the rooms we can unlock with room 0s keys
# keep repeating until we have visited every room or we have run out of keys

# rooms = [[1,3], [3,0,1], [2,1], [0]]
#                                  ^
#
#
#
#
#
# list of keys = [0, 1, 3] # maybe a hashmap? maybe default dict?
#                          ^
# if we get to the end the keys hashmap 