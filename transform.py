
class Transfoermer:

    def transform(self, data):
        if data == "csv":
            return self.transform_csv(data)
        elif data == "json":
            return self.transform_json(data)
        elif data == "sql":
            return self.transform_sql(data)
        else:
            print("Unsupported source type")
            return None

        
    def transform_csv(data):
        try:
            # Example transformation: Drop rows with any missing values
            transformed_data = data.dropna()
            
            # Example transformation: Convert all column names to lower case
            transformed_data.columns = [col.lower() for col in transformed_data.columns]
            
            print(" CSV Data transformation complete.")
            return transformed_data
        except Exception as e:
            print(f"Error transforming csv data: {e}")
            return None
        
    def transform_json(data):
        try:
            transformed_data = data
            print(" JSON Data transformation complete.")
            return transformed_data
        except Exception as e:
            print(f"Error transforming json data: {e}")
            return None
        
    def transform_sql(data):
        try:
            transformed_data = data
            print(" SQL Data transformation complete.")
            return transformed_data
        except Exception as e:
            print(f"Error transfroming sql data: {e}")
            return None
        