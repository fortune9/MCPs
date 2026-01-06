# My Tools MCP Server

This is a Model Context Protocol (MCP) server providing custom tools.

## Prerequisites

- Python 3.10 or higher
- `pip`

## Setup

1.  **Clone the repository or navigate to the project directory:**
    ```bash
    cd my-tools
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    *   **Windows:**
        ```powershell
        .\venv\Scripts\Activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

To start the MCP server, run the following command:

```bash
python server.py
```

## Configuration

### Claude Desktop

To use this server with Claude Desktop, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "my-tools": {
      "command": "/absolute/path/to/my-tools/venv/bin/python",
      "args": ["/absolute/path/to/my-tools/server.py"]
    }
  }
}
```

Replace `/absolute/path/to/my-tools` with the full path to this directory.
