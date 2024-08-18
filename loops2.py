packing_list = ["passport","tickets","camera","clothes"]
packed_items = ["passport","camera","clothes"]

for item in packing_list:
    if item not in packed_items:
        print(f"You forgot to pack {item}")
        break