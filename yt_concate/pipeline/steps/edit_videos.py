from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

from .step import Step


class EditVideos(Step):
    def process(self, utils, inputs, data):
        clips = []
        for found in data:
            if not found.yt.check_video_file_exists():
                continue
            if found.yt.caption_id == 'b9dWgUlMb9o':
                continue
            start, end = self.parser_caption_time(found.time)
            # print(start, end)
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break
        print(len(clips))
        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(inputs)
        final_clip.write_videofile(output_filepath)
        return data

    def parser_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parser_time_str(start), self.parser_time_str(end)

    def parser_time_str(self, time):
        h, m, s = time.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms) / 1000
