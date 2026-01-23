# config/train_marketing_bot_small.py
import time

out_dir = 'out-marketing-bot-small'
eval_interval = 100
log_interval = 10
eval_iters = 50
always_save_checkpoint = True

wandb_log = False

dataset = 'marketing_bot'
batch_size = 4
block_size = 128

# TINY model
n_layer = 2
n_head = 2
n_embd = 128
dropout = 0.1
bias = False

learning_rate = 5e-4
max_iters = 500
weight_decay = 1e-1
beta1 = 0.9
beta2 = 0.95
grad_clip = 1.0
decay_lr = False
warmup_iters = 50

device = 'cpu'
compile = False