v=(input())
try:
  if "." in v:
    val=float(v)
    print("yes")
  else:
    val=int(v)
    print("yes")
except ValueError:
  print("No")
