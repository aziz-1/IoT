import requests
from typing import List
from uagents import Agent, Context, Model

# Define the uagents agent
agent_info = Agent(name="TwitterAgentV2", seed="secret_aziz", port=8000, endpoint=["http://localhost:8000/submit"])


class TwitterAgentRequest(Model):
    query: str

class TwitterAgentResponse(Model):
    response: str
    

# function for handling Twitter API interactions

async def fetch_tweets_v2(query, max_results):
    print("Inside fetch tweets")
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAGuPxAEAAAAAizYDTEEku0oODRlyaNMJKbxXD80%3DVb19perxOkw90J1Y5w8z0VVI9Qxiqz1jAYSaEy8P72Pxrk1HeO"
    base_url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "text,lang",  # Ensure text is fetched
    }

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        tweets = response.json().get("data", [])
        tweets_string = "\n".join([tweet["text"] for tweet in tweets if "text" in tweet])

        # Extract text from tweets, ensuring language is English
        return tweets_string
        
    except Exception as e:
        print(f"Error fetching tweets using v2 endpoint: {e}")
        return "error"

# Twitter API Bearer Token
# twitter_agent = TwitterAgentV2(BEARER_TOKEN)

# Integrate the Twitter functionality into the uagents context
@agent_info.on_event("startup")
async def fetch_tweets_handler(ctx: Context):
        ctx.logger.info(f"Address: {agent_info.address}")




# @agent_info.on_message(model=TwitterAgentRequest, replies=TwitterAgentResponse)
# async def handle_request(ctx: Context, sender: str, msg: TwitterAgentRequest):

#     ctx.logger.info(f"Received query: {msg.query}")
#     tweets = await fetch_tweets_v2(msg.query, 10)
    
#     # for tweet in tweets:
#     #     print(f"Tweet: {tweet}")
#     #     print("-" * 80)
    
#     await ctx.send(
#         sender, TwitterAgentResponse(response=tweets)
#     )


# Run the agent
if __name__ == "__main__":
    agent_info.run()

