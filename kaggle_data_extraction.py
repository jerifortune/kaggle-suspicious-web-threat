import kagglehub

# Download latest version
path = kagglehub.dataset_download("jancsg/cybersecurity-suspicious-web-threat-interactions")

print("Path to dataset files:", path)