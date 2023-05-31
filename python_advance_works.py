# # Python Advance Works

# In[11]:


#Take n number, plus every numbers in the n until it becomes 1 digit. And return this action's count.
def continuity_added(n):
    count = 0
    while n > 9:
        n = sum(int(i) for i in str(n))
        count += 1
    return count


# In[12]:


continuity_added(1679583)


# In[5]:


#A function that return the SHA-256 hash value from the giving value.
import hashlib
def sha256_hash(hash):
    string = hashlib.sha256(hash.encode('utf-8')).hexdigest()
    return string


# In[4]:


sha256_hash("password123")


# In[19]:


#The word that have missing letter is complatable or not?
def is_complatable(letter,word):
    letter = list(letter)
    for i in word:
        if i == letter[0] : letter.remove(letter[0]) 
    return not letter


# In[25]:


is_complatable("ggzel","güzel")


# In[14]:


def prime_word(sentence):
    value = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sentence = sentence.upper()
    sentence = list(sentence)
    for i in sentence:
            if i in alphabet:
                value += int(alphabet.index(i))+1
            elif i.isdigit():
                value += int(i)
            else:
                pass
    return value


# In[16]:


prime_word("ABc!abc...@123")


# In[42]:


#IF the cell is 1, the cell isnT locked, and if it is 0, the cell is locked. IF cell isn't locked jailed can escape.
#When a jailed escape, 1's returns 0, 0's returns 1. The function counts how many jailed is escape?
def escape_jail(jailed):
    if jailed[0] == 0:
            return 0
    escap = 1
    for i in range(1,len(jailed)):
        if jailed[i] != jailed[i-1]:
            escap += 1
    return escap


# In[44]:


escape_jail([1,1,0,0,0,1,0])


# In[33]:


# Count backward the num and print the string 
def backwards(num,st):
    res = ""
    num = int(num)+1
    while num > 1:
        num = num - 1
        res += str(num)+"."
    res += st+"!"
    return res
def backwards1(num,st):
    res = ""
    num = int(num)
    for i in range(num):
        res = res + str(num-i) + ". "
    res = res + st
    return res


# In[36]:


backwards(7,"HEMEN"),backwards1(7,"HEMEN!")

