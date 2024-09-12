from python.helpers.tool import Tool, Response
from python.helpers.perplex_scraper import Perplex
from python.helpers.url_scraper import fetch_page_content

class WebpageContentTool(Tool):
    async def execute(self, **kwargs):
        try:
            target_url = kwargs.get('url')
            search_queries = kwargs.get('queries')

            if not target_url or not search_queries:
                return self.create_error_response("Missing URL or search queries.")

            page_content = await fetch_page_content(url=target_url, max_retries=2, headless=False)
            
            if page_content.startswith("ERROR:"):
                return self.create_error_response(f"Failed to fetch page content: {page_content}")

            perplex = Perplex(agent=self.agent)
            processed_content = await perplex.scraper(queries=search_queries, content=page_content)

            formatted_content = self.agent.read_prompt("tool.webpage.response.md", scraped_data=processed_content)
            return Response(message=formatted_content, break_loop=False)

        except Exception as e:
            return self.create_error_response(f"An error occurred: {str(e)}")

    def create_error_response(self, error_message):
        formatted_error = self.agent.read_prompt("fw.error.md", error=error_message)
        return Response(message=formatted_error, break_loop=False)