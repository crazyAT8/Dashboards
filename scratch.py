import ast
import operator

def solve(text_equation: str) -> str:
    allowed_operators = {
        ast.Add: operator.add, ast.Sub: operator.sub, 
        ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.Pow: operator.pow, ast.USub: operator.neg
    }

    def eval_expr(expr):
        node = ast.parse(expr, mode='eval').body
        return eval_node(node)

    def eval_node(node):
        if isinstance(node, ast.Num): 
            return node.n
        elif isinstance(node, ast.BinOp): 
            return allowed_operators[type(node.op)](eval_node(node.left), eval_node(node.right))
        elif isinstance(node, ast.UnaryOp):  
            return allowed_operators[type(node.op)](eval_node(node.operand))
        else:
            raise TypeError(node)

    result = eval_expr(text_equation)
    return str(float(result))  

print(solve("12 - 4*3"))  
print(solve("3 * 2 - 4 * 2/ 3 - 0"))  
print(solve("4"))  
print(solve("1 + 1"))  
print(solve("2 * 2 * 2 * 2 * 2"))  
print(solve("2 * 2 / 0 - 2"))  


