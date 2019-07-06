import yaml,glob,os
config_file_extension = ".yaml"

class StationConfig:
    def __init__(self,filename):
        self.filename = filename
        with open(filename, 'r') as stream:
            try:
                self.raw_config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def load_available_config_file(path):
        return glob.glob(os.path.join(path,"*"+config_file_extension))
