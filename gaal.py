

def multiply(a, b):
    if(len(a[0]) != len(b)):
        return False
    result = []
    for i in range(len(a)):
        current = []
        result.append(current)
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(a[0])):
                sum += a[i][k] * b[k][j]
            current.append(sum)
    return result

def operate_constant(a, b, operation):
    result = []
    for i in range(len(a)):
        current = []
        result.append(current)
        for j in range(len(a[i])):
            current.append(operation(a[i][j], b))
    return result

def multiply_constant(a, b):
    return operate_constant(a, b,lambda a, b: a * b)

def divide_constant(a, b):
    return operate_constant(a, b,lambda a, b: a / b)

def transpose(vec):
    result = []
    for i in range(len(vec[0])):
        current = []
        result.append(current)
        for j in range(len(vec)):
            current.append(vec[j][i])
    return result

#square
def trace(vec):
    if(len(vec) != len(vec[0])):
        return False
    result = 0
    for i in range(len(vec)):
        result += vec[i][i]
    return result

def create_identity(width):
    identity = [[0 for i in range(width)] for j in range(width)]
    for i in range(width):
        identity[i][i] = 1
    return identity

def is_reverse(a, b):
    if(len(a) != len(a[0])):
        return False

    if(len(a) != len(b)):
        return False

    if(len(a[0]) != len(b[0])):
        return False

    identity = create_identity(len(a))
    
    if(multiply(a, b) != identity):
        return False
    
    if(multiply(b, a) != identity):
        return False

    return True

import math
def solve_reverse_matrix(input):
    def normalize(value, line):
        for i in range(len(line)):
            line[i] /= value

    def nullify(value, source, target):
        for i in range(len(source)):
            target[i] -= source[i] * value

    i = 0
    done_lines = []
    while(i < len(input[0])):
        min_zeros = math.inf
        min_line = 0
        for j in range(len(input)):
            for k in range(i, int(len(input[j]) / 2)):
                if(input[j][k] != 0):
                    break
            if(k < min_zeros and j not in done_lines):
                min_zeros = k
                min_line = j
        
        done_lines.append(min_line)

        i = min_zeros
        if(min_zeros == math.inf): break
        if(input[min_line][i] == 0):
            continue
        normalize(input[min_line][i], input[min_line])
        for j in range(len(input)):
            if(j != min_line):
                nullify(input[j][i], input[min_line], input[j])
        i += 1

import copy
def find_reverse(input):
    if(len(input) != len(input[0])):
        return False
    matrix = copy.deepcopy(input)
    identity = create_identity(len(matrix))

    for i in range(len(matrix)):
        matrix[i] += identity[i]

    solve_reverse_matrix(matrix)

    output = []
    for i in range(len(matrix)):
        output.append(matrix[i][len(matrix)::])

    if(not is_reverse(input, output)):
        return False
    
    return output
    