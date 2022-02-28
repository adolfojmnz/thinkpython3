nested = ["hello", 2.0, 5, [10, 20]]
nested[3].append([15, 16])
             #  0      1   2         (3)      
# nested =  ["hello", 2.0, 5, [10, 20, [15, 16]]]
                             # 0   1 (2)|0  (1)   
                                            
print(nested[3][2][1])                  # [3]: List 0, element 3 | [2] list 2, element 1.

