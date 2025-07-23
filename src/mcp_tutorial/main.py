from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name='mcp-tutorial' , stateless_http=True)

mcp_app = mcp.streamable_http_app()
