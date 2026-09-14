class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        # Map the first element of each piece to the piece itself
        piece_map = {piece[0]: piece for piece in pieces}
        
        i = 0
        while i < len(arr):
            # If the current element in arr isn't the start of any piece, return False
            if arr[i] not in piece_map:
                return False
            
            # Get the matching piece
            target_piece = piece_map[arr[i]]
            
            # Verify if the entire piece matches the sequence in arr
            for num in target_piece:
                if arr[i] != num:
                    return False
                i += 1
                
        return True
