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

To add the above server to an MCP host like Gemini CLI, you would use the following configuration
in `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    {
        "Math-calculator": {
            "timeout": 60, # fail if no response in 60 seconds
            "command": "/path/to/python",
            "args": ["/path/to/server.py"],
            "transportType": "stdio"
        }
    }
  }
}
```

## How to debug MCP servers locally

You can debug MCP server using @modelcontextprotocol/inspector:

1. Install the inspector globally using npm:

   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Start the inspector:

   ```bash
   mcp dev /path/to/your/mcp-server.py
   ```

3. Open your web browser and navigate to the url provied by the above
   command.

4. Click 'Connect' to start debugging your MCP server, followed by
   clicking `Tools` tab at the top, and then select the tool you want
   to test. Then input the required arguments and click 'Run Tool' to
   see the output.

5. To allow to connect to MCP server from a remote machine (default is from local machine only), then you
   need specify some environment variables before starting the MCP server.
   For example, you need specify `HOST` and `ALLOWED_ORIGINS`
   environment variables as follows, where server-ip address is where
   the server is running:

   ```bash
   HOST=0.0.0.0 ALLOWED_ORIGINS=http://server-ip-address:6274 mcp dev math-calc/server.py
   ```

   You can also change the port number by using `CLIENT_PORT`
   environment variable if you like. Check https://github.com/modelcontextprotocol/inspector?tab=readme-ov-file#from-an-mcp-server-repository

You can find more about MCP inspector at [github](https://github.com/modelcontextprotocol/inspector) and 
[here](https://modelcontextprotocol.io/docs/tools/inspector).

You may also want to check
[mcp-cli](https://github.com/chrishayuk/mcp-cli) which allows to run
MCP servers from command line for testing purpose.

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
