# Write a Python program that finds the longest common substring between two strings.


def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    result = 0
    end = 0
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j ==0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > result:
                    result = dp[i][j]
                    end = i-1
            else:
              dp[i][j] == 0
    return str1[end-result+1:end+1]




str1 = "ABABC"
str2 = "BABCA"
output = longest_common_substring(str1,str2)

print(output)