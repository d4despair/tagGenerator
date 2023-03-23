# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/18 16:21

from taggen.tag import Tag

import keyword
print(type(keyword.kwlist))
print(keyword.kwlist)
t = Tag('name', 'type', 'comment')
print(t)
print(t.__init_subclass__())
