# OPET Fuel Prices MCP Server

A Model Context Protocol (MCP) server that provides access to OPET fuel prices data through Claude AI.

## Demo
![Example](example.gif)

## Features

- Get all available provinces
- Fetch fuel prices for specific provinces
- Get last update timestamp
- Error handling with detailed messages

## Installation

### Prerequisites

- Python 3.12 or higher
- uv package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd opet-mcp
```

2. Create a virtual environment and install dependencies:
```bash
uv venv -p 3.12
source .venv/bin/activate
uv add fastmcp
```

## Configuration

Set the OPET API URL using environment variables:

```bash
export OPET_API_URL=http://your-api-endpoint.com
```

## Usage

### Running the Server

Start the MCP server:

```bash
fastmcp run server.py
```

### Example Configuration

Install the server to Claude with a custom name and API URL:

```bash
{
  "mcpServers": {
    "Opet Server": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "fastmcp",
        "run",
        "/your_absolute_path/opet-mcp/server.py"
      ],
      "env": {
        "OPET_API_URL": "CHANGE_ME"
      }
    }
  }
}
```

### Example Installation Command

```bash
fastmcp install server.py --name "OPET Fuel Prices" \
  --env-var OPET_API_URL=http://localhost:5050
```

## Available Tools

### get_all_provinces()
Retrieves a list of all provinces where fuel prices are available.

### get_fuel_prices_by_province(province_id)
Fetches current fuel prices for a specific province using its ID.

**Parameters:**
- `province_id` (str): The unique identifier of the province

### get_last_update_time()
Gets the timestamp of when the fuel prices were last updated in the system.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 