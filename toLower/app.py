import csv
import os
import logging
import sys

# Configure the logger
log_dir = '/data/logs'
log_filename = 'app.log'
log_path = os.path.join(log_dir, log_filename)

logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

incoming_dir = '/data/processed'
processed_dir = '/data/outgoing'

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
                        processed_row = [cell.lower() for cell in row]
                        writer.writerow(processed_row)

            logging.info(f"Processed file: {input_file}")
        except FileNotFoundError:
            logging.error(f"CSV file not found at: {input_file}")
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

logging.shutdown()
sys.exit(0)
