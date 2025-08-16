from PIL import Image
import pytesseract

# Ensure Tesseract is installed and specify the path to the executable if necessary
# Example for Windows:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """
    Extracts text from the given image using Tesseract OCR.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: The text extracted from the image.
    """
    try:
        # Open the image file
        image = Image.open(image_path)
        # Use Tesseract to extract text
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    image_path = "C:\\Users\\pradn\\OneDrive\\Desktop\\tesseract.png"  # Replace with your image path
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:")
    print(extracted_text)
