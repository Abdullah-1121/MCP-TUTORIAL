from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name='mcp-tutorial' , stateless_http=True)

# Creating a Dummy Tool
@mcp.tool()
def search_web(query: str) -> str:
    return f'https://www.google.com/search?q={query}'

@mcp.tool()
def get_weather(city: str) -> str:
    return f'The weather in {city} is sunny.'
mcp_app = mcp.streamable_http_app()
