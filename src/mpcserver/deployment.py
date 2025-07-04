from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")

@mcp.tool()
def add_two_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b