import spacy

from .models import Phone, Network
from django.db.models import TextField, IntegerField, CharField

nlp = spacy.load("en_core_web_md")

def parse_models(instance):
    data = []

    # Iterate over all fields in the model
    for field in instance._meta.fields:
        value = getattr(instance, field.name)
        # Check if the field is a TextField
        if isinstance(field, TextField) and value:
            data.append(value)
        # concatenate field name and value otherwise
        else:
            data.append(f"{field.verbose_name}: {value}")
            
    # Return concatenated string of all TextField values
    return ' '.join(data)


def get_most_relevant(prompt, top_n=3):
 
    prompt_doc = nlp(prompt)

    # Iterate over each entry in the database
    similarities = []
    combined = list(Phone.objects.all()) + list(Network.objects.all())
    for entry in combined:
        text_data = parse_models(entry)
        entry_doc = nlp(text_data)  
        similarity = prompt_doc.similarity(entry_doc)
        similarities.append((entry, similarity))

    # Sort by similarity 
    sorted_entries = sorted(similarities, key=lambda x: x[1], reverse=True)
    return [entry[0] for entry in sorted_entries[:top_n]]


# relevant_entries = get_most_relevant("Your prompt here")