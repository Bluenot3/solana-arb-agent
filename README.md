# Simple Solana Arbitrage Bot

This repository contains a **basic, educational** Solana arbitrage bot that:
- Monitors two (simulated) Serum markets for price differences.
- Executes trades when a threshold is met.
- Includes a Streamlit user interface to start/stop the bot and tweak settings.

## Features
- Written in Python, uses `solana-py` and `serum-py` libraries for Solana interactions.
- A simple UI with Streamlit to control the bot.
- Configurable threshold, trade amount, and Solana RPC endpoint in `config.py`.

## Setup & Installation
1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/YourUsername/my-solana-arb-bot.git
   cd my-solana-arb-bot
