# ParallelMain.py
from DataProcessor import DataProcessor
from ContentGenerator import ContentGenerator
import multiprocessing

def process_and_generate(data_chunk, keywords, api_key):
    """Process data and generate content in parallel."""
    processor = DataProcessor('')
    filtered_sentences = processor.filter_context_related_sentences(data_chunk, keywords)
    generator = ContentGenerator(api_key)
    return [generator.generate_content(sentence) for sentence in filtered_sentences]

def main():
    csv_file_path = "clean_dataset.csv"
    api_key = "AIzaSyBUG_6Y27wVVMLLTE7LFAD3Fs6NTGje2z0"
    keywords = [["temperature"]]
    processor = DataProcessor(csv_file_path)
    data = processor.process_data_from_csv()

    num_cores = multiprocessing.cpu_count()
    chunk_size = len(data) // num_cores
    data_chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    
    with multiprocessing.Pool(processes=num_cores) as pool:
        args = [(chunk, keywords, api_key) for chunk in data_chunks]
        results = pool.starmap(process_and_generate, args)
    
    combined_results = sum(results, [])
    print("Generated content:", combined_results)

if __name__ == "__main__":
    main()
