def sign(x):
  if x > 0:
    return 'positive'
  elif x < 0:
    return 'negative'
  else:
    return 'zero'
for x in [-1, 0, 1]:
  print(sign(x))