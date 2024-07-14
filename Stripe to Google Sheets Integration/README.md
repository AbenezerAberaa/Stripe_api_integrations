# Stripe to Google Sheets Integration

This project aims to develop a system that retrieves data from a user's Stripe account using the Stripe API and writes it to a Google Sheet in a tabular format. By integrating Stripe and Google Sheets, users can conveniently manage and analyze their Stripe transactions within a familiar spreadsheet environment. The system will authenticate users, retrieve Stripe data using the Stripe API, and utilize the Google Sheets API to update the user's Google Sheet. It will provide data synchronization, error handling, configuration options, and a user-friendly interface for seamless management of Stripe data.

## Table of Contents

- [Installation](#installation)
- [SetupGoogle](#SetupGoogle)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   git clone https://github.com/AbenezerAberaa/Stripe_api_integration

2. Navigate to the project directory:

   cd Stripe_api_integration

3. Install the dependencies:
   pip install -r requirements.txt

## SetupGoogle

    1. Go to the Google Cloud Console: <https://console.cloud.google.com/>.
    2. Create a new project or select an existing project.
    3. Enable the Google Sheets API for your project:
        Click on the "Navigation menu" (☰) in the upper-left corner.
        Go to "APIs & Services" > "Library".
        Search for "Google Sheets API" and select it.
        Click on the "Enable" button.
    4. Set up Service Account credentials:
          Click on the "Navigation menu" (☰) in the upper-left corner.
          Navigate to the "APIs & Services" section and click on "Credentials."
          Click on the "Create Credentials" button and select "Service Account" from the dropdown menu.
          Provide a name for the service account and optionally add a description.
          Click on the "Create" button.
          On the "Service account permissions" page, click on the "Continue" button.
          On the "Grant this service account access to project" page, select the "Editor" role from the dropdown menu.
              The "Editor" role provides full access to the project, including the ability to manage and modify Google Sheets.
          Click on the "Done" button to create the service account. The service account will be created.
          Click on the service account you created.
          In the "Service account details" page, go to the "Keys" section and click on "Add key" -> "Create key".
          Select the key type JSON and click on the "Create" button.
          The service account key file will be downloaded to your device.
          The service account credentials JSON file will be downloaded to your device.
          Rename the downloaded JSON file to credentials.json.

    5. Move the credentials.json file to the same directory as your main.py file.

    6. Enable API access to the Google Sheet, please follow these steps:

        Copy the service email provided for the API integration.

        Open the Google Sheet you want to grant API access to.

        Click on the "Share" button in the top-right corner of the Google Sheet.

        In the "People" field, paste the service email you copied in Step 1.

        Set the access permission to "Editor" for the service email.

        Click the "Send" button to share the Google Sheet with the service email.

## Usage

    1. Open the main.py file in a text editor.

    2. In the if __name__=="__main__": block, you will find the following lines:

        ```if __name__=="__main__":
            api_key=""
            sheet_url=""
            main(api_key, sheet_url)
        ```
    3. Replace the empty strings api_key="" and sheet_url="" with your Stripe API key and Google Sheet URL,  respectively.

        ```if __name__=="__main__":
            api_key="your_stripe_api_key"
            sheet_url="your_google_sheet_url"
            main(api_key, sheet_url)
        ```
        Make sure to wrap the values with quotes and provide the actual API key and URL.

    4. Save the main.py file.

    5. Run the script:
       python main.py

    The script will use the provided API key and Google Sheet URL to perform the necessary operations.
