def get_java_config():
    conf = {
        'workdir': './java/',
        # data_params
        # training data
        'train_name': 'train.methname.h5',
        'train_api': 'train.apiseq.h5',
        'train_tokens': 'train.tokens.h5',
        'train_desc': 'train.desc.h5',
        # test data
        'valid_name': 'test.methname.h5',
        'valid_api': 'test.apiseq.h5',
        'valid_tokens': 'test.tokens.h5',
        'valid_desc': 'test.desc.h5',
        # use data (computing code vectors)
        'use_codebase': 'use.rawcode.txt',  # 'use.rawcode.h5'
        'use_names': 'use.methname.h5',
        'use_apis': 'use.apiseq.h5',
        'use_tokens': 'use.tokens.h5',
        # results data(code vectors)
        'use_codevecs': 'use.codevecs.normalized.h5',  # 'use.codevecs.h5',

        # parameters
        'name_len': 6,
        'api_len': 30,
        'tokens_len': 50,
        'desc_len': 30,
        'n_words': 10000,  # len(vocabulary) + 1
        # vocabulary info
        'vocab_name': 'vocab.methname.pkl',
        'vocab_api': 'vocab.apiseq.pkl',
        'vocab_tokens': 'vocab.tokens.pkl',
        'vocab_desc': 'vocab.desc.pkl',

        # training_params
        'batch_size': 1024,
        'chunk_size': 100000,
        #'nb_epoch': 2000,
        'nb_epoch': 2,
        'validation_split': 0.2,
        # 'optimizer': 'adam',
        'lr': 0.001,
        'valid_every': 10,
        'n_eval': 100,
        'evaluate_all_threshold': {
            'mode': 'all',
            'top1': 0.4,
        },
        'log_every': 100,
        'save_every': 10,
        'reload': -1,
        # 970,#epoch that the model is reloaded from . If reload=0, then train from scratch
        # 'reload': 1,

        # model_params
        'emb_size': 100,
        'n_hidden': 400,  # number of hidden dimension of code/desc representation
        # recurrent
        'lstm_dims': 200,  # * 2
        'init_embed_weights_methname': None,  # 'word2vec_100_methname.h5',
        'init_embed_weights_tokens': None,  # 'word2vec_100_tokens.h5',
        'init_embed_weights_desc': None,  # 'word2vec_100_desc.h5',
        'margin': 0.05,
        'sim_measure': 'cos',  # similarity measure: gesd, cosine, aesd

    }
    return conf


def get_python_config():
    conf = {
        'workdir': './python/',
        # data_params
        # training data
        'train_name': 'train.methname.npy',
        'train_api': 'train.apiseq.npy',
        'train_tokens': 'train.tokens.npy',
        'train_desc': 'train.desc.npy',
        # test data
        'valid_name': 'small.test.methname.npy',
        'valid_api': 'small.test.apiseq.npy',
        'valid_tokens': 'small.test.tokens.npy',
        'valid_desc': 'small.test.desc.npy',
        # use data (computing code vectors)
        'use_codebase': 'small.rawcode.txt', # 'full.rawcode.txt',  # 'use.rawcode.h5'
        'use_names': 'train.methname.npy',
        'use_apis': 'train.apiseq.npy',
        #'use_tokens': 'train.apiseq.npy',
        'use_tokens': 'train.tokens.npy',
        # results data(code vectors)
        'use_codevecs': 'use.codevecs.normalized.h5',  # 'use.codevecs.h5',

        # parameters
        'name_len': 5,
        'api_len': 45,
        'tokens_len': 55,
        'desc_len': 15,
        'n_words': 10002,  # len(vocabulary) + 1
        # vocabulary info
        'vocab_name': 'vocab.methname.pkl',
        'vocab_api': 'vocab.apiseq.pkl',
        'vocab_tokens': 'vocab.tokens.pkl',
        'vocab_desc': 'vocab.desc.pkl',

        # training_params
        'batch_size': 512,
        'chunk_size': 100000,
        'nb_epoch': 1,
        'validation_split': 0.2,
        # 'optimizer': 'adam',
        'lr': 0.001,
        'valid_every': 10,
        'n_eval': 100,
        'evaluate_all_threshold': {
            'mode': 'all',
            'top1': 0.4,
        },
        'log_every': 100,
        'save_every': 3,
        #'reload': -1,
        # 970,#epoch that the model is reloaded from . If reload=0, then train from scratch
        'reload': 1,

        # model_params
        'emb_size': 100,
        'n_hidden': 400,  # number of hidden dimension of code/desc representation
        # recurrent
        'lstm_dims': 200,  # * 2
        'init_embed_weights_methname': None,  # 'word2vec_100_methname.h5',
        'init_embed_weights_tokens': None,  # 'word2vec_100_tokens.h5',
        'init_embed_weights_desc': None,  # 'word2vec_100_desc.h5',
        'margin': 0.05,
        'sim_measure': 'cos',  # similarity measure: gesd, cosine, aesd

    }
    return conf
