def make_out_word(out, word):
  if len(out)==4:
    return out[0]+out[1]+word+out[2]+out[3]
print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('[[]]', 'word'))
