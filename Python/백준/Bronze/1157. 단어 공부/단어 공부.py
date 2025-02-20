n = input().upper()  # Convert input to uppercase

cnt = [0] * 26  # Array to store frequency of each letter

# Counting occurrences of each letter
for char in n:
    if 'A' <= char <= 'Z':  # Ensuring it's an uppercase letter
        cnt[ord(char) - ord('A')] += 1  # Map 'A' to index 0, 'B' to 1, ..., 'Z' to 25

ma = max(cnt)  # Get the maximum frequency
ccnt = cnt.count(ma)  # Count how many letters have this max frequency

if ccnt > 1:
    print("?")
else:
    print(chr(cnt.index(ma) + ord('A')))  # Convert index back to the corresponding letter
