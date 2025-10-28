from fastmcp import FastMCP

mcp = FastMCP(name="Calculator")

@mcp.tool()
def multiply(a:float, b:float) -> float :
    """
    Multiply two numbers.

    args: a(float): The First number.
          b(float): The second number 
    returns : float: The preoduct of the two numbers
    """
    return a * b

@mcp.tool(
    name = "add",
    description = "Add two numbers together.",
    tags = ["arithmetic", "addition"],
)
def add_numbers(x:float, y:float) -> float:
    """
    Add two numbers together.

    args: x(float): The first number.
          y(float): The second number.
    returns: float: The sum of the two numbers.
    """
    return x + y

@mcp.tool()
def subtract(x:float, y:float) -> float:
    """
    Subtract one number from another.

    args: x(float): The number to be subtracted from.
          y(float): The number to subtract.
    returns: float: The result of the subtraction.
    """
    return x - y

@mcp.tool()
def divide(x:float, y:float) -> float:
    """
    Divide one number by another.

    args: x(float): The dividend.
          y(float): The divisor.
    returns: float: The quotient of the division.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

if __name__ == "__main__":
    mcp.run(transport="http", host="localhost", port=8002) #HTTP Transport