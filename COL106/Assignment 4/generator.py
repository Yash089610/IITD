import a4
import random
l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# l = ['A', 'C', 'G', 'T']
# l = ['A']


def prime_till_n(N):
    lp = [0]*(N+1)
    pr = []

    for i in range(2, N+1):
        if (lp[i] == 0):
            lp[i] = i
            pr.append(i)
        for j in range(0, len(pr)):
            if pr[j] <= lp[i] and i * pr[j] <= N:
                lp[i * pr[j]] = pr[j]
    return pr


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*M
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            kmp.append(i-j)
            j = lps[j-1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


t = 10**5
eps = 0.1
po = 2
qwe = prime_till_n(a4.findN(eps, po+1))
print(a4.findN(eps, po+1), len(qwe))


for i in range(10):
    m = str()
    x = str()
    for i in range(t):
        m += random.choice(l)

    for i in range(po):
        x += random.choice(l)
    x += '?'
    # x = random.choices(m, k=random.randint(5, 100))
    kmp = []
    print(x)
    # Python program for KMP Algorithm

    for i in l:
        KMPSearch(x[:-1]+i, m)

    k = 0
    for i in qwe:
        out = a4.modPatternMatchWildcard(i, x, m)
        out = set(out)
        kmp = set(kmp)

        if (kmp.issubset(out)):
            if (len(out)-len(kmp) > 0):
                k += 1
                # w = out.intersection(kmp)
                # q = (1-(len(kmp)/len(out)))
                # print("Tolerance ", eps, " Got ", q, len(
                #     kmp), len(out), len(out)-len(kmp))
        else:
            print("Answer didnt match")

    print(k/len(qwe), len(kmp))
