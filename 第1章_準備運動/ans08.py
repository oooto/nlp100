def cipher(org_str):
    org_str = [chr(219 - ord(s)) if 97 <= ord(s) <= 122 else s for s in org_str]
    return "".join(org_str)

org_str = 'ParaParaParadise'
ans = cipher(org_str)
print(ans)
ans = cipher(ans)
print(ans)
