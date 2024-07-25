
import load
import extract
import transform

# def main():
#     # File paths

if __name__ == "__main__":

    # ETL process
    # CSV
    input_file_path = 'input_file.csv'
    output_file_path = 'output_file.csv'

    source_type = "csv"
    source = "input_file.csv"

    extracted_csv_data = extract.Extractor.extract_csv(input_file_path)
    extracted_json_data = extract.Extractor.extract_json(file_path)
    if extracted_csv_data is not None:
        transformed_data = transform.Transfoermer.transform_csv(extracted_csv_data)
        if transformed_data is not None:
            load.load(transformed_data, output_file_path)

    elif extracted_json_data is not None:
        transformed_data = transform.Transfoermer.transform_json(extracted_json_data)
        if transformed_data is not None:
            load.load(transformed_data, file_path)

    # JSON

    # source_type = "json"
    # source = "input_file.json"
    # extracted_data = extract.Extractor.extract_json(source_type, source)

    # SQL

    # source_type = "sql"
    # connection_string = "mysql+pymysql://username:password@host/dbname"
    # query = "SELECT * FROM tablename"
    # extracted_data = extract.Extractor.extract_sql(source_type, (connection_string, query))


    

# if __name__ == "__main__":
#     main()

# if __name__ == "__main__":
#     extractor = extract.Extractor()
#     transformer = transform.Transformer()
#     loader = load.Loader()

#     # Example usage for extracting data from CSV
#     source_type = "csv"
#     source = "input_file.csv"
#     extracted_data = extractor.extract(source_type, source)

#     # Example usage for extracting data from JSON
#     # source_type = "json"
#     # source = "input_file.json"
#     # extracted_data = extractor.extract(source_type, source)

#     # Example usage for extracting data from SQL
#     # source_type = "sql"
#     # connection_string = "mysql+pymysql://username:password@host/dbname"
#     # query = "SELECT * FROM tablename"
#     # extracted_data = extractor.extract(source_type, (connection_string, query))
    
#     if extracted_data is not None:
#         # Transform data
#         transformed_data = transformer.filter_rows(extracted_data, "column_name", 50)
        
#         if transformed_data is not None:
#             # Load data
#             target_type = "csv"
#             target = "output_file.csv"
#             loader.load(transformed_data, target_type, target)
