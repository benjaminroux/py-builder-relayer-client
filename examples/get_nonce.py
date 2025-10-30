from py_builder_relayer_client.client import RelayClient

from dotenv import load_dotenv
import os

load_dotenv()


def main():
    print("starting...")
    relayer_url = os.getenv("RELAYER_URL", "https://relayer-v2-staging.polymarket.dev/")
    chain_id = int(os.getenv("CHAIN_ID", 80002))
    client = RelayClient(relayer_url, chain_id)

    resp = client.get_nonce("0x6e0c80c90ea6c15917308F820Eac91Ce2724B5b5", "SAFE")
    print(resp)


main()
