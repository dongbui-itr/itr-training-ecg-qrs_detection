TEST_TIME = 'run-0'
# DATABASE = 'ltdb/'
DATABASE = 'mitdb/'
<<<<<<< HEAD
PROJECT_DIR = 'itr-training-ecg-qrs_detection/'
=======
PROJECT_DIR = '/itr-training-ecg-qrs_detection/'
>>>>>>> 9b2d21c20127ffab4e8acca9c9d64ed8f5d2977a

SAVE_MODEL_DIR = PROJECT_DIR + 'model/' + DATABASE
TEMP_DIR = PROJECT_DIR + 'temp/'
TENSOR_BOARD_DIR = PROJECT_DIR + 'log/'
RESULT_DIR = PROJECT_DIR + 'result/'


LTDB_DIR = '/ltdb/'
MITDB_DIR = '/mitdb/'
AHADB_DIR = '/ahadb/'
ESCDB_DIR = '/escdb/'
NSTDB_DIR = '/nstdb/'

PREPROCESSED_DATA_DIR = '/itr-training-ecg-qrs_detection/' + DATABASE
<<<<<<< HEAD
CHECK_POINT_DIR = '/itr-training-ecg-qrs_detection/checkpoint/'
=======
CHECK_POINT_DIR = '/itr-training-ecg-qrs_detection/checkpoint/' + DATABASE
>>>>>>> 9b2d21c20127ffab4e8acca9c9d64ed8f5d2977a

FREQUENCY_SAMPLING = 360
NEIGHBOUR_POINT = int(FREQUENCY_SAMPLING * 0.1) + int(FREQUENCY_SAMPLING * 0.3) + 1
POSITIVE_RANGE = int(FREQUENCY_SAMPLING * 0.04) + 1

DATA_TYPE = 'float32'
