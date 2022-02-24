def rev_word(sent):
    return  " ".join(sent.split()[:: -1])


sent_ip = 'python reverse word'
print(rev_word(sent_ip))
