from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("My First Tool Server")

@mcp.tool()
def say_hello(name: str) -> str:
    """
    Greets the user by name.
    
    Args:
        name: The name of the user to greet.
    """
    return f"Hello, {name}! This comes from your custom MCP tool."

if __name__ == "__main__":
    mcp.run()
