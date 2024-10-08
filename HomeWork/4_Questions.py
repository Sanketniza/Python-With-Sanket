
def clean_text(text):
    # Step 1: Define a simple list of common stopwords
    stop_words = ["is", "and", "the", "a", "it", "contains", "some"]

    # Step 2: Remove punctuation from the text
    text = text.replace(",", "").replace(".", "")  # Simple punctuation removal

    # Step 3: Split the text into words
    words = text.split()

    # Step 4: Remove stopwords from the list of words
    cleaned_words = [word for word in words if word.lower() not in stop_words]

    # Step 5: Join the cleaned words back into a single string
    cleaned_text = ' '.join(cleaned_words)

    return cleaned_text

# Example usage
input_text = "This is a sample text, and it contains some common stopwords."
cleaned_text = clean_text(input_text)
print("Cleaned Text:", cleaned_text)