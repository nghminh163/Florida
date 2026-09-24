import lief, sys, random

input_file = sys.argv[1]
print(f"[*] anti-anti-frida patch: {input_file}")
rnd = "".join(random.sample("ABCDEFGHIJKLMNO", 5))
b = lief.parse(input_file)
if b:
    for s in b.symbols:
        if s.name == "frida_agent_main":
            s.name = "main"
        if "frida" in s.name:
            s.name = s.name.replace("frida", rnd)
        if "FRIDA" in s.name:
            s.name = s.name.replace("FRIDA", rnd)
    b.write(input_file)
    print("[*] symbols scrubbed with", rnd)
else:
    print("[!] lief parse failed")
