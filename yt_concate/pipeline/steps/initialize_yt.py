from yt_concate.models.yt import YT
from .step import Step


class InitializeYT(Step):
    def process(self, utils, inputs, data):
        return [YT(url) for url in data]

    def __str__(self):
        return '<class InitializeYT: This class is initialize yt data structure. Ever parameter in list is YT(url)' + '\n'
