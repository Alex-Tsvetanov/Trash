line = input()
lines = []

while line != "ANSWER ME":
  lines.append(line)
  line = input()
  
ll = {}
removed = set()

for line in lines:
  command = line.split(' ')
  if command[0] == 'ORDER':
    ll[command[2]] = command[1]
  elif command[0] == 'REMOVE':
    removed.add(command[1])

count = 0
key = 'Pesho'
queue = ['Pesho']
while key in ll:
  key = ll[key]
  queue.append(key)

#print(removed)
for key in queue:
  #print(key)
  count += int(not key in removed)

print(count)
