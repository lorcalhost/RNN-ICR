from textgenrnn import textgenrnn


textgen = textgenrnn(weights_path='RNN-ICR_weights.hdf5',
                     vocab_path='RNN-ICR_vocab.json',
                     config_path='RNN-ICR_config.json')

textgen.generate_samples(max_gen_length=1000)
textgen.generate_to_file('RNN-ICR_gentext.txt', max_gen_length=1000)
