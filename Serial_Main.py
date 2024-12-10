# SerialMain.py
from DataProcessor import DataProcessor
from ContentGenerator import ContentGenerator

def main():
    csv_file_path = "clean_dataset.csv"
    api_key = "AIzaSyBUG_6Y27wVVMLLTE7LFAD3Fs6NTGje2z0"
    keywords = [["temperature"]]

    processor = DataProcessor(csv_file_path)
    data = processor.process_data_from_csv()
    filtered_data = processor.filter_context_related_sentences(data, keywords)

    generator = ContentGenerator(api_key)
    generated_content = [generator.generate_content(sentence) for sentence in filtered_data]
    
    print("Generated content:", generated_content)

if __name__ == "__main__":
    main()
