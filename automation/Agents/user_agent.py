from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low


AGENT_MAILBOX_KEY="50c0b50c-b64f-4acf-8cf5-d1da0d3b3a28"

# Define the uagents agent
user_agent = Agent(name="User Agemt", seed="user-agent-seed-phrase", mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai")
fund_agent_if_low(user_agent.wallet.address())

class TwitterAgentRequest(Model):
    query: str

class TwitterAgentResponse(Model):
    response: str


TWITTER_AGENT_ADDRESS="agent1qda23laeg2dadjthgl6ukrtrg3mt9nh448uazm52a0dkuergcdc7jedlmxe"

@user_agent.on_event("startup")
async def fetch_tweets_handler(ctx: Context):
        ctx.logger.info(user_agent.address)
        await ctx.send(TWITTER_AGENT_ADDRESS, TwitterAgentRequest(query="Vaccine"))

@user_agent.on_message(model=TwitterAgentResponse)
async def handle_request(ctx: Context, sender: str, msg: TwitterAgentResponse):
    ctx.logger.info(msg.response)


# Run the agent
if __name__ == "__main__":
    user_agent.run()