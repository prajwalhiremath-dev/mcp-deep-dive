#HTTP
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
#1.Let's make a FastAPI app (that means API) first

app = FastAPI(title="Calculator API")

@app.post("/multiply")
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    args: a(float): The First number.
          b(float): The second number 
    returns : float: The product of the two numbers
    """
    result = a * b
    return {"result": result}
@app.post("/add")
def add_numbers(x: float, y: float) -> float:
    """
    Add two numbers together.

    args: x(float): The first number.
          y(float): The second number.
    returns: float: The sum of the two numbers.
    """
    result = x + y
    return {"result": result}
@app.post("/subtract")
def subtract(x: float, y: float) -> float:
    """
    Subtract one number from another.

    args: x(float): The number to be subtracted from.
          y(float): The number to subtract.
    returns: float: The result of the subtraction.
    """
    result = x - y
    return {"result": result}
@app.post("/divide")
def divide(x: float, y: float) -> float:
    """
    Divide one number by another.

    args: x(float): The dividend.
          y(float): The divisor.
    returns: float: The quotient of the division.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    result = x / y
    return {"result": result}

# 2. Converting to MCP
mcp = FastApiMCP(app, name="CalculatorAPI")
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8085)