def PrintMatrix(A:list):
	if A == None:
		print(A, end="\n\n")
		return
	rows = len(A)
	cols = len(A[0])
	for i in range(rows):
		for j in range(cols):
			print(f"{A[i][j]:.2f}", end = " ")
		print()
	print()

def CheckMatrix(A:list):
    if len(A)!=0: t=len(A[0])
    else: return False
    for i in A:
        if len(i)==t and len(i)!=0:
            for j in i:
                if not isinstance(j,float):
                    return False
        else: return False
    else: return True

def Transpose(A:list):
    if CheckMatrix(A):
        tran=[[0.00 for _ in range(len(A))] for _ in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[i])):
                tran[j][i]=A[i][j]
        return tran
    else: return None
    
def Multiplication(A:list,B:list):
    if CheckMatrix(A) and CheckMatrix(B) and len(A[0])==len(B):
        mult=[[0.00 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    mult[i][j]+=A[i][k]*B[k][j]
        return mult
    else: return None

def Addition(A:list,B:list):
    if CheckMatrix(A) and CheckMatrix(B) and len(A)==len(B) and len(A[0])==len(B[0]):
        addi=[[0.00 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[i])):
                addi[i][j]=A[i][j]+B[i][j]
        return addi       
    else: return None

def Symmetric(A:list):
    if CheckMatrix(A) and len(A)==len(Transpose(A)):
        if A==Transpose(A):
            return True
        else:
            return False
    else: return False