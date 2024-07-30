import pandas as pd
import sqlalchemy
import json

class Extractor:
    def extract(self, source_type, source):
        if source_type == "csv":
            return self.extract_csv(source)
        elif source_type == "json":
            return self.extract_json(source)
        elif source_type == "sql":
            return self.extract_sql(source)
        else:
            print("Unsupported source type")
            return None
        
    def extract_csv(input_file_path):
        try:
            data = pd.read_csv(input_file_path, encoding='unicode_escape')
            print("Data extraction complete.")
            return data
        except Exception as e:
            print(f"Error extracting csv data: {e}")
            return None
        
    def extract_json(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            data = pd.json_normalize(data)
            return data
        except Exception as e:
            print(f"Error reading JSON {file_path}: {e}")
            return None

    def extract_sql(self, connection_string, query):
        try:
            from sqlalchemy import create_engine
            engine = create_engine(connection_string)
            data = pd.read_sql(query, engine)
            return data
        except Exception as e:
            print(f"Error executing query: {e}")
            return None


