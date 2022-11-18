import os
import json

import logging
import datetime


logging_config = {
    'filename': "main_log.txt",
    'level': logging.DEBUG,
    'format': "%(asctime)s  [%(levelname)s] > %(message)s",
    'datefmt': "[%m-%d-%Y] ~ %I:%M:%S %p"
}

logging.basicConfig(**logging_config)

def test_log():    
    logging.info('Test Info')
    logging.debug('Test Debug')
    logging.warning('Test Warning')
    logging.error('Test Error')

def get_date(dt_format: str="%m-%d-%Y %I:%M:%S %p") -> str:
    now_dt = datetime.datetime.now().strftime(dt_format) 
    return now_dt


class State:
    def __init__(self, tracking_file="track.json"):
        self.filename = tracking_file
        
        self.log_config = None
        self.date_format = None # Default > %m-%d-%Y %I:%M:%S %p

        self.last_checked = None

        self.load_state()
    
    def load_state(self):
        with open(self.filename, 'r') as input_state:
            raw_state = json.load(input_state)
    
        self.log_config = raw_state.get('log_config', None)
        
        match self.log_config.get('level', None):
            case "debug":
                self.log_config['level'] = logging.DEBUG
            case "info":
                self.log_config['level'] = logging.INFO
            case "warning":
                self.log_config['level'] = logging.WARNING
            case "error":
                self.log_config['level'] = logging.ERROR

        self.date_format = raw_state.get('date_format', None)

        logging.basicConfig(**self.log_config)
        # if self.log_config is not None and self.date_format is not None:
        #     self.loaded = True


    def save_state(self):
        data = {
            'log_config': {**self.log_config, "level": "debug"},
            'date_format': self.date_format,
            "last_checked": get_date(self.date_format)
        }
        with open(self.filename, 'w') as output_data:
            json.dump(data, output_data, indent=4)
        
        logging.info("Data Saved!")


def main():
    # current_datetime = get_date()
    # print(current_datetime)

    new_state = State()
    new_state.save_state()

    # test_log()

if __name__ == '__main__':
    main()
