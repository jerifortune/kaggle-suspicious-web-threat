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
         

df = read_file("CloudWatch_Traffic_Web_Attack.csv")


# Converting to dataframe

df = pd.DataFrame(df)

df.head(5)
