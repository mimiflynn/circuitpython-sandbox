test = 'Turn Right onto Road'
direction = ''

if 'light' in test:
    direction = 'turn right'

if 'left' in test:
    direction = 'turn left'

if 'south' in test:
    direction = 'head south'

print(direction)
print(test.split())