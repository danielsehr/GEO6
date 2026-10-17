from pathlib import Path


class Config():
    data_root: Path = Path("data/")
    data_export_dir: Path = (data_root / "export")
    
    particle_size_path: Path = Path(data_root) / "particle_size_distribution.csv"
    cation_exchange_capacity_path: Path = Path(data_root) / "cation_exchange_capacity.csv"
    ph_cacl_path: Path = Path(data_root) / "ph_cacl.csv"
    ph_water_path: Path = Path(data_root) / "ph_water.csv"
    conductivity_path: Path = Path(data_root) / "conductivity.csv"
    chns_path: Path = Path(data_root) / "chns.csv"
    total_phenolic_compounds_path: Path = Path(data_root) / "total_phenolic_compounds.csv"
    dissolved_carbon_nitrogen_path: Path = Path(data_root) / "dissolved_carbon_nitrogen.csv"
    nitrification_rate_path: Path = Path(data_root) / "nitrification_rate.csv"
    copper_path: Path = Path(data_root) / "copper.csv"
    uv_phenolic_compounds_path: Path = Path(data_root) / "uv_phenolic_compounds.csv"
    microresp_path: Path = Path(data_root) / "microresp.csv"