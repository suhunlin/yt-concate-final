from .step import Step


class ReadCaptions(Step):
    def process(self, utils, inputs, data):
        for yt in data:
            if not yt.check_caption_file_exists():
                # print(yt.caption_id + '.txt file not exists!!!')
                continue
            captions = {}
            time_line = False
            with open(yt.caption_filepath, 'r') as f:
                for line in f:
                    if "-->" in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        time_line = False
                        caption = line.strip()
                        captions[caption] = time
            yt.captions = captions

        # for obj in data:
        #     print(obj.captions)
        return data

    def __str__(self):
        return '<class ReadCaption: This class is use for read caption to dictionary format. and save to yt.captions.>'
