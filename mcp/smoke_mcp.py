"""End-to-end SDK client: handshake, discovery, calls and tool errors over stdio."""
import asyncio
import json
from pathlib import Path
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params=StdioServerParameters(command=sys.executable,args=[str(Path(__file__).with_name('server.py'))])
    async with stdio_client(params) as (read,write):
        async with ClientSession(read,write) as client:
            await client.initialize()
            tools=await client.list_tools()
            assert len(tools.tools)==4
            for name,args in [('search_evidence',{'query':'seguimiento'}),('get_source',{'source_id':'S5'}),
                              ('check_comparability',{'source_a':'S1','source_b':'S4'}),
                              ('get_hypothesis',{'hypothesis_id':'H3'})]:
                r=await client.call_tool(name,args)
                assert not r.isError,(name,r)
                payload=r.structuredContent or json.loads(r.content[0].text)
                if name=='check_comparability': assert payload['status']=='incompatible'
                print('PASS',name)
            rejected=await client.call_tool('get_source',{'source_id':'S1','project_id':'other-client'})
            assert rejected.isError
            print('PASS unauthorized project rejected over MCP')

if __name__=='__main__': asyncio.run(main())
