import csv
import os

incoming_dir = '/data/incoming'
processed_dir = '/data/processed'

for filename in os.listdir(incoming_dir):
    if filename.endswith('.csv'):
        input_file = os.path.join(incoming_dir, filename)
        output_file = os.path.join(processed_dir, filename)

        try:
            with open(input_file, 'r') as csv_file:
                reader = csv.reader(csv_file)

                with open(output_file, 'w') as processed_csv:
                    writer = csv.writer(processed_csv)
                    for row in reader:
                        processed_row = [cell.upper() for cell in row]
                        writer.writerow(processed_row)

        except FileNotFoundError:
            print(f"CSV file not found at: {input_file}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
