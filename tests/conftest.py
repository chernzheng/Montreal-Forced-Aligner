
import os
import pytest

from aligner.corpus import Corpus
from aligner.config import MfccConfig
from aligner.dictionary import Dictionary

@pytest.fixture(scope='session')
def test_dir():
    return os.path.abspath('tests/data')

@pytest.fixture(scope='session')
def generated_dir(test_dir):
    generated = os.path.join(test_dir, 'generated')
    if not os.path.exists(generated):
        os.makedirs(generated)
    return generated

@pytest.fixture(scope='session')
def basic_dir(test_dir):
    return os.path.join(test_dir, 'basic')

@pytest.fixture(scope='session')
def dict_dir(test_dir):
    return os.path.join(test_dir, 'dictionaries')

@pytest.fixture(scope='session')
def basic_dict_path(dict_dir):
    return os.path.join(dict_dir, 'basic.txt')

@pytest.fixture(scope='session')
def expected_dict_path(dict_dir):
    return os.path.join(dict_dir, 'expected')

@pytest.fixture(scope='session')
def basic_topo_path(expected_dict_path):
    return os.path.join(expected_dict_path, 'topo')

@pytest.fixture(scope='session')
def basic_graphemes_path(expected_dict_path):
    return os.path.join(expected_dict_path, 'graphemes.txt')

@pytest.fixture(scope='session')
def basic_phone_map_path(expected_dict_path):
    return os.path.join(expected_dict_path, 'phone_map.txt')

@pytest.fixture(scope='session')
def basic_phones_path(expected_dict_path):
    return os.path.join(expected_dict_path, 'phones.txt')

@pytest.fixture(scope='session')
def basic_words_path(expected_dict_path):
    return os.path.join(expected_dict_path, 'words.txt')

@pytest.fixture(scope='session')
def basic_rootsint_path(expected_dict_path):
    return os.path.join(expected_dict_path, 'roots.int')

@pytest.fixture(scope='session')
def basic_rootstxt_path(expected_dict_path):
    return os.path.join(expected_dict_path, 'roots.txt')

#@pytest.fixture(scope='session')
#def basic_roots_path(expected_dict_path):
#    return os.path.join(expected_dict_path, 'roots.txt')

@pytest.fixture(scope='session')
def basic_setsint_path(expected_dict_path):
    return os.path.join(expected_dict_path, 'sets.int')

@pytest.fixture(scope='session')
def basic_setstxt_path(expected_dict_path):
    return os.path.join(expected_dict_path, 'sets.txt')

@pytest.fixture(scope='session')
def basic_word_boundaryint_path(expected_dict_path):
    return os.path.join(expected_dict_path, 'word_boundary.int')

@pytest.fixture(scope='session')
def basic_word_boundarytxt_path(expected_dict_path):
    return os.path.join(expected_dict_path, 'word_boundary.txt')

@pytest.fixture(scope='session')
def sick_dict_path(dict_dir):
    return os.path.join(dict_dir, 'sick.txt')

@pytest.fixture(scope='session')
def acoustic_corpus_wav_path(basic_dir):
    return os.path.join(basic_dir, 'acoustic_corpus.wav')

@pytest.fixture(scope='session')
def acoustic_corpus_lab_path(basic_dir):
    return os.path.join(basic_dir, 'acoustic_corpus.lab')

@pytest.fixture(scope='session')
def acoustic_corpus_textgrid_path(basic_dir):
    return os.path.join(basic_dir, 'acoustic_corpus.TextGrid')

@pytest.fixture(scope='session')
def sick_dict(sick_dict_path, generated_dir):
    output_directory = os.path.join(generated_dir, 'sickcorpus')
    dictionary = Dictionary(sick_dict_path, output_directory)
    dictionary.write()
    return dictionary

@pytest.fixture(scope='session')
def sick_corpus(sick_dict, basic_dir, generated_dir):
    output_directory = os.path.join(generated_dir, 'sickcorpus')
    c = MfccConfig(output_directory)
    corpus = Corpus(basic_dir, output_directory, c, num_jobs = 2)
    corpus.write()
    corpus.create_mfccs()
    corpus.setup_splits(sick_dict)
    return corpus


