import os
import shutil
import re

from .prep import prepare_dict, prepare_lang, prepare_train_data, prepare_mfccs, prepare_config

def data_prep(data_directory, lm_path):
    """
    Prepares data for alignment from a directory of sound files with
    TextGrids (or label files)

    Parameters
    ----------
    source_dir : str
        Path to directory of sound files to align
    temp_dir : str
        Path to directory to temporary store files used in alignment
    dict_path : str
        Path to a pronunciation dictionary
    lm_path : str
        Path to a language model
    """
    config_dir = os.path.join(data_directory, 'conf')
    if not os.path.exists(config_dir):
        print('Creating a config directory...')
        prepare_config(config_dir)
        print('Done!')
    else:
        print('Using existing config directory.')

    lang_dir = os.path.join(data_directory, 'lang')
    if not os.path.exists(lang_dir):
        print('Preparing dictionary and language models...')
        prepare_dict(data_directory)
        prepare_lang(data_directory, lm_path)
        print('Done!')
    else:
        print('Using existing dictionary and language models.')

    train_dir = os.path.join(data_directory, 'train')
    if not os.path.exists(train_dir):
        print('Preparing training data...')
        files_dir = os.path.join(data_directory, 'files')
        prepare_train_data(files_dir, train_dir)
        print('Done!')
    else:
        print('Using existing training set up.')


    mfcc_dir = os.path.join(data_directory, 'mfcc')
    if not os.path.exists(mfcc_dir):
        print('Creating mfccs...')
        mfcc_config = os.path.join(config_dir, 'mfcc.conf')
        prepare_mfccs(train_dir, mfcc_dir, mfcc_config, num_jobs = 6)
        print('Done!')
    else:
        print('Using existing mfccs.')

def transcription_prep():
    pass

def dictionary_prep():
    pass

def lm_prep():
    pass

def mfcc_prep():
    pass