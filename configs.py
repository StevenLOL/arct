"""Record of config settings for reported experiments and retrievel."""
import pandas as pd
import glovar
import os


def get_seed(experiment_name, run_num):
    experiment_name = experiment_name.split('_seed')[0]
    df = pd.read_csv(os.path.join(glovar.DATA_DIR, 'all_results.csv'))
    exp = df[df['experiment_name'] == experiment_name]
    exp = exp[exp['run_no'] == run_num]
    seed = int(exp['seed'].values[0])
    return seed


def get_config(experiment_name):
    if experiment_name == 'compX':
        return {
            'train_subsample': 0,
            'name': 'compX',
            'stop_t_worse': 1,
            'projection_size': 200,
            'override': False,
            'lr_decay_grace': 0,
            'transfer': True,
            'p_drop': 0.1,
            'tokenizer': 'spacy',
            'lr_decay_every': 0.0,
            'target': 'train-full',
            'seed': -1,
            'l2': 0.0,
            'tune_target': 'dev-full',
            'stopping': 'min_lr',
            'encoder_layers': 1,
            'lr_decay_rate': 0.2,
            'tune_encoder': True,
            'annealing': 'tune_acc_decay',
            'sos_eos': True,
            'lr': 0.002,
            'embed_size': 300,
            'from_grid': True,
            'encoder_size': 2048,
            'hidden_size': 512,
            'batch_size': 16,
            'emb_lr_factor': 0.01,
            'n_runs': 20,
            'max_epochs': 200,
            'from_grid_trans': True,
            'embed_type': 'glove',
            'bidirectional': True,
            'encoder': 'lstm',
            'collator': 'rnn_sent',
            'model': 'comp',
            'enc_lr_factor': 1.0,
            'tune_embeds': True,
            'grid_name': 'compX_grid',
            'p_drop_rnn': 0.0,
            'stop_lr_lim': 1e-05,
            'transfer_name': 'e2048',
        }

    elif experiment_name == 't2048fwcomp':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't2048fwcomp',
            'batch_size': 16,
            'transfer_name': 'e2048',
            'sos_eos': True,
            'encoder_size': 2048,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'comp',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.002,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 'r2048fwcomp':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 'r2048fwcomp',
            'batch_size': 16,
            'transfer_name': 'e2048',
            'sos_eos': True,
            'encoder_size': 2048,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'comp',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': False,
            'stop_t_worse': 1,
            'transfer': False,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.002,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't1024fwcomp':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't1024fwcomp',
            'batch_size': 16,
            'transfer_name': 'e1024',
            'sos_eos': True,
            'encoder_size': 1024,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'comp',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.004,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 'r1024fwcomp':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 'r1024fwcomp',
            'batch_size': 16,
            'transfer_name': 'e1024',
            'sos_eos': True,
            'encoder_size': 1024,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'comp',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': False,
            'stop_t_worse': 1,
            'transfer': False,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.004,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't512fwcomp':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't512fwcomp',
            'batch_size': 16,
            'transfer_name': 'e512',
            'sos_eos': True,
            'encoder_size': 512,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'comp',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.003,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 1,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't512fwcompHalf':
        return {
            'train_subsample': 605,
            'name': 't512fwcompHalf',
            'stop_t_worse': 1,
            'projection_size': 200,
            'override': True,
            'lr_decay_grace': 0,
            'transfer': True,
            'p_drop': 0.1,
            'tokenizer': 'spacy',
            'lr_decay_every': 0.0,
            'target': 'train-full',
            'seed': -1,
            'l2': 0.0,
            'tune_target': 'dev-full',
            'stopping': 'min_lr',
            'encoder_layers': 1,
            'lr_decay_rate': 0.2,
            'tune_encoder': True,
            'annealing': 'tune_acc_decay',
            'sos_eos': True,
            'lr': 0.003,
            'embed_size': 300,
            'from_grid': False,
            'encoder_size': 512,
            'hidden_size': 512,
            'batch_size': 16,
            'emb_lr_factor': 0.01,
            'n_runs': 20,
            'max_epochs': 200,
            'from_grid_trans': True,
            'embed_type': 'glove',
            'bidirectional': True,
            'encoder': 'lstm',
            'collator': 'rnn_sent',
            'model': 'comp',
            'enc_lr_factor': 1.0,
            'tune_embeds': False,
            'grid_name': '',
            'p_drop_rnn': 0.0,
            'stop_lr_lim': 1e-05,
            'transfer_name': 'e512',
        }

    elif experiment_name == 't512fwcompN':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't512fwcompN',
            'batch_size': 16,
            'transfer_name': 'e512',
            'sos_eos': True,
            'encoder_size': 512,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'comp',
            'target': 'negs',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.003,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 'r512fwcomp':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 'r512fwcomp',
            'batch_size': 16,
            'transfer_name': 'e512',
            'sos_eos': True,
            'encoder_size': 512,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'comp',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': False,
            'stop_t_worse': 1,
            'transfer': False,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.003,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't300fwcomp':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't300fwcomp',
            'batch_size': 16,
            'transfer_name': 'e300',
            'sos_eos': True,
            'encoder_size': 300,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'comp',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.002,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 1,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 'r300fwcomp':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 'r300fwcomp',
            'batch_size': 16,
            'transfer_name': 'e300',
            'sos_eos': True,
            'encoder_size': 300,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'comp',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': False,
            'stop_t_worse': 1,
            'transfer': False,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.002,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 19,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't100fwcomp':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't100fwcomp',
            'batch_size': 16,
            'transfer_name': 'e100',
            'sos_eos': True,
            'encoder_size': 100,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'comp',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.003,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 'r100fwcomp':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 'r100fwcomp',
            'batch_size': 16,
            'transfer_name': 'e100',
            'sos_eos': True,
            'encoder_size': 100,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'comp',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': False,
            'stop_t_worse': 1,
            'transfer': False,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.003,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't512fwcompc':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't512fwcompc',
            'batch_size': 16,
            'transfer_name': 'e512',
            'sos_eos': True,
            'encoder_size': 512,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.1,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'compc',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.002,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't512fwcompcHalf':
        return {
            'train_subsample': 605,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't512fwcompcHalf',
            'batch_size': 16,
            'transfer_name': 'e512',
            'sos_eos': True,
            'encoder_size': 512,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.1,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'compc',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.002,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't512fwcompcN':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't512fwcompcN',
            'batch_size': 16,
            'transfer_name': 'e512',
            'sos_eos': True,
            'encoder_size': 512,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.1,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'compc',
            'target': 'negs',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.002,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't640fwcomprw2':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't640fwcomprw2',
            'batch_size': 16,
            'transfer_name': 'e640',
            'sos_eos': True,
            'encoder_size': 640,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'comprw2',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.006,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't2048fwlin':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't2048fwlin',
            'batch_size': 16,
            'transfer_name': 'e2048',
            'sos_eos': True,
            'encoder_size': 2048,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'lin',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.002,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 'r2048fwlin':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 'r2048fwlin',
            'batch_size': 16,
            'transfer_name': 'e2048',
            'sos_eos': True,
            'encoder_size': 2048,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'lin',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': False,
            'stop_t_worse': 1,
            'transfer': False,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.003,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't1024fwlin':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't1024fwlin',
            'batch_size': 16,
            'transfer_name': 'e1024',
            'sos_eos': True,
            'encoder_size': 1024,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'lin',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.003,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 'r1024fwlin':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 'r1024fwlin',
            'batch_size': 16,
            'transfer_name': 'e1024',
            'sos_eos': True,
            'encoder_size': 1024,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'lin',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': False,
            'stop_t_worse': 1,
            'transfer': False,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.003,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't512fwlin':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't512fwlin',
            'batch_size': 16,
            'transfer_name': 'e512',
            'sos_eos': True,
            'encoder_size': 512,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'lin',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.02,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 'r512fwlin':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 'r512fwlin',
            'batch_size': 16,
            'transfer_name': 'e512',
            'sos_eos': True,
            'encoder_size': 512,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'lin',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': False,
            'stop_t_worse': 1,
            'transfer': False,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.02,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't300fwlin':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't300fwlin',
            'batch_size': 16,
            'transfer_name': 'e300',
            'sos_eos': True,
            'encoder_size': 300,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'lin',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.02,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 'r300fwlin':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 'r300fwlin',
            'batch_size': 16,
            'transfer_name': 'e300',
            'sos_eos': True,
            'encoder_size': 300,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'lin',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': False,
            'stop_t_worse': 1,
            'transfer': False,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.02,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 't100fwlin':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 't100fwlin',
            'batch_size': 16,
            'transfer_name': 'e100',
            'sos_eos': True,
            'encoder_size': 100,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'lin',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': True,
            'stop_t_worse': 1,
            'transfer': True,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.2,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    elif experiment_name == 'r100fwlin':
        return {
            'train_subsample': 0,
            'tune_target': 'dev-full',
            'bidirectional': True,
            'projection_size': 200,
            'p_drop': 0.1,
            'collator': 'rnn_sent',
            'lr_decay_rate': 0.2,
            'tune_embeds': False,
            'name': 'r100fwlin',
            'batch_size': 16,
            'transfer_name': 'e100',
            'sos_eos': True,
            'encoder_size': 100,
            'stop_lr_lim': 1e-05,
            'emb_lr_factor': 0.01,
            'encoder': 'lstm',
            'encoder_layers': 1,
            'grid_name': '',
            'model': 'lin',
            'target': 'train-full',
            'tune_encoder': True,
            'l2': 0.0,
            'max_epochs': 200,
            'from_grid_trans': False,
            'stop_t_worse': 1,
            'transfer': False,
            'lr_decay_every': 0.0,
            'seed': -1,
            'tokenizer': 'spacy',
            'hidden_size': 512,
            'embed_type': 'glove',
            'lr': 0.2,
            'lr_decay_grace': 0,
            'embed_size': 300,
            'n_runs': 20,
            'p_drop_rnn': 0.0,
            'stopping': 'min_lr',
            'annealing': 'tune_acc_decay',
            'enc_lr_factor': 1.0,
            'override': True,
            'from_grid': False,
        }

    else:
        raise ValueError('Unexpexted experiment_name: %s' % experiment_name)
