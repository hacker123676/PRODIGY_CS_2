from PIL import Image
import numpy as np

def load_image(image_path):
    print(f"Loading image from {image_path}")
    try:
        image = Image.open(image_path)
        print("Image loaded successfully")
        return image
    except Exception as e:
        print(f"Failed to load image: {e}")
        return None

def save_image(image, output_path):
    print(f"Saving image to {output_path}")
    try:
        image.save(output_path)
        print("Image saved successfully")
    except Exception as e:
        print(f"Failed to save image: {e}")

def encrypt_image(image, key):
    print("Encrypting image")
    try:
        pixels = np.array(image)
        encrypted_pixels = pixels ^ key  # XOR operation with the key
        encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
        print("Image encrypted successfully")
        return encrypted_image
    except Exception as e:
        print(f"Failed to encrypt image: {e}")
        return None

def decrypt_image(encrypted_image, key):
    print("Decrypting image")
    try:
        encrypted_pixels = np.array(encrypted_image)
        decrypted_pixels = encrypted_pixels ^ key  # XOR operation with the key
        decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
        print("Image decrypted successfully")
        return decrypted_image
    except Exception as e:
        print(f"Failed to decrypt image: {e}")
        return None

def main():
    image_path = 'input_image.png'
    encrypted_image_path = 'encrypted_image.png'
    decrypted_image_path = 'decrypted_image.png'
    key = 42  # This is the key for XOR operation. You can use any integer value.

    # Load the image
    image = load_image(image_path)
    if image is None:
        return

    # Encrypt the image
    encrypted_image = encrypt_image(image, key)
    if encrypted_image is not None:
        save_image(encrypted_image, encrypted_image_path)
        print(f'Image encrypted and saved as {encrypted_image_path}')
    else:
        print("Encryption failed")

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key)
    if decrypted_image is not None:
        save_image(decrypted_image, decrypted_image_path)
        print(f'Image decrypted and saved as {decrypted_image_path}')
    else:
        print("Decryption failed")

if __name__ == "__main__":
    main()
