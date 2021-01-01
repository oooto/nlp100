org_str1 = "パトカー"
org_str2 = "タクシー"
alt_list = [str1 + str2 for str1, str2 in zip(org_str1, org_str2)]
ans_str = "".join(alt_list)
print(ans_str)