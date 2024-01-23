#!/usr/bin/env python
# coding: utf-8

# In[2]:


def product_except_self(nums):
    n = len(nums)
    
    
    left_products = [1] * n
    right_products = [1] * n
    
    left_product = 1
    for i in range(n):
        left_products[i] = left_product
        left_product *= nums[i]
    
    right_product = 1
    for i in range(n - 1, -1, -1):
        right_products[i] = right_product
        right_product *= nums[i]
    
    answer = [left_products[i] * right_products[i] for i in range(n)]
    
    return answer



# In[3]:


nums1 = [1, 2, 3, 4]
output1 = product_except_self(nums1)
print(output1) 


# In[4]:


nums2 = [-1, 1, 0, -3, 3]
output2 = product_except_self(nums2)
print(output2)  


# In[ ]:




