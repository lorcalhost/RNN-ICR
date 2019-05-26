from textgenrnn import textgenrnn

file_name = "gz_dataset.txt"
model_name = 'CNN_ICR'   # change to set file name of resulting trained models/texts
textgen = textgenrnn(name=model_name)

train_function = textgen.train_from_largetext_file

train_function(
    file_path=file_name,
    new_model=True,
    num_epochs=20,  # set higher to train the model for longer
    gen_epochs=1,  # generates sample text from model after given number of epochs
    batch_size=1024,
    train_size=0.8,  # proportion of input data to train on
    dropout=0.0, # ignore a random proportion of source tokens each epoch, allowing model to generalize better
    validation=False,
    is_csv=False,
    rnn_layers=3, # number of LSTM layers
    rnn_size=128,  # number of LSTM cells of each layer
    rnn_bidirectional=True, # consider text both forwards and backward, can give a training boost
    max_length=8, # number of tokens to consider before predicting the next (20-40 for characters, 5-10 for words is best)
    dim_embeddings=100,
    word_level=True)
