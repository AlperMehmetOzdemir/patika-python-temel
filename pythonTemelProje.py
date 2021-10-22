def flattenList(l):
  if len(l) == 0:
    return l
  if isinstance(l[0], list):
    return flattenList(l[0]) + flattenList(l[1:])
  return l[:1] + flattenList(l[1:])

print(flattenList([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))

def reverseRecursive(l):
  try:
    if len(l) > 1:
      return list(reverseRecursive(e) for e in reversed(l))
    return l
  except TypeError:
    return l

print(reverseRecursive( [[1, 2], [3, 4], [5, 6, 7]]))

