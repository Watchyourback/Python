seq1=['happy','chinese','new','year']
join_seq=' '
print join_seq.join(seq1)
print '-'.join(seq1)

seq2='happy chinese new year'
print ','.join(seq2)

seq3=('happy','chinese','new','year')
print ':'.join(seq3)

seq4={'happy':1,'chinese':2,'new':3,'year':4}
print ' '.join(seq4)