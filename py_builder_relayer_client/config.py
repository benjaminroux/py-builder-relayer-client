from dataclasses import dataclass

"""
export interface SafeContractConfig {
    SafeFactory: string;
    SafeMultisend: string;
}

export interface ContractConfig {
    SafeContracts: SafeContractConfig;
};

const AMOY: ContractConfig = {
    SafeContracts: {
        SafeFactory: "0xaacFeEa03eb1561C4e67d661e40682Bd20E3541b",
        SafeMultisend: "0xA238CBeb142c10Ef7Ad8442C6D1f9E89e07e7761",
    }
};

const POL: ContractConfig = {
    SafeContracts: {
        SafeFactory: "0xaacFeEa03eb1561C4e67d661e40682Bd20E3541b",
        SafeMultisend: "0xA238CBeb142c10Ef7Ad8442C6D1f9E89e07e7761",
    }
};

"""


@dataclass
class ContractConfig:
    """
    Contract Configuration
    """

    safe_factory: str

    safe_multisend: str


CONFIG = {
    137: ContractConfig(
        safe_factory="0xaacFeEa03eb1561C4e67d661e40682Bd20E3541b",
        safe_multisend="0xA238CBeb142c10Ef7Ad8442C6D1f9E89e07e7761",
    ),
    80002: ContractConfig(
        safe_factory="0xaacFeEa03eb1561C4e67d661e40682Bd20E3541b",
        safe_multisend="0xA238CBeb142c10Ef7Ad8442C6D1f9E89e07e7761",
    ),
}


def get_contract_config(chain_id: int) -> ContractConfig:
    """
    Gets the contract config
    """
    config = CONFIG.get(chain_id)
    if config is None:
        raise Exception(f"Invalid chainID: {chain_id}")

    return config
