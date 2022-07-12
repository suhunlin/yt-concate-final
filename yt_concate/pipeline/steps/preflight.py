from .step import Step


class Preflight(Step):
    def process(self, utils, inputs, data):
        return utils.create_dir()

    def __str__(self):
        return '<class Preflight: prepare before run program>'
