# for i in range(5):
#    print(i)

# for i in range(5):
#    print(i, end="")

# for i in range(5):
#    print(f"{i:5}", end="")

for i in range(10):
    print(f"{i:8}", end="")

print()
print()
for i in range(10):
    print(i, end="")
    for j in range(10):
        print(f"{i*j:8}", end="   ")
    print()


