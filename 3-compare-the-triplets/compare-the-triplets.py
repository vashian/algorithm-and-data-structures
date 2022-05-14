alice = list(map(int, input().split()))
bob = list(map(int, input().split()))

alice_score = 0
bob_score = 0

for i in range(len(alice)):

    if alice[i] > bob[i]:
        alice_score += 1

    elif alice[i] < bob[i]:
        bob_score += 1

print(alice_score, bob_score)
