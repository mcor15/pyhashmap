import unittest
from hashmap import HashMap

class HashMapTests(unittest.TestCase):
   
    def testKeysSet(self):
        data_keys = ['a','b','c','d','e','f','g','h','i']
        data_values = [2,5,7,3,81,11,888,13,3]
        hashMap = HashMap()
        for key, value in zip(data_keys, data_values):
            hashMap.put(key, value)
        self.assertEqual(hashMap.keySet().sort(),data_keys.sort())

    def testValueSet(self):
        data_keys = ['a','b','c','d','e','f','g','h','i']
        data_values = [2,5,7,3,81,11,888,13,3]
        hashMap = HashMap()
        for key, value in zip(data_keys, data_values):
            hashMap.put(key, value)
        self.assertEqual(hashMap.valueSet().sort(),data_values.sort())

    def testEntrySet(self):
        data_keys = ['a','b','c','d','e','f','g','h','i']
        data_values = [2,5,7,3,81,11,888,13,3]
        hashMap = HashMap()
        data_pairs = []
        for key, value in zip(data_keys, data_values):
            hashMap.put(key, value)
            data_pairs.append([key, value])
        self.assertEqual(hashMap.entrySet().sort(),data_pairs.sort())
         
    def testIfHashMapIsEmpty(self):
        hm = HashMap()
        self.assertTrue(hm.isEmpty())
     
    def testAddOneEntry(self):
        hm = HashMap()
        hm.put('a',13)
        self.assertEqual(hm.get('a'), 13)
       
    def testAddManyEntry(self):
        hm = HashMap()
        hm.put('a', 13)
        hm.put('b', 22)
        hm.put('c', 102)
        self.assertTrue(hm.size() == 3)
       
    def testRemoveOneEntry(self):
        hm = HashMap()
        hm.put('a',13)
        hm.remove('a')
        self.assertTrue(hm.size() == 0)
        
    def testRemoveManyEntry(self):
        hm = HashMap()
        hm.put('a', 13)
        hm.put('b', 22)
        hm.put('c', 102)
        
        hm.remove('a')
        hm.remove('b')
        self.assertTrue(hm.size() == 1)
       
    def testUpdateValue(self):
        hm = HashMap()
        hm.put('a',13)
        hm.put('a',7)
        self.assertTrue(hm.get('a')==7)
       
    def testHashMapSameAsPythonDict(self):
        data_keys = ['a','b','c','d','e','f','g','h','i']
        data_values = [2,5,7,3,81,11,888,13,3]
       
        pydict = {}
        hm = HashMap()
        for k, v in zip(data_keys, data_values):
            hm.put(k, v)
            pydict[k] = v
        self.assertEqual(hm, pydict)
           
    def testIsEqual(self):
        data_keys = ['a','b','c','d','e','f','g','h','i']
        data_values = [2,5,7,3,81,11,888,13,3]
       
        hm1 = HashMap()
        hm2 = HashMap()
        for k, v in zip(data_keys, data_values):
            hm1.put(k, v)
            hm2.put(k, v)
        self.assertEqual(hm1, hm2)
        
    def testIsNotEqual(self):
        data_keys = ['a','b','c','d','e','f','g','h','i']
        data_values = [2,5,7,3,81,11,888,13,3]
       
        hm1 = HashMap()
        hm2 = HashMap()
        for k, v in zip(data_keys, data_values):
            hm1.put(k, v)
            hm2.put(k, v+1)
        self.assertNotEqual(hm1, hm2)

    def testNoneKeyPut(self):
        hm = HashMap()
        self.assertRaises(ValueError, hm.put, None, 1) 
        
    def testNoneKeyGet(self):
        hm = HashMap()
        self.assertRaises(ValueError, hm.get, None) 
        
    def testKeyNotInHashMap(self):
        hm = HashMap()
        self.assertRaises(KeyError, hm.get, 'NotHere') 
        
    def testKeyNotInHashMapSameHash(self):
        hm = HashMap(buckets=1)
        hm.put("a", "£")
        self.assertRaises(KeyError, hm.get, 'NotHere') 
        
    def testRemoveKeyNotInHashMap(self):
        hm = HashMap()
        self.assertRaises(KeyError, hm.remove, 'NotHere') 
        
    def testRemoveKeyNotNone(self):
        hm = HashMap()
        self.assertRaises(ValueError, hm.remove, None) 
        
    def testRemoveKeyNotInHashMapSameHash(self):
        hm = HashMap(buckets=1)
        hm.put("a", "£")
        self.assertRaises(KeyError, hm.get, 'NotHere')  
        
if __name__ == "__main__":
    unittest.main()
    