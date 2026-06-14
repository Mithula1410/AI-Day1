import asyncio
import os
from dotenv import load_dotenv
from supabase import acreate_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

async def main():
    supabase = await acreate_client(SUPABASE_URL, SUPABASE_KEY)

    def handle_insert(payload):
        email = payload["data"]["record"]["email"]
        print(f"New user added: {email}")

    channel = (
        supabase
        .channel("users-changes")
        .on_postgres_changes(
            event="INSERT",
            schema="public",
            table="users",
            callback=handle_insert
        )
    )

    await channel.subscribe()

    print("Listening for new users...")

    while True:
        await asyncio.sleep(1)

asyncio.run(main())