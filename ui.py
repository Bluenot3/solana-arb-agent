# ui.py

import asyncio
import streamlit as st
from arbitrage import SolanaArbitrageBot
from config import ARBITRAGE_THRESHOLD, TRADE_AMOUNT

# Create global references
bot_instance = None
bot_task = None

st.title("Solana Arbitrage Bot")
st.markdown("A simple UI to start/stop the bot and adjust settings.")

# Display & adjust threshold
threshold = st.number_input("Arbitrage Threshold (%)", min_value=0.0, value=ARBITRAGE_THRESHOLD * 100.0)
trade_amount = st.number_input("Trade Amount", min_value=0.0, value=TRADE_AMOUNT)

start_button = st.button("Start Bot")
stop_button = st.button("Stop Bot")

if start_button and not bot_instance:
    # Update config values for current session
    bot_instance = SolanaArbitrageBot()
    st.write("Starting arbitrage bot...")

    # Launch the bot in an async loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    bot_task = loop.create_task(bot_instance.run_bot())

    # We run the loop in a Streamlit-compatible way
    st.write("Bot is running. Check the console/logs for details.")

if stop_button and bot_instance:
    bot_instance.stop_bot()
    bot_instance = None
    st.write("Bot stopped.")
