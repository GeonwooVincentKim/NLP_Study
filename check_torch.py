import numpy as np
import torch

import multiprocessing

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)

model_ckpt = 'KETI-AIR/ke-t5-base'
max_token_length = 64
print(model_ckpt)
print(max_token_length)
