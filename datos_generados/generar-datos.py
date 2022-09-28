from random import randint
import random
import requests

def mac_generator():
        mac = [random.randint(0x00, 0xFF),
            random.randint(0x00, 0xFF),
            random.randint(0x00, 0xFF),
            random.randint(0x00, 0xFF),
            random.randint(0x00, 0xFF),
            random.randint(0x00, 0xFF)]
        new_mac = ':'.join(map(lambda x: "%02X" % x, mac))
        return new_mac

def generate_id():
    generations = [183,181,191,193,201,203,211,213,]
    rn_id = random.randint(0, 900)
    rn_choice = random.choice(generations)
    id = f"{rn_choice}{rn_id:03d}"
    return id

def mega_generator():
    consumo = randint(0, (1024*4))
    result = 0
    if consumo > 1024:
        result = str(round(consumo / 1024,2)) + " GB"
    else:
        result = str(round(consumo,2)) + " MB"
    return result


if __name__ == "__main__":
    with open("macs.txt", "w") as f:
        for i in range(100):
            f.write(mac_generator() + "\n")
    # with open("ids.txt", "w") as f:
    #     for i in range(100):
    #         f.write(generate_id() + "\n")
    
    # with open("consumo.txt", "w") as f:
    #     for i in range(100):
    #         f.write(mega_generator() + "\n")
    
    