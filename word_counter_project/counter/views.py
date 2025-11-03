from django.shortcuts import render
import re

def home(request):
    return render(request, 'counter/home.html')

# Function 1: Count Words
def count_words_logic(text):
    """Counts total number of words in given text."""
    words = re.findall(r'\b\w+\b', text)
    return len(words)

# Function 2: Count Letters
def count_letters_logic(text):
    """Counts total number of alphabetic characters in given text."""
    letters = re.findall(r'[A-Za-z]', text)
    return len(letters)

# Function 3: Main Controller
def count_text(request):
    if request.method != 'POST':
        return render(request, 'counter/home.html', {'error': 'Please submit text using the form.'})

    text = request.POST.get('text', '').strip()
    count_type = request.POST.get('count_type', 'words')  # ✅ Fixed name match

    if not text:
        return render(request, 'counter/result.html', {
            'text': '',
            'result': 0,
            'message': 'No text provided.'
        })

    # ✅ Decide which counting logic to use
    if count_type == 'letters':
        result = count_letters_logic(text)
        message = "Total Letters Counted"
    else:
        result = count_words_logic(text)
        message = "Total Words Counted"

    return render(request, 'counter/result.html', {
        'text': text,
        'result': result,
        'message': message,
        'count_type': count_type,
    })
