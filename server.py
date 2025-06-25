from fastmcp import FastMCP, Context
import httpx
from typing import Dict, Any, Annotated
from pydantic import BaseModel
import os

mcp = FastMCP("Opet MCP Server")

OPET_API_URL = os.getenv("OPET_API_URL", "http://localhost:5050")

class ErrorResponse(BaseModel):
    error: str
    details: str | None = None

@mcp.tool()
async def get_all_provinces(ctx: Context) -> Dict[str, Any]:
    """Retrieves all provinces."""
    await ctx.info("Getting all provinces")
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{OPET_API_URL}/fuel/provinces")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return ErrorResponse(
                error="Failed to fetch provinces",
                details=str(e)
            ).model_dump()

@mcp.tool()
async def get_fuel_prices_by_province(
    province_id: Annotated[
        str,
        "The unique identifier of the province to fetch fuel prices for. This should be a valid province ID from the get_all_provinces() response."
    ], ctx: Context
) -> Dict[str, Any]:
    """Retrieves fuel prices for a specific province."""
    await ctx.info(f"Getting fuel prices for province {province_id}")
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{OPET_API_URL}/fuel/prices/{str(province_id)}")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return ErrorResponse(
                error=f"Failed to fetch fuel prices for province {province_id}",
                details=str(e)
            ).model_dump()

@mcp.tool()
async def get_last_update_time(ctx: Context) -> Dict[str, Any]:
    """Retrieves the last update timestamp."""
    await ctx.info("Getting last update time")
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{OPET_API_URL}/fuel/last-update")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return ErrorResponse(
                error="Failed to fetch last update time",
                details=str(e)
            ).model_dump()

if __name__ == "__main__":
    mcp.run()