
def csv21list(filepath):
  file = open(filepath)
  first = True

  L = []
  for line in file:
    if first:
      first = False
      continue

    L.append(line.strip().split(","))

  return L