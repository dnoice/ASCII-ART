from PIL import Image
import numpy as np

def load_image(source_filename: str) -> np.ndarray:
    """
    Load an image from the given filename and return it as a NumPy array.
    Args:
        source_filename (str): Path to the source image.
    Returns:
        np.ndarray: Image data as a NumPy array.
    """
    try:
        image = Image.open(source_filename)
        return np.asarray(image)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{source_filename}' not found.")
    except Exception as e:
        raise RuntimeError(f"Error loading image: {e}")

def resize_image(image_array: np.ndarray, target_width: int) -> np.ndarray:
    """
    Resize the image proportionally based on the target width.
    Args:
        image_array (np.ndarray): The original image array.
        target_width (int): Desired width for the resized image.
    Returns:
        np.ndarray: Resized image data as a NumPy array.
    """
    aspect_ratio = image_array.shape[0] / image_array.shape[1]
    target_height = int(target_width * aspect_ratio * 0.57)  # Aspect correction factor
    resized_image = Image.fromarray(image_array).resize((target_width, target_height))
    return np.asarray(resized_image).astype("float64")

def normalize_image(image_array: np.ndarray) -> np.ndarray:
    """
    Normalize the image array values to range between 0 and 255.
    Args:
        image_array (np.ndarray): Image data as a NumPy array.
    Returns:
        np.ndarray: Normalized image array.
    """
    return (image_array / np.max(image_array)) * 255

def convert_to_grayscale(image_array: np.ndarray) -> np.ndarray:
    """
    Convert the image array to grayscale.
    Args:
        image_array (np.ndarray): Image data as a NumPy array.
    Returns:
        np.ndarray: Grayscale image data.
    """
    try:
        return np.mean(image_array, axis=2)  # Efficient grayscale conversion
    except ValueError:
        return image_array  # In case it's already grayscale

def generate_ascii_art(gray_image_array: np.ndarray, gray_levels: str) -> str:
    """
    Generate ASCII art from a grayscale image array.
    Args:
        gray_image_array (np.ndarray): Grayscale image data.
        gray_levels (str): String of ASCII characters representing intensity.
    Returns:
        str: Formatted ASCII art as a string.
    """
    ascii_art = ""
    for i in range(gray_image_array.shape[0]):
        for j in range(gray_image_array.shape[1]):
            density_level = int(9 * gray_image_array[i, j] // 255)
            density_level = min(density_level, 8)
            ascii_art += gray_levels[density_level]
        ascii_art += "\n"
    return ascii_art

def save_ascii_art(ascii_art: str, destination_filename: str) -> None:
    """
    Save the generated ASCII art to a text file.
    Args:
        ascii_art (str): The ASCII art string to save.
        destination_filename (str): Path to save the output text file.
    """
    try:
        with open(destination_filename, "w") as dest:
            dest.write(ascii_art)
    except Exception as e:
        raise RuntimeError(f"Error saving ASCII art: {e}")

def main():
    """
    Main function to handle user input and generate ASCII art.
    """
    # File paths
    source_filename = "path_to_your_image"
    destination_filename = "./output.txt"

    # Load and process image
    image_array = load_image(source_filename)

    # Resize logic
    target_width = int(input("Enter desired width: "))
    resized_image = resize_image(image_array, target_width)
    normalized_image = normalize_image(resized_image)
    grayscale_image = convert_to_grayscale(normalized_image)

    # ASCII Art Generation
    gray_levels = ".:-=+*#%@"
    ascii_art = generate_ascii_art(grayscale_image, gray_levels)

    # Display and Save Results
    print(ascii_art)
    save_ascii_art(ascii_art, destination_filename)
    print(f"\n✅ ASCII art successfully saved to '{destination_filename}'")

if __name__ == "__main__":
    main()
    
