import pickle
from pathlib import Path
import pandas as pd
from dataclasses import  dataclass, asdict
from geo6.config.config import Config

config = Config()


@dataclass
class Data:
    soil_particle_size: pd.DataFrame
    cation_exchange_capacity: pd.DataFrame
    ph_cacl: pd.DataFrame
    ph_water: pd.DataFrame
    conductivity: pd.DataFrame
    chns: pd.DataFrame
    total_phenolic_compounds: pd.DataFrame
    dissolved_carbon_nitrogen: pd.DataFrame
    nitrification_rate: pd.DataFrame
    copper: pd.DataFrame
    uv_phenolic_compounds: pd.DataFrame
    microresp: pd.DataFrame
    

def read_csv(
    path: str | Path,
    col_types: dict | None = None
    ) -> pd.DataFrame:
        
        if col_types is None:
            df = pd.read_csv(
                    path,
                    sep=";",
                    decimal=",",
                    na_values=["NA"],
                )
            
        if col_types is not None:
            df = pd.read_csv(
                path,
                sep=";",
                decimal=",",
                na_values=["NA"],
                dtype=col_types,
            )
        
        float_cols = df.select_dtypes(include=["float64"]).columns
        df[float_cols] = df[float_cols].round(3)

        return df


tpc_types = {
    "sample": str,
    "type": str,
    "group": "float64",
    "subrep": "int64",
    "tpc_cacl_inc_ug_gae_kg_dm": "float64",
    "tpc_c_froz_ug_gae_kg_dm": "float64",
    "tpc_meoh_inc_ug_gae_kg_dm": "float64",
    "tpc_meoh_froz_ug_gae_kg_dm": "float64",
}


def load_data() -> Data:
    return Data(
        soil_particle_size=read_csv(config.particle_size_path),
        
        cation_exchange_capacity=read_csv(config.cation_exchange_capacity_path),
        
        ph_cacl=read_csv(config.ph_cacl_path),
        
        ph_water=read_csv(config.ph_water_path),
        
        conductivity=read_csv(config.conductivity_path),
        
        chns=read_csv(config.chns_path),
        
        total_phenolic_compounds=read_csv(
            config.total_phenolic_compounds_path,
            col_types=tpc_types
            ),
        
        dissolved_carbon_nitrogen=read_csv(config.dissolved_carbon_nitrogen_path),
     
        nitrification_rate=read_csv(config.nitrification_rate_path),

        copper=read_csv(config.copper_path),
        
        uv_phenolic_compounds=read_csv(config.uv_phenolic_compounds_path),

        microresp=read_csv(config.microresp_path),
    )
    

def export_data(data: Data, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("wb") as file:
        pickle.dump(
            asdict(data), 
            file, 
            protocol=pickle.HIGHEST_PROTOCOL
        )
        

def load_data_pickle(path: str | Path) -> Data:
    with Path(path).open("rb") as file:
        return pickle.load(file)