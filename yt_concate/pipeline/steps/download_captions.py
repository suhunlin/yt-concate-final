from pytube import YouTube

from .step import Step


class DownloadCaptions(Step):
    def process(self, utils, inputs, data):
        for yt in data:
            if yt.check_caption_file_exists():
                # print(yt.caption_id + '.txt file exists!!!')
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError) as e:
                print('Download caption error in', e)
                continue
            # save the caption to a file named Output.txt
            text_file = open(yt.caption_filepath, "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        return data

    def __str__(self):
        return '<class DownloadCatpions: This class is use to download all captions file from yt.url>'

