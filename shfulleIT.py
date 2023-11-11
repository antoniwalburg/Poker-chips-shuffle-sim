import matplotlib.pyplot as plt

x = []
for i in range(4, 1001, 2):
    x.append(i)

stack = []
for t in x:
    helper = []
    for i in range(1, (t // 2) + 1):
        helper.append(1)
    for j in range(1, (t // 2) + 1):
        helper.append(0)
    stack.append(helper)


def shuffle(n):
    step_counter = 0
    half_1 = n[0:len(n) // 2]
    half_2 = n[len(n) // 2:len(n)]
    while True:
        single_shuffle = [item for pair in zip(half_1, half_2) for item in pair]
        step_counter += 1
        half_1 = single_shuffle[0:len(single_shuffle) // 2]
        half_2 = single_shuffle[len(single_shuffle) // 2:len(single_shuffle)]
        if single_shuffle == n:
            break
        if single_shuffle == n[::-1]:
            print("It reversed!")
    return step_counter


steps = []
for k in stack:
    steps.append(shuffle(k))

plt.bar(x, steps,width=1.5,  edgecolor="white", linewidth=1)

# Add labels and title
plt.xlabel('Number of chips')
plt.ylabel('Number of steps')
plt.title('Ratio of chips to steps')

# Show the plot
plt.show()
print(range(len(steps)))