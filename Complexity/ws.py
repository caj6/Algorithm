#1.
def fibo(n):
    if n <= 1:
        return n;
    else:
        return fibo(n - 1) + fibo(n - 2);
    
# O(2^n)
#--------------------------------------------------------------------------------------
#2.
def bubble(l):
    n = len(l);
    for i in range(n):
        swap = False;
        for j in range(0, n-i, 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j];
                swap = True;
            if not swapp:
                break;
                
# best case : O(n)
# average case : O(n^2)
# worst case : O(n^2)

def merge(l):
    if len(l) > 1:
        mid = len(l) // 2;
        left = l[:mid];
        right = l[mid:];
        
        merge(left);
        merger(right);
        
        i = j = k = 0;
        
        while i < len(left) and j < len(right):
            if left[i] < right [j]:
                l[k] = left[i];
                i += 1;
            else:
                l[k] = right[j];
                j += 1;
            k += 1;
            
        while i < len(left):
            l[k] = left[i];
            j += 1;
            k += 1;
        
        while i < len(right):
            l[k] = right[i];
            j += 1;
            k += 1;

# best case : O(n log n)
# average case : O(n log n)
# worst case : O(n log n)

#---------------------------------------------------------------------------------------

#4. Bubble sort : O(1) while O(n) for the merger sort

#---------------------------------------------------------------------------------------
var = {1 : "jan is no that bad?", 2 : "feb", 3 : "mar"};
#print(hash(var[2]))

def hashy(k,s):
    return sum(ord(a) for a in k) % s
    return len(k) % s

#print("hashy of 'jan' :", hashy("jan", 5))
#print("hashy of 'naj' :", hashy("naj", 5))

class chaining:
    def __init__(self, s):
        self.s = s;
        self.t = [[] for _ in range(s)];
        
    def _hashy(self, k):
        return hash(k) % self.s;
    
    def insert(self, k, v):
        index = self._hashy(k);
        for n in self.t[index]:
            if n[0] == k:
                n[1] = v;
                return
        self.t[index].append([k,v]);
            
    def look(self,k):
        index = self._hashy(k);
        for n in self.t[index]:
            if n[0] == k:
                return n[1]
        return None
    
th = chaining(5);
th.insert("jan", 1);
th.insert("feb", 2);
th.insert("mar",3);
#print(th.look("feb"));
#---------------------------------------------------------------------------------------------
class probing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_index = self._hash(key)
        while self.table[hash_index] != None:
            pair = self.table[hash_index]
            if pair[0] == key:
                pair[1] = value
                return
            hash_index = (hash_index + 1) % self.size
        self.table[hash_index] = [key, value]
    
    def lookup(self, key):
        hash_index = self._hash(key)
        count = 0
        while count < self.size and self.table[hash_index] != None:
            if self.table[hash_index][0] == key:
                return self.table[hash_index][1]
            hash_index = (hash_index + 1) % self.size
            count += 1
        return None

#-------------------------------------------------------------------------------------------------------------------------------------------------
#5.
def binary(n, t):
    l, r = 0, len(n) - 1;
    if l <= r:
        m = (l + r) // 2;
        if n[m] == t:
            return True
        elif n[m] < t:
            l = m + 1
        else:
            r = m - 1
    return False

# O(log n)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#6.
def counter(l):
    seen = {};
    for i in l:
        if i not in seen:
            seen[i] = 0;
        seen[i] += 1;
    return seen;

# O(n)

#---------------------------------------------------------------------------------------------------------------------------------------
#7.
def hashmap(d,t):
    for i in d.values():
        if i == t:
            return True;
    return False;
        
# O(n)
