'''
Author: xmh
Date: 2021-06-08 20:45:03
LastEditors: xmh
LastEditTime: 2021-06-09 12:06:53
Description:
FilePath: \DPCNN\\utils\\config.py
'''

import torch
from utils.arg_config import args

class Config:

    def __init__(self,
            embedding_dim=300,
        ):
        
        self.embedding_dim = embedding_dim
        
        self.num_filter = 32
        # self.dropout_embedding_rate = 0.5
        self.num_rel = 2
        self.batch_size = 128
        self.vocab_file = '../data/vocab.txt'
        # self.vocab_file = '../data/vocab_pretrain.txt'

        cnt = 1  # 添加padd的位置
        with open(self.vocab_file, 'r') as f:
            for line in f:
                cnt += 1
        self.vocab_size = cnt
        self.epochs = 100
        self.lr = 1e-3

        if torch.cuda.is_available():
            self.USE_CUDA = False
        else:
            self.USE_CUDA = False
        
        self.using_pretrained_embedding = args['use_pre_embed']


config = Config()

