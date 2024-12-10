# DataProcessor.py
import csv
import spacy

class DataProcessor:
    """Processes data from CSV files and filters sentences based on keywords."""
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.nlp = spacy.load("en_core_web_md")  # Load the SpaCy NLP model once when the class is initialized.

    def process_data_from_csv(self):
        """Extracts unique sentences from a CSV file."""
        seen_sentences = set()
        result = []
        with open(self.file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None)  # Skip header if present
            for row in csv_reader:
                text = row[1]  # Assumes text is in the second column
                sentences = self.get_sentences(text)
                for sentence in sentences:
                    if sentence not in seen_sentences:
                        seen_sentences.add(sentence)
                        result.append(sentence)
        return result

    @staticmethod
    def get_sentences(text):
        """Splits text into a list of sentences."""
        sentences = text.split('. ')
        if sentences and sentences[-1].endswith('.'):
            sentences[-1] = sentences[-1][:-1]
        return sentences

    def filter_context_related_sentences(self, data, keywords):
        """Filters sentences by contextual relevance using the specified keywords."""
        categorized_sentences = [[] for _ in keywords]
        target_tokens_groups = [[self.nlp(keyword) for keyword in group] for group in keywords]
        for sentence in data:
            doc = self.nlp(sentence)
            for group_index, target_tokens in enumerate(target_tokens_groups):
                if any(doc_token.similarity(target_token) > 0.8 for doc_token in doc for target_token in target_tokens):
                    categorized_sentences[group_index].append(sentence)
        return categorized_sentences