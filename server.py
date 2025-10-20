import json
from fastmcp import FastMCP
from opet.api import OpetApiClient


mcp = FastMCP(name="Opet MCP")
opet_client = OpetApiClient()

@mcp.tool()
def get_provinces():
    """
    Returns the province of the cities.
    :return:
    """
    try:
        with open("provinces.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "File 'provinces.json' not found."}
    except json.JSONDecodeError:
        return {"error": "Error decoding JSON content from 'provinces.json'."}


@mcp.tool()
def get_fuel_price(province_code: str):
    """
    Function to retrieve the fuel price for a specified province using its code.

    The function takes the province code as input and fetches the price using an
    external client. If any exception occurs during the process, it returns the
    error message within a dictionary.

    Args:
        province_code (str): Code of the province for which the fuel price
        needs to be retrieved.

    Returns:
        dict: A dictionary containing either the fuel price or an error message
        in case of an exception.
    """
    try:
        return opet_client.price(province_code)
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run()