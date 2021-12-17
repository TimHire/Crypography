import strings


cipher_text = "Wklv lv d whvw wr vhh zkhwkhu pb vlpxodwhg dqqhdolqj surjudp fdq vxffhvvixoob ghfubsw wklv vlpsoh flskhuwhaw. Lw zloo eh hvshfldoob lqwhuhvwlqj wr vhh zkhwkhu frpsolfdwhg zrugv vxfk dv cheud dqg txlgglwfk zloo eh surshuob ghfubswhg, dv wkhvh frqwdlq ohwwhuv zklfk duh qrw riwhq xvhg lq wkh Hqjolvk doskdehw."
alphabet = dict(zip(range(1, 27), string.ascii_uppercase))

def prepare(cipher):
    cipher = cipher.upper()
    cipher = cipher.replace(" ", "").replace(".", "").replace(",", "").replace("!", "").replace("?", "")
    return cipher

def swap(data, a, b):
    position_a = []
    position_b = []
    for l in range(len(data)):
        if data[l] == a:
            position_a.append(l)
        if data[l] == b:
            position_b.append(l)
    data_string = list(data)
    for g in position_a:
        data_string[g] = str(b)
    for h in position_b:
        data_string[h] = str(a)
    return "".join(data_string)


def ceaser(cipher):
