class MonsterClassificationAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        self.positives = {}
        self.negatives = {}
        pass

    def solve(self, samples, new_monster):
        #Populate positive/negative entries if they are empty.
        if not self.positives and not self.negatives:
            self.cache_positive_negatives(samples)
            
        #Base case. 
        #Perhaps A monster happens to have the same features as another case seen before.
        if any (new_monster == monster for monster in self.positives.values()):
            return True
        elif any (new_monster == monster for monster in self.negatives.values()):
            return False
        #Find the difference in distance between our new monster, and existing positives.
        
        
        
        #Add your code here!
        #
        #The first parameter to this method will be a labeled list of samples in the form of
        #a list of 2-tuples. The first item in each 2-tuple will be a dictionary representing
        #the parameters of a particular monster. The second item in each 2-tuple will be a
        #boolean indicating whether this is an example of this species or not.
        #
        #The second parameter will be a dictionary representing a newly observed monster.
        #
        #Your function should return True or False as a guess as to whether or not this new
        #monster is an instance of the same species as that represented by the list.
        pass
    
    def cache_positive_negatives(self, samples):
        for monster_dict, is_positive in samples:
            if (is_positive):
                self.positives[len(self.positives)] = monster_dict
            else:
                self.negatives[len(self.negatives)] = monster_dict
        print(self.positives)
        
        
    def find_closest_positive(self, target_monster, positives, negatives):
        closest_match = None
        smallest_diff = None
        for entry in positives:
            diff = self.distance_difference(target, entry)
            if diff < smallest_diff:
                smallest_diff = diff
                closest_match = entry
                
    def find_closest_negative(self, target_monster, negatives):
        closest_match = None
        smallest_diff = None
        for entry in negatives:
            diff = self.distance_difference(target, entry)
            if diff < smallest_diff
            smallest_diff = diff
            closest_match = entry
