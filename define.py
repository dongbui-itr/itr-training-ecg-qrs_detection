TEST_TIME = 'run-0'
# DATABASE = 'ltdb/'
DATABASE = 'mitdb/'
PROJECT_DIR = '/itr-training-ecg-qrs_detection/'

SAVE_MODEL_DIR = PROJECT_DIR + 'model/' + DATABASE
TEMP_DIR = PROJECT_DIR + 'temp/'
TENSOR_BOARD_DIR = PROJECT_DIR + 'log/' + DATABASE
RESULT_DIR = PROJECT_DIR + 'result/' + DATABASE


LTDB_DIR = '/ltdb/'
MITDB_DIR = '/mitdb/'
AHADB_DIR = '/ahadb/'
ESCDB_DIR = '/escdb/'
NSTDB_DIR = '/nstdb/'

PREPROCESSED_DATA_DIR = '/itr-training-ecg-qrs_detection/' + DATABASE
CHECK_POINT_DIR = '/itr-training-ecg-qrs_detection/checkpoint/' + DATABASE

FREQUENCY_SAMPLING = 250
NEIGHBOUR_POINT = int(FREQUENCY_SAMPLING * 0.1) + int(FREQUENCY_SAMPLING * 0.3) + 1
POSITIVE_RANGE = int(FREQUENCY_SAMPLING * 0.04) + 1

DATA_TYPE = 'float32'
