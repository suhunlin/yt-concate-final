import os

from settings import OUTPUTS_DIR
from settings import DOWNLOADS_DIR
from settings import VIDEOS_DIR
from settings import CAPTIONS_DIR


class Utils:
    def create_dir(self):
        os.makedirs(OUTPUTS_DIR, exist_ok=True)
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        return 'Create dir ok'

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def check_video_list_file_exists(self, filepath):
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def get_output_filepath(self, inputs):
        filename = inputs['channel_id'] + inputs['search_word'] + '.mp4'
        return os.path.join(OUTPUTS_DIR, filename)
