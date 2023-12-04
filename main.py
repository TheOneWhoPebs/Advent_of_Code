total = 0
numbers = ['1','2','3','4','5','6','7','8','9']
with open('input.txt') as f:
    for line in f:
        current_line = []
        line_num = ''
        line = line.strip()
        for char in line:
            if char in numbers:
                current_line.append(char)
        line_num = current_line[0] + current_line[-1]
        total += int(line_num)       

print(total)