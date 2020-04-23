import string
def decode(message):
    dp = [0 for _ in range(len(message)+1)]
    dp[0] = 1;
    dp[1] = 0 if int(message[0]) == 0 else 1

    for n in range(2,len(message)+1):
        one = int(message[n-1 :n])
        two = int(message[n-2 :n])

        if one >=1:
          dp[n] += dp[n-1]
        if two >=10 and two <=26:
          dp[n] += dp[n-2]

    print dp[len(message)]

decode('226')
