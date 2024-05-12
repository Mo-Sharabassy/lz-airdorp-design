# LZ-AirDrop-Design: LayerZero AirDrop Design Project Process

## Introduction to LayerZero

LayerZero is a novel technology that enables the scaling of blockchain networks by introducing the Omnichain concept, which facilitates seamless integration between different blockchain networks.

## AirDrop Design Project

The AirDrop design project focused on the best-performing Decentralized Validator Networks (DVNs). When building an application on top of LayerZero, a primary required validator must be chosen for transactions, followed by optional validators (e.g., option1, option2, etc.). Each validator is connected to different blockchain networks through endpoints, such as Nethermind, which has a contract on Ethereum for validating transactions from Ethereum, as well as endpoints on Polygon, Arbitrum, and others.

## Performance Metrics

 The following metrics were selected to evaluate the performance of DVNs:
 - Number of transactions (successful, failed, pending)
 - Time taken to process transactions
 - Value/data handled from these transactions

## Data Collection and Analysis

With the guidance of the team leader, I initially explored LayerZero Labs (a DVN on Ethereum) smart contract data decoded by Dune Analytics (Crypto's Data Platform) and extracted from the Ethereum blockchain into structured tables. However, this approach did not provide a comprehensive view of the data. Submitting individual contracts from each DVN from each endpoint and consolidating the data into a single dataset seemed inaccurate and cumbersome.

## LayerZero API and Data Scraping

LayerZero is expected to provide APIs for consolidated data access, which is currently under development. In the meantime, I decided to scrape a single snapshot of LayerZero Scan Data, which provided 100 transactions per minute of API response. This allowed me to collect data from a consolidated point of view and run various queries.

## Data Processing and Visualization

You can find the script used to collect, normalize, and clean the data in this notebook [lz_scan_data](lz_scan_data.py). After exploring and cleaning the data, I downloaded it as a CSV file and uploaded it to Dune Analytics as a database. Afterwards, I built this dashboard [sharabassy/lz-scan-poc](https://dune.com/sharabassy/lz-scan-poc).

## POC for AirDrop Design

Although the data from the API response did not provide significant insights into DVN performance based on the selected metrics, I hope that the upcoming LayerZero API will enable more comprehensive analysis. Beyond the airdrop design, it would be fascinating to work on Omnichain application (OApp) analysis, leveraging data from different blockchain networks simultaneously.

## Important Links

- [LayerZero White Paper](https://layerzero.network/publications/LayerZero_Whitepaper_V2.1.0.pdf)
- [LayerZero Scan](https://layerzeroscan.com/)
- [Check API Response](https://support.demandbase.com/hc/en-us/articles/7484772828187-Check-API-Response)
- [Dune Analytics](https://dune.com/home)