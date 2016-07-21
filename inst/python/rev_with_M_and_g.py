def revcompl (s):
        rev_s = ''.join([{'M':'g', 'g':'M', 'A':'T','C':'G','G':'C','T':'A'}[B] for B in s][::-1])
        return rev_s
        
