with open("invitees.txt", "r") as ins:
...     source_lines = []
...     for line in ins:
...         source_lines.append(line)

...for source_line in source_lines:
...    if ";" in source_line:
...       filtered_lines.append(source_line)

with open('flat_invitees.txt', 'w') as file:
...     for filtered_line in filtered_lines:
...         split_reg = filtered_line.split(';')
...         for regs in split_reg:
...            file.write("\n" + regs)