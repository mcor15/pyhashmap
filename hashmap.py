# Hash Map implementation
# Simplistic hash function and linear probing for hashing collisions.
# 
#Based on the specification at...
#https://www.cs.emory.edu/~cheung/Courses/253/Syllabus/Map/intro.html

class HashMap:
   
    #Constructor. Using a default of 10 buckts to hash to.
    def __init__(self, buckets=10):
        self.entryCount = 0
        self.buckets = buckets
        #Store (key, value) pairs as a list [key, value] in  as list. [[key1, value1], [key2, value2], [key3, value3], ...]
        self.table = [None] * buckets

    #Returns the number of (key, value) pairs in the hash map.
    def size(self):
        return self.entryCount
    
    #Hash funcation using Python hash().
    def hashKey(self, key):
        return abs(hash(key)) % self.buckets
     
    #Checks if the hash map is empty. 
    def isEmpty(self):
        return self.entryCount == 0
    
    #Helper method to check if keys are not None.
    def checkNone(self, value):
        if value == None:
            raise ValueError("None cannot be used as a key.")
         
    #Returns the value paired to the key parameter.
    def get(self, key):
        
        #Type check
        self.checkNone(key)
       
        #Get hash of key.
        index = self.hashKey(key)
        
        #Key is not here.
        if self.table[index] == None:
            raise KeyError("{} is not a key of the hash map.".format(key))

        #Linear prob to find the key.
        for e in self.table[index]:
            if e[0] == key:
                #We found the key.
                return e[1]
        #We did not find the key.
        raise KeyError("{} is not a key of the hash map.".format(key))
     
    # Add or replace a value paired to key.
    def put(self, key, value):
        
        #Type check
        self.checkNone(key)
        
        #Get hash of key.
        keyIndex = self.hashKey(key)
        
        #Key not in hash map. Add it with value.
        if self.table[keyIndex] == None:
            self.table[keyIndex] = [[key,value]]
            self.entryCount += 1
        else:
            #Hash of key does exist in hash map. Check keys.
            keyValueUpdated = False
            
            for e in self.table[keyIndex]:
                if e[0] == key:
                    e[1] = value
                    #Key is here. Update value.
                    keyValueUpdated = True
                    break
            #Hash is here but key is not. Add (key, value) pair.
            if not keyValueUpdated:
                self.table[keyIndex].append([key, value])
                self.entryCount += 1
               
    # Remove key and paired value.     
    def remove(self, key):
        self.checkNone(key)
        keyIndex = self.hashKey(key)
        
        # Key is not in hash map.
        if self.table[keyIndex] == None:
            raise KeyError("{} is not a key of the hash map.".format(key))
        
        removed = False
        
        #Linear search for key and then remove it.
        for e in self.table[keyIndex]:
            if e[0] == key:
                self.table[keyIndex].remove([key,self.get(key)])
                self.entryCount -= 1
                removed = True
                
        # Key is not in hash map.       
        if not removed:
            raise KeyError("{} is not a key of the hash map.".format(key))
         
           
    #Return of list of keys in the hash map.
    def keySet(self):
        if self.isEmpty():
            return []
        keys = []
        for e in self.table:
            if e == None:
                continue
            else:
                for pair in e:
                    keys.append(pair[0])
        return keys
        
    #Return of list of values in the hash map.       
    def valueSet(self):
        if self.isEmpty():
            return []
        values = []
        for e in self.table:
            if e == None:
                continue
            else:
                for pair in e:
                    values.append(pair[1])
        return values
       
    # Returns the (key, value) pairs as a list of lists. [[key1, value1], [key2, value2], [key3, value3], ...]
    def entrySet(self):
        if self.isEmpty():
            return []
           
        entries = []
        for e in self.table:
            if e == None:
                continue
            for pair in e:
                entries.append([pair[0],pair[1]])
        return entries
   
    # Equlaity check implementation.
    def __eq__(self, other):
        
        # If compairsion is to another HashMap instance.
        if isinstance(other, HashMap):
            return self.entrySet() == other.entrySet()
            
        # If compairsion is a Python Dictionary.  
        elif isinstance(other, dict):
            
            self_entries = self.entrySet()
            other_entries = list(other.items())
            
            # Put these into the same order.
            self_entries.sort()
            other_entries.sort()
            
            # Not same number of pairs.
            if not len(self_entries) == len(other_entries):
                return False
                
            #Check that each key and value match.
            for other_e, self_e in zip(other_entries, self_entries):
                if not other_e[0] == self_e[0] and other_e[1] == self_e[1]:
                    return False
            
            return True
        else:
            #Let caller know we have not implementated this compairsion.
            return NotImplemented
       
       