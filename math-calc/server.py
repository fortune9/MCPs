# math_mcp_server.py
import sympy as sp
from mcp.server.fastmcp import FastMCP

server = FastMCP("math-calculator")

@server.tool()
def calculate(expression: str) -> str:
    """Evaluates mathematical expressions.

    Args:
        expression (str): A mathematical expression as a string.
    Returns:
        str: The result of the evaluation or an error message.
    """
    try:
        expr = sp.sympify(expression)
        return str(sp.N(expr))
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    server.run()
