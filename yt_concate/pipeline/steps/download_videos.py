from pytube import YouTube

from .step import Step
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, utils, inputs, data):
        yt_set = set([found.yt for found in data])

        for yt in yt_set:
            if yt.check_video_file_exists():
                # print(yt.caption_id + '.mp4 file exists!!!')
                continue
            print(yt.url,'downloading.......')
            YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.caption_id + '.mp4')
        return data

    def __str__(self):
        return '<class DownloadVideos: This class is use for download all youtube video aboud search word>'
