file1 = open(r"solution.txt")
file2 = open(r"submission.txt")

line1 = file1.readline()
line2 = file2.readline()

solutionF = file1.read()
solutionF = solutionF.replace(","," ")
solutionF = solutionF.split("\n")

submissionF = file2.read()
submissionF = submissionF.replace(","," ")
submissionF = submissionF.split("\n")

TableQ = []
j = 0
D_num = 0
P_rate = 0
AP_total = 0



for i in range(len(solutionF)-1):
	A = solutionF[i]
	A = A.split()
	B = submissionF[j]
	B = B.split()
	for k in range(len(A)-1):
		TableQ.append(B.index(A[k+1]))
		TableQ.sort()
	for m in range(len(TableQ)):
			D_num +=1
			P_rate += ((D_num / TableQ[m]))
	AP = P_rate / D_num 
	print("No.",i+1,"Query_AP = ",AP)
	AP_total += AP
	j += 1
	del TableQ[:]
	D_num = 0
	AP = 0
	P_rate = 0

print("\nMAP = ",AP_total/16)
