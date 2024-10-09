import sys

def ValidLisp(code):
    stack = []
    open = ["[", "(", "{"]
    closed = ["]", ")", "}"]
    match = {"[" : "]", "(" : ")", "{" : "}"}
    for i, c in enumerate(symbols):
        if c in open:
            stack.append(c)
        elif c in closed:
            if not stack or match[stack.pop()] != c:
                return f'{c} {i}'
    return "ok so far"

if __name__ == "__main__":
    inp = sys.stdin.readline().strip("\n").split(" ")
    L = int(inp[0])
    symbols = sys.stdin.readline().strip("\n")
    print(ValidLisp(symbols))
