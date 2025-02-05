import kagglehub;
import pandas as pd;



# Download  kaggle cybersecurity-suspicious-web-threat-interactions dataset
path = kagglehub.dataset_download("jancsg/cybersecurity-suspicious-web-threat-interactions")

print("Path to dataset files:", path)

# use pandas  to read the dataset - json and csv format only
def read_file(file_path):
     if file_path.endswith('.json'):
         return pd.read_csv(file_path)
     elif file_path.endswith('.csv'):
         return pd.read_csv(file_path)
     else:
         raise ValueError("Invalid file type. This function only acecepts json and csv file formats")
         
df = read_file('CloudWatch_Traffic_Web_Attack.csv')


# convert dates to datetime
df['creation_time'] = pd.to_datetime(df['creation_time'])
df['end_time'] = pd.to_datetime(df['end_time'])
df['time'] = pd.to_datetime(df['time'])

# Converting to dataframe

df = pd.DataFrame(df)

#df.head(5)
#df.columns

# change the data types
new_dtype_dict = {
    'bytes_in':'int64', 
    'bytes_out':'int64', 
    'src_ip':'str',
    'src_ip_country_code':'str', 
    'protocol':'str' ,
    'response.code':'int64', 
    'dst_port':'int64',
    'dst_ip':'str', 
    'rule_names':'str', 
    'observation_name':'str', 
    'source.meta':'str',
    'source.name':'str', 
    'detection_types':'str'
    }

df.astype(new_dtype_dict)

# Renaming the columns

cols_new_name_dict = {
    'bytes_in':'bytes_in', 
    'bytes_out':'bytes_out', 
    'creation_time':'creation_time', 
    'end_time':'end_time', 
    'src_ip':'source_ip',
    'src_ip_country_code':'source_ip_country_code', 
    'protocol':'protocol' ,
    'response.code':'response_code', 
    'dst_port':'destination_port',
    'dst_ip':'destination_ip', 
    'rule_names':'rule', 
    'observation_name':'observation', 
    'source.meta':'source_metadata',
    'source.name':'source_name', 
    'time':'event_detection_time', 
    'detection_types':'detection_types'
    }
df.rename(cols_new_name_dict, axis=1, inplace=True)



# Add a calculated column
df['event_duration'] = df['end_time']- df['creation_time']

# covert the event duration to seconds
df['event_duration'] = df['event_duration'].dt.seconds
df.head(5)