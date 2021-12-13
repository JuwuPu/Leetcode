# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        # if not t1:
        #     return t2
        # if not t2:
        #     return t1
        # t = TreeNode(t1.val+t2.val)
        # t.left = self.mergeTrees(t1.left, t2.left)
        # t.right = self.mergeTrees(t1.right, t2.right)
        # return t
        
        
        # initial filter for inputs to make sure they're Tree Nodes with values 
        if not t1: 
            return t2
        if not t2: 
            return t1 

        # initializing a tree node to store the merged tree 
        t = TreeNode(0)
        t.left = TreeNode(1)
        t.right = TreeNode(1)
        
        # initializing a stack 
        dfs= []
        dfs.append(t1)
        dfs.append(t2)
        dfs.append(t)  
       
        # will merge while the stack has items to merge 
        while dfs: 
            
            t_node = dfs.pop()
            t2_node = dfs.pop()
            t1_node = dfs.pop()
          
            # need to make sure the items appended are valid; otherwise 
            if t1_node and t2_node and t_node: 

                sumup = t1_node.val + t2_node.val
                t_node.val = sumup 

                if not t1_node.left: 
                    t_node.left = t2_node.left
                elif not t2_node.left and t1_node.left: 
                    t_node.left = t1_node.left
                else: 
                    dfs.append(t1_node.left)
                    dfs.append(t2_node.left)
                    if not t_node.left: 
                        t_node.left = TreeNode(0)
                    dfs.append(t_node.left)
                    
                    
                if not t1_node.right: 
                    t_node.right = t2_node.right 
                elif not t2_node.right and t1_node.right: 
                    t_node.right = t1_node.right
                else: 
                    dfs.append(t1_node.right)
                    dfs.append(t2_node.right)

                    # not super confident about this... I feel like this isn't a good method
                    if not t_node.right: 
                        t_node.right = TreeNode(0)
                    dfs.append(t_node.right)
        
        return t 
