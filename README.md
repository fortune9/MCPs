# Custom MCP Servers Collection

Welcome to this repository! This collection serves as a hub for sharing Model Context Protocol (MCP) servers that I have developed. The goal is to provide useful tools and extensions that can be easily integrated with MCP-compliant clients like Claude Desktop.

## MCP

The Model Context Protocol (MCP) is a protocol designed to facilitate
communication between clients and servers that provide AI model
functionalities. MCP servers can offer various tools and services that
enhance the capabilities of AI models.

### MCP Hosts

MCP hosts are software applications that implement the MCP protocol,
allowing users to connect to MCP servers. They provide an interface
for users to interact with the tools and services offered by the
    servers.

- [Claude Desktop](https://claude.ai/desktop) - A popular MCP client
  for interacting with various MCP servers.

- [Cline](https://cline.bot/) - Another MCP client that supports multiple servers
  and provides a user-friendly interface.

### MCP server

MCP servers are applications that implement the MCP protocol to
provide specific functionalities or tools. These servers can be
accessed by MCP hosts to enhance the capabilities of AI models.

### MCP tools

MCP tools are specific functionalities or services provided by MCP
servers. These tools can range from simple utilities to complex
applications that enhance the user experience when interacting with
AI models.

### An example of MCP server to calculate math expressions

```python
import sympy as sp
from mcp.server.fastmcp import FastMCP

# create an MCP server instance
server = FastMCP("math-calculator")

# register a tool to calculate mathematical expressions
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
# run the MCP server
    server.run()
```


## Available Servers

| Server Name | Description | Link |
| :--- | :--- | :--- |
| **My Tools** | A starter MCP server providing basic utility tools (e.g., greetings). | [View Code](./my-tools) |


## Author

**Zhenguo Zhang**

## Contributing

Contributions are welcome! If you have ideas for new tools, improvements to existing servers, or bug fixes, please feel free to open an issue or submit a pull request.

### Code of Conduct

We are committed to providing a friendly, safe, and welcoming environment for all, regardless of gender, sexual orientation, disability, ethnicity, religion, or similar personal characteristic. Please be kind and respectful in all interactions.
