import os
import json
import MeCab

tagger = MeCab.Tagger("-Owakati")
tagger.parse("")


def load_json(file_name):
    json_file = open(file_name, 'r')
    json_data = json.load(json_file)
    json_file.close()
    return json_data


def main():
    request = open('train/request.txt', 'w')
    response = open('train/response.txt', 'w')
    for file_name in os.listdir('./json/rest1046'):
        file_path = os.path.join('./json/rest1046', file_name)
        json_data = load_json(file_path)
        U = ""
        S = ""
        for data in json_data['turns']:
            utterance = data['utterance']
            speaker = data['speaker']
            if len(utterance) == 0:
                continue

            if speaker == 'U':
                U = utterance + '\n'
            else:
                S = utterance + '\n'

            if U != "" and S != "":
                request.write(tagger.parse(U))
                response.write(tagger.parse(S))
                U = S = ""


if __name__ == '__main__':
    main()