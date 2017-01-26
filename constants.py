#########
# Service
#########

SERVICE_ENDPOINT = "http://35.164.83.223:9000/mnist/classify"

######
# Data
######

NB_TEST_EXAMPLES = 10000
NB_TRAINING_EXAMPLES = 60000
NB_CLASSES = 10
# input image dimensions
IMG_ROWS, IMG_COLS = 28, 28
FLAT_IMAGE_LENGTH = IMG_ROWS * IMG_COLS

################
# Model training
################

CNN_MODEL_FILENAME = 'cnn_model.h5'

RANDOM_STATE = 2017
BATCH_SIZE = 128
NB_EPOCH = 10

# number of convolutional filters to use
NB_FILTERS = 32
# size of pooling area for max pooling
POOL_SIZE = (2, 2)
# convolution kernel size
KERNEL_SIZE = (3, 3)