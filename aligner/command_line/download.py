import requests
import os

from aligner.exceptions import ArgumentError
from aligner.models import G2PModel, AcousticModel
from aligner.utils import get_pretrained_acoustic_path, get_pretrained_g2p_path, get_dictionary_path


def list_available_languages(model_type):
    url = 'https://raw.githubusercontent.com/MontrealCorpusTools/mfa-models/master/{}/index.txt'.format(model_type)
    r = requests.get(url)
    out = r.text
    return out.split('\n')


def download_model(model_type, language):
    if language is None:
        print('Available languages to download for {}:'.format(model_type))
        for lang in list_available_languages(model_type):
            print(lang)
        return
    if model_type == 'acoustic':
        extension = AcousticModel.extension
        out_path = get_pretrained_acoustic_path(language)
    elif model_type == 'g2p':
        extension = G2PModel.extension
        out_path = get_pretrained_g2p_path(language)
    elif model_type == 'dictionary':
        extension = '.dict'
        out_path = get_dictionary_path(language)
    else:
        raise NotImplementedError
    url = 'https://github.com/MontrealCorpusTools/mfa-models/raw/master/{}/{}{}'.format(model_type, language, extension)

    r = requests.get(url)
    with open(out_path, 'wb') as f:
        f.write(r.content)


def validate_args(args):
    args.model_type = args.model_type.lower()
    if args.model_type not in ['acoustic', 'g2p', 'dictionary']:
        raise ArgumentError("model_type must be one of 'acoustic', 'g2p', or 'dictionary'")
    if args.language is not None:
        available_languages = list_available_languages(args.model_type)
        if args.language not in available_languages:
            raise ArgumentError('Could not find {}, possible languages for download are: {}'.format(args.language, ', '.join(available_languages)))


def run_download(args):
    validate_args(args)
    download_model(args.model_type, args.language)


if __name__ == '__main__':
    from aligner.command_line.mfa import download_parser
    args = download_parser.parse_args()

    run_download(args)
