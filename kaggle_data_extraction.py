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



# Converting to dataframe

df = pd.DataFrame(df)

df.head(5)
df.columns


# Renaming the columns

cols_new_name_dict = {
    'bytes_in':'', 
    'bytes_out':'', 
    'creation_time':'creation_time', 
    'end_time':'nd_time', 
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
df.head(5)