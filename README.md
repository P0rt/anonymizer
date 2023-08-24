# Data Anonymizer

This project provides a Python script to anonymize personal data. It identifies and replaces names, emails, public links, and any personal details with generic IDs, making it easier to handle data without privacy concerns.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/P0rt/anonymizer.git
```
2. Make sure you have Python installed.
3. Navigate to the project directory.

## Usage

1. Place your data in the `data` directory with a filename `sample.json`.
2. Run the anonymization script:
```bash
python anonymizer_script.py
```
3. Find the anonymized data in the `anon` directory named `result.json`.

## Features

- Email detection and replacement.
- URL detection and replacement.
- Mentions (e.g., @username) detection and replacement.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

Please ensure that any changes do not compromise the anonymization process.

## License

[MIT](https://choosealicense.com/licenses/mit/)
