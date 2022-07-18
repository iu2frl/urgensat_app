import yaml,glob,os,logging,helpers
config_file_extension = ".yaml"

class StationConfig:
    def __init__(self,filename):
        self.filename = filename
        self.logger = logging.getLogger('station')

        try:
            with open(filename, 'r') as stream:
                try:
                    self.raw_config = yaml.safe_load(stream)
                except Exception as e:
                    self.logger.exception("Unable to parse '"+filename+"'")
                    helpers.terminate()
        except Exception as e:
            self.logger.exception("Error opening '"+filename+"'")
            helpers.terminate()

        
    @staticmethod
    def load_available_config_file(path):
        return glob.glob(os.path.join(path,"*"+config_file_extension))
