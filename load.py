
class Loader:
    def transform(self, transformed_data):
        if transformed_data == "csv":
            return self.transform_csv(transformed_data)
        elif transformed_data == "json":
            return self.transform_json(transformed_data)
        elif transformed_data == "sql":
            return self.transform_sql(transformed_data)
        else:
            print("Unsupported source type")
            return None

    def load_csv(transformed_data, output_file_path):
        try:
            transformed_data.to_csv(output_file_path, index=False)
            print("CSV Data loading complete.")
        except Exception as e:
            print(f"Error loading CSV data: {e}")

    def load_json(transformed_data, output_file_path_json):
        try:
            transformed_data.to_json(output_file_path_json, index=False)
            print(" JSON Data loading complete.")
        except Exception as e:
            print(f"Error loading JSON data: {e}")

# class Loader:
#     def load(self, data, target_type, target):
#         if target_type == "csv":
#             return self.load_csv(data, target)
#         else:
#             print("Unsupported target type")
#             return None
    
#     def load_csv(self, data, file_path):
#         try:
#             data.to_csv(file_path, index=False)
#             print(f"Data successfully written to {file_path}")
#         except Exception as e:
#             print(f"Error writing to CSV {file_path}: {e}")
