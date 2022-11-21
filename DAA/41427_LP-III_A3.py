def knapSack(K_C, weight, val, n):
	K = [[0 for x in range(K_C + 1)] for x in range(n + 1)]
	for i in range(n + 1):
		for w in range(K_C + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif weight[i-1] <= w:
				K[i][w] = max(val[i-1] + K[i-1][w-weight[i-1]], K[i-1][w])
			else:
				K[i][w] = K[i-1][w]
	return K[n][K_C]


val = [40,50,100,95,30]
weight = [2,5,6,5,3]
K_C = 10
n = len(val)
print("Maximum total value : ", knapSack(K_C, weight, val, n))
