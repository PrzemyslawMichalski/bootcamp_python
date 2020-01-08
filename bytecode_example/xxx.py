program = """
x=1
y=2
print(x+y)
"""

import dis

print(dis.dis(program))