import logging
import pandas as pd
from datetime import datetime


logger = logging.getLogger('nodes.data_storage')


def update(client, params):
	df=pd.read_csv(params.intermediate_data)
	df.to_sql('movies', client.conn, index=False, if_exists='append')
	logger.info(f'Results stored for {datetime.now().strftime("%Y-%m-%d")}')
def done(client, params):
	#method 1 - DO NOT USE ler o arquivo dump.log e usar regex ou in para verificar se está escrito o results stored for data
	#method 2 - USE THIS verificar se a data esta na base de dados
	return False
