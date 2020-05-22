import logging
from datetime import datetime
import os.path
import pandas as pd

logger = logging.getLogger('nodes.data_transform')


def update(client, params):
	df=pd.read_csv(params.raw_data)
	df['date'] = str(datetime.today().year).zfill(4) + str(datetime.today().month).zfill(2) + str(datetime.today().day).zfill(2)
	df.to_csv(params.intermediate_data,index=False)

def done(client, params):
	return os.path.isfile(params.intermediate_data)
