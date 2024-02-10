from dataclasses import dataclass
from torch.untils.data.dataloader import DataLoader

@dataclass
class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str 
