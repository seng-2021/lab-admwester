import codecs


digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))

def encode(s):
    originlen = len(s)
    if not isinstance(s,str):
        raise TypeError
    elif originlen > 1000:
        raise ValueError
    

    encrypted = ""
    for i in range(1000):
        if i < originlen:
            c = s[i]
        else:
            c = "a"
        if c in "+åäöÅÄÖ":
            raise ValueError
        elif c.isalpha():
            # Rot13 the character for maximum security
            encrypted += codecs.encode(c,'rot13')
        elif c in digitmapping:
            encrypted += digitmapping[c]
        else:
            raise ValueError
        
    return encrypted[:originlen].upper()


def decode(s):
    originlen = len(s)
    if not isinstance(s,str):
        raise TypeError
    elif originlen > 1000:
        raise ValueError
    
    decrypted = ""
    for i in range(1000):
        if i < originlen:
            c = s[i]
        else:
            c = "a"
        if c in "+åäöÅÄÖ":
            raise ValueError
        elif c.isalpha():
            # Rot13 the character for maximum security
            decrypted += codecs.encode(c,'rot13')
        elif c in digitmapping:
            decrypted += digitmapping[c]
        else:
            raise ValueError

    return decrypted[:originlen].lower()


