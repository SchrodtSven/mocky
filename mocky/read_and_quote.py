with open('data/meta_syntactic_vars.txt', 'r') as fr:
    foo_lines = fr.readlines()
foo_lines.sort()
bar = []
for x in foo_lines:
    x = x.strip()
    bar.append(f"'{x}'")
print(', '.join(bar))