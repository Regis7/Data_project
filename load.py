def load(data, output_file_path):
    try:
        data.to_csv(output_file_path, index=False)
        print("Data loading complete.")
    except Exception as e:
        print(f"Error loading data: {e}")

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
