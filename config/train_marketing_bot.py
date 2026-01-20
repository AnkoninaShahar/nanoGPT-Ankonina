import time;

# Marketing bot configuration
out_dir = 'out-marketing-bot'
eval_interval = 200
log_interval = 1
eval_iters = 200
wandb_log = True
wandb_project = 'marketing-bot'
wandb_run_name = 'marketing-gpt-' + str(time.time())
# Data
dataset = 'marketing_bot'
batch_size = 16
block_size = 512
# Model architecture
n_layer = 8
n_head = 8
n_embd = 512
dropout = 0.1
bias = False
# Optimizer
learning_rate = 3e-4
max_iters = 5000
weight_decay = 1e-1
beta1 = 0.9
beta2 = 0.95
grad_clip = 1.0
decay_lr = True
warmup_iters = 100
# Hardware
device = 'cpu'  # or 'cuda'
compile = True
