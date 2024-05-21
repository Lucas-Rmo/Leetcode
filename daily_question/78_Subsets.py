class Solution(object):
    def subsets(self, nums):
    # Start with an empty list that will eventually hold all subsets
        subsets = [[]]
        
        # Iterate over each element in the original list
        for element in nums:
            # For each existing subset, create a new subset that includes the current element
            new_subsets = []
            for subset in subsets:
                # Create a new subset that includes the current element
                new_subset = subset + [element]
                # Add the new subset to the list of new subsets
                new_subsets.append(new_subset)
            
            # Add all new subsets to the list of all subsets
            subsets.extend(new_subsets)
        
        return sorted(subsets)
