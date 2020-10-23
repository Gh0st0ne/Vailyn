#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_____, ___
   '+ .;    
    , ;   
     .   
           
       .    
     .;.    
     .;  
      :  
      ,   
       

┌─[Vailyn]─[~]
└──╼ VainlyStrain
"""

import treelib, string, random
from core.colors import color

"""generates a random string, used for unique tree ids when duplicate file names"""
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

"""removes Vailyn's colors from string"""
def replaceColors(ntag):
    tag = ntag.replace(color.RD, "").replace(color.END, "").replace(color.O, "")
    return tag.replace(color.CURSIVE, "").replace(color.BOLD, "")
    
"""append file to found files tree"""
def tree_append(tree, path, parentnode):
    plist = path.split("/")
    id = plist[0]
    if not tree.contains(id):
        if len(plist) > 1:
            tree.create_node(color.END+color.CURSIVE+color.END+plist[0]+color.RD, id, parent=parentnode)
        else:
            tree.create_node(color.END+color.CURSIVE+plist[0]+color.END+color.RD, id, parent=parentnode)
    else:
        if tree.parent(id).identifier != parentnode:
            new = True
            for i in tree.children(parentnode):
                if replaceColors(i.tag) == id:
                    new = False
            if new:
                id = id + randomword(128)
                if len(plist) > 1:
                    tree.create_node(color.END+plist[0]+color.RD, id, parent=parentnode)
                else:
                    tree.create_node(color.END+color.CURSIVE+plist[0]+color.END+color.RD, id, parent=parentnode)
    if len(plist) > 1:
        tree_append(tree, "/".join(plist[1::]), id)
        
"""create the found files tree"""
def create_tree(tree, filepaths):
    for i in filepaths:
        contained = False
        #prevent dups if parent folder found
        for j in filepaths:
            if i != j and i != "" and i in j:
                contained = True
                #print("i:"+i+"\nj:"+j)
        if i != "" and not contained:
            tree_append(tree, i, "root")
