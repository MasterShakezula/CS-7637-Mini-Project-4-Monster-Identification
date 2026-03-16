#This agent is using case-based reasoning (CBR) and difference distancing.
#I calculate, quantitatively, the difference between a monster, versus old cases. And take the avg.
#But right now, I don't weigh any of the unique traits. 
#I will try to add this consideration.

class MonsterClassificationAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, samples, new_monster):
        #Populate positive/negative entries if they are empty.
        positives, negatives = self.get_positive_negative(samples)
            
        #Base case. 
        #Perhaps A monster happens to have the same features as another case seen before.
        if any (new_monster == monster for monster in positives):
            return True
        if any (new_monster == monster for monster in negatives):
            return False
            
        weight = self.get_trait_weight(positives, negatives, new_monster)
        
        if weight > 0:
            return True
        if weight < 0:
            return False
        #Compare average difference in a quantified "distance" number, of how different
        #our new monster is to our positive groups, versus out negative groups
        #smaller diff = more similar. 
        #If more similar to positives, return true. If more similar to negatives, return false.
        average_pos_distance = self.find_avg_diff_dist(new_monster, positives)
        average_neg_distance = self.find_avg_diff_dist(new_monster, negatives)
        
        
        #More likely a match(?)
        if average_pos_distance < average_neg_distance:
            print("Avg Positive Distance: ", average_pos_distance)
            return True
        elif average_neg_distance < average_pos_distance:
            print("Avg Negative Distance: ", average_neg_distance)
            return False
            
        #Edge case, avg distance are the same. Check local case differences. 
        closest_local_positive = self.find_closest_dist(new_monster, positives)
        closest_local_negative = self.find_closest_dist(new_monster, negative)
        
        return closest_local_positive <= closest_local_negative #same distance, resolve this edge case.
        
        
        
        
    def get_positive_negative(self, samples):
        positives = []
        negatives = []
        for monster_traits, is_positive in samples:
            if is_positive:
                positives.append(monster_traits)
            else:
                negatives.append(monster_traits)
        return positives,negatives
        
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
    
    def find_avg_diff_dist(self, target_monster, monsters):
        if not monsters:
            return 1
        total_diff_dist = 0.0
        for monster in monsters:
            total_diff_dist += self.distance_difference(target_monster, monster)
        return total_diff_dist/len(monsters)
        
        
    def find_closest_dist(self, target_monster, monsters):
        if not monsters:
            return 1.0
        smallest_diff = None
        for monster in monsters:
            diff = self.distance_difference(target_monster, monster)
            if diff < smallest_diff:
                smallest_diff = diff
        return smallest_diff
    
    def get_trait_weight(self, positives, negatives, new_monster):
        weight = 0
        
        for trait, value in new_monster.items():
            positive_values = {mon[trait] for mon in positives}
            negative_values = {mon[trait] for mon in negatives}
            
            #check trait values in one group, but not the other. This contributes to weight
            if value in positive_values and value not in negative_values:
                weight += 1
            elif value in negative_values and value not in positive_values:
                weight -=1
                
            return weight
            
    def distance_difference(self, target, entry):
        #find sum of difference for keys present in both dictionaryies.
        all_traits = set(target.keys())
        
        #distance, for now, is normalized and weightless.
        #each commonality will be a point. 
        #For later, maybe see if different traits have a greater/lesser weight/impact on true/false
        similarity = 0
        for trait in all_traits:
            if target[trait] == entry[trait]:
                similarity += 1
        similarity = similarity/len(all_traits) #normalize.
        dist = 1.0-similarity
        print("Dist: ", dist)
        return dist
