from .step import Step

from yt_concate.models.found import Found

class Search(Step):
    def process(self, utils, inputs, data):
        search_word = inputs['search_word']
        found = []
        for yt in data:
            if not yt.check_caption_file_exists():
                # print(yt.caption_id + '.txt file not exists!!!')
                continue
            captions = yt.captions
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)
        # for obj in found:
        #     print(obj.yt,obj.caption,obj.time)
        return found

    def __str__(self):
        return '<class Search: This class is use for search key word and recorder to Found data structure>'



