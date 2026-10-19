class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        results = []
        dict_sets = {}
        
        for i in range(len(strs)):
            val = tuple(sorted(strs[i]))
            if val not in dict_sets:
            #     dict_sets[val].append(strs[i])
            # else:
                dict_sets[val] = []
            
            dict_sets[val].append(strs[i])
        
        
        for _,v in dict_sets.items():
            results.append(v)
            
        return results