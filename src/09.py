# --- Day 9: Disk Fragmenter ---

from sys import argv

with open(argv[1]) as file:
    diskmap = list(map(int, file.read().strip()))

disk, data, freespace, head = [], [], [], 0

for i, n in enumerate(diskmap):
    disk += [None if (odd := i & 1) else (data_id := i >> 1)] * n
    if odd:
        freespace += [(head, n)]
    else:
        data += [(data_id, head, n)]
    head += n

disk_copy = [*disk]  # to calculate n2, after n1

head = diskmap[0]
while head < len(disk_copy):
    if disk_copy[head]:
        head += 1
    elif data_id := disk_copy.pop():
        disk_copy[head] = data_id

n1 = sum(i * data_id for i, data_id in enumerate(disk_copy))

for data_id, di, dn in data[::-1]:
    for i, (fi, fn) in enumerate(freespace):
        if has_free_space := fi <= di and dn <= fn:
            if fn == dn:
                freespace.pop(i)
            else:
                freespace[i] = (fi + dn, fn - dn)
            break
    if has_free_space:
        disk[di:di + dn] = [None] * dn
        disk[fi:fi + dn] = [data_id] * dn

n2 = sum(i * data_id for i, data_id in enumerate(disk) if data_id)

print(n1, n2)
