import requests

def download_file_from_google_drive(url, destination):
    """Downloads a file from a Google Drive link to a specified destination.

    Args:
        url (str): The URL of the Google Drive file.
        destination (str): The path where the file should be saved.
    """

    session = requests.Session()
    response = session.get(url, stream=True)

    with open(destination, 'wb') as f:
        for chunk in response.iter_content(chunk_size=128):
            if chunk:  # Filter out keep-alive new chunks
                f.write(chunk)

    print(f"File downloaded successfully to {destination}")

# Example usage:
url = "https://drive.google.com/file/d/YOUR_FILE_ID/view?usp=sharing"
destination = "downloaded_file.jpeg"  # Replace with your desired filename

download_file_from_google_drive(url, destination)