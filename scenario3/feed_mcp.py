from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name="FreeCodeCamp News Feed Searcher")

@mcp.tool()
def fcc_news_search(query: str, max_results: int = 5) -> list:
    """
    Search FreeCodeCamp news feed for articles matching the query.

    args: query(str): The search term to look for in the news feed.
          max_results(int): The maximum number of results to return. Default is 5.
    returns: list: A list of dictionaries containing the title and link of matching articles.
    """
    feed_url = "https://www.freecodecamp.org/news/rss/"
    feed = feedparser.parse(feed_url)
    
    results = []
    for entry in feed.entries:
        if query.lower() in entry.title.lower() or query.lower() in entry.summary.lower():
            results.append({
                "title": entry.title,
                "link": entry.link
            })
        if len(results) >= max_results:
            break
    
    return results

@mcp.tool()
def fcc_youtube_search(query: str, max_results: int = 5) -> list:
    """
    Search FreeCodeCamp YouTube channel for videos matching the query.

    args: query(str): The search term to look for in the YouTube channel.
          max_results(int): The maximum number of results to return. Default is 5.
    returns: list: A list of dictionaries containing the title and link of matching videos.
    """
    feed_url = "https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ"
    feed = feedparser.parse(feed_url)
    
    results = []
    for entry in feed.entries:
        if query.lower() in entry.title.lower() or query.lower() in entry.summary.lower():
            results.append({
                "title": entry.title,
                "link": entry.link
            })
        if len(results) >= max_results:
            break
    
    return results

if __name__ == "__main__":
    mcp.run()
