# arbitrage.py

import time
import asyncio
import math
from solana.rpc.async_api import AsyncClient
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer

from config import (
    SOLANA_RPC_URL,
    MARKET_1_ADDRESS,
    MARKET_2_ADDRESS,
    WALLET_PRIVATE_KEY,
    ARBITRAGE_THRESHOLD,
    TRADE_AMOUNT
)

# You may need these libraries for Serum orderbook interactions
# pip install "serum-py>=0.4.0"
# from serum.async_connection import async_connection
# from serum.market import Market

class SolanaArbitrageBot:
    def __init__(self):
        # Convert the private key array to a Keypair
        self.wallet = Keypair.from_secret_key(bytes(WALLET_PRIVATE_KEY))
        self.client = AsyncClient(SOLANA_RPC_URL)

        # In a real scenario, you'd load Serum markets like this:
        # connection = await async_connection(SOLANA_RPC_URL)
        # self.market1 = await Market.load(connection, PublicKey(MARKET_1_ADDRESS))
        # self.market2 = await Market.load(connection, PublicKey(MARKET_2_ADDRESS))

        # For this example, we simulate prices
        self.simulated_price_market1 = 1.0
        self.simulated_price_market2 = 1.05

        self.running = False

    async def check_arbitrage_opportunity(self):
        """
        Check for a price difference between two markets.
        In a real scenario, you'd get the orderbook from each Serum market,
        derive the best bid/ask, and compare them.
        """
        # Simulate price changes
        self.simulated_price_market1 += (0.001 * (1 if math.sin(time.time()) > 0 else -1))
        self.simulated_price_market2 += (0.001 * (1 if math.cos(time.time()) > 0 else -1))

        price1 = self.simulated_price_market1
        price2 = self.simulated_price_market2

        # Find difference in percentage
        if price1 > 0:
            diff = ((price2 - price1) / price1) * 100
        else:
            diff = 0

        # Print info (for debugging)
        print(f"Market1 Price: {price1:.4f} | Market2 Price: {price2:.4f} | Diff: {diff:.2f}%")

        # If difference is greater than threshold, trade
        if abs(diff) >= ARBITRAGE_THRESHOLD * 100:
            if diff > 0:
                print("Buy from Market1, Sell on Market2")
                # Place buy on Market1, then sell on Market2
                await self.execute_trade("BUY_M1_SELL_M2")
            else:
                print("Buy from Market2, Sell on Market1")
                # Place buy on Market2, then sell on Market1
                await self.execute_trade("BUY_M2_SELL_M1")

    async def execute_trade(self, trade_direction):
        """
        Placeholder for actual trade logic on Serum. 
        We'll just print the trade direction & assume success.
        In a real scenario, you'd:
        1) Place a buy order on the cheaper market.
        2) Wait for fill confirmation.
        3) Place a sell order on the more expensive market.
        """

        # Example of a Solana transfer transaction (not an actual Serum trade):
        # In real arbitrage, you'd sign and send a Serum dex instruction, not just transfer SOL.
        recipient = self.wallet.public_key  # In real use, might be the DEX program or your own account.
        transfer_tx = Transaction().add(
            transfer(
                TransferParams(
                    from_pubkey=self.wallet.public_key,
                    to_pubkey=recipient,
                    lamports=int(0.000001 * 10**9)  # trivial transfer
                )
            )
        )
        try:
            signature = await self.client.send_transaction(transfer_tx, self.wallet)
            print(f"Executed {trade_direction}. Tx Signature: {signature}")
        except Exception as e:
            print(f"Error executing trade: {e}")

    async def run_bot(self):
        """ Main loop to continuously check for opportunities """
        self.running = True
        while self.running:
            await self.check_arbitrage_opportunity()
            await asyncio.sleep(2)  # Pause briefly between checks

    def stop_bot(self):
        """ Stop the arbitrage loop """
        self.running = False
        print("Stopping arbitrage bot...")

