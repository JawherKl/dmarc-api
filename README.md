# CheckDMARC Flask API

This is a Flask application that provides an API to check DMARC records for a given domain. The API can return the results in either JSON or CSV format based on user preference.

## Features

- Check DMARC records for a specified domain.
- Output results in JSON format (default).
- Output results in CSV format if specified.

## Prerequisites

- Python 3.6 or later
- Docker (optional, for running in a container)
- `checkdmarc` library (installed automatically when running the application)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/checkdmarc-flask.git
   cd checkdmarc-flask

2. Install the required Python packages:

   ```bash
    pip install Flask checkdmarc

## Running the Application
### Locally
    python app.py

### Using docker
1. Build Docker image:
    docker build -t checkdmarc-api .

2. Run the Docker container:
    docker run -d -p 5000:5000 --name checkdmarc-api checkdmarc-api

## API Usage
### Endpoint
    `POST /checkdmarc`

### Request Body
    The request should be in JSON format and should include:
        * domain: The domain to check (required).
        * format: The desired response format (json or csv). If not provided, the default is json.

    Example Request:
        For JSON output: 
        ```bash
        {
            "domain": "example.com",
            "format": "json"
        }       
        For CSV output: 
        ```bash
        {
            "domain": "example.com",
            "format": "csv"
        }     

### Response
    The API will return the DMARC check results in the specified format:
        * JSON: A structured JSON response containing the DMARC record details.
        * CSV: A CSV file containing the same details.

    Example JSON Response:
        ```bash
        {
            "domain": "example.com",
            "base_domain": "example.com",
            "dnssec": false,
            "ns": {
                "hostnames": [
                "a.iana-servers.net",
                "b.iana-servers.net"
                ],
                "warnings": []
            },
            "mx": {
                "hosts": [],
                "warnings": [
                "No MX records found. Is the domain parked?"
                ]
            },
            "mta_sts": {
                "valid": false,
                "error": "An MTA-STS DNS record does not exist for this domain"
            },
            "spf": {
                "record": "v=spf1 -all",
                "valid": true,
                "dns_lookups": 0,
                "dns_void_lookups": 0,
                "warnings": [],
                "parsed": {
                "pass": [],
                "neutral": [],
                "softfail": [],
                "fail": [],
                "include": [],
                "redirect": null,
                "exp": null,
                "all": "fail"
                }
            },
            "dmarc": {
                "record": "v=DMARC1;p=reject;sp=reject;adkim=s;aspf=s",
                "valid": true,
                "location": "example.com",
                "warnings": [
                "rua tag (destination for aggregate reports) not found"
                ],
                "tags": {
                "v": {
                    "value": "DMARC1",
                    "explicit": true
                },
                "p": {
                    "value": "reject",
                    "explicit": true
                },
                "sp": {
                    "value": "reject",
                    "explicit": true
                },
                "adkim": {
                    "value": "s",
                    "explicit": true
                },
                "aspf": {
                    "value": "s",
                    "explicit": true
                },
                "fo": {
                    "value": "0",
                    "explicit": false
                },
                "pct": {
                    "value": 100,
                    "explicit": false
                },
                "rf": {
                    "value": "afrf",
                    "explicit": false
                },
                "ri": {
                    "value": 86400,
                    "explicit": false
                }
                }
            },
            "smtp_tls_reporting": {
                "valid": false,
                "error": "An SMTP TLS Reporting DNS record does not exist for this domain"
            }
        }

## Contributing
    Contributions are welcome! Please feel free to submit a pull request or open an issue.

### License
    This project is licensed under 'Jawher Kl'