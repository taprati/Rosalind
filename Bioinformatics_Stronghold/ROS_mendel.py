#
# Mendel's First Law
#

homo_D = 2 #k
Hetero = 2 #m
homo_R = 2 #n

N = homo_D + Hetero + homo_R

prob_DD = (homo_D / N) * (homo_D-1) / (N-1)

prob_HH = (Hetero / N) * (Hetero-1) / (N-1) * 3/4

prob_DH = (homo_D / N) * (Hetero / (N-1)) + (Hetero / N) * (homo_D / (N-1))

total_prob = prob_DD + prob_HH + prob_DH
print(total_prob)

