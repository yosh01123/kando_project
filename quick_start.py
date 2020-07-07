import json
from kando import kando_client
import datetime
import pandas as pd 
import matplotlib.pyplot as  plt 


def get_data(point_id =1012 ,start = datetime.datetime(2017, 12, 1, 0, 0).timestamp() , end= datetime.datetime(2018, 1, 1, 0, 0).timestamp() ):
	'''function calling the api from start to end and return the data in a dataframe with colums: PI, EC, PH, WL, ORPM TEMPERATURE.
	point_id : int 
	start: timestamp 
	end : timestamp 
	return df: dataframe 
	'''
	with open('key.json') as f:
	    secret = json.load(f)

	client = kando_client.client("https://app.kando.eco", secret['key'], secret['secret'])


	data = client.get_all(point_id, '', start, end)
	df = pd.DataFrame(data['samplings']).transpose()
	#I these 3 colums does not contain significant columns, mostly Nan values ...
	try:
		df.drop(['DateTime', 'Battery', 'Signal', 'WL'], axis = 1, inplace = True)
	except :
		pass

	return data

	



def plot_columns(df, col): 
	fig, ax = plt.subplots()
	ax.plot(df[col])
	ax.set_title(f'plot of {col}')
	ax.set_ylabel(f'{col}')
	fig.savefig(f'{col}.png')



