# config.py

# RPC endpoint (mainnet-beta example)
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"

# Serum Market Addresses (example placeholders)
# Replace with actual Serum markets you want to arbitrage.
MARKET_1_ADDRESS = "SomeSerumMarketAddress1"
MARKET_2_ADDRESS = "SomeSerumMarketAddress2"

# Your wallet private key (replace with your actual key or a path to a key file)
# For example, if your private key is in a .json file, load it here.
WALLET_PRIVATE_KEY = [0, 0, 0, ...]  # PASTE your actual key array (NOT RECOMMENDED for production)

# Trading settings
ARBITRAGE_THRESHOLD = 0.01  # 1% price difference threshold
TRADE_AMOUNT = 0.1          # Amount of base token to trade when an arb is found
