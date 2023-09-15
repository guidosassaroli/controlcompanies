# Contribution Guidelines

You can contribute to this database with issues and pull requests.

## Issues

Issues can be used to ask questions, report errors, or start discussions.  

## Pull Requests

Pull requests can be used to add/edit companies from the list.

### How To Contribute with PRs

The new companies must be added to the `/data` folder using a dedicated file in `_data_structure.json` format.
Subsequently, the `README.md` file is automatically generated, so you don't have to edit it manually.

1. Open `./data` directory
2. Add a new JSON file for the new company (file name should be a slugified version of the company name)
3. File content should respect the following format:

```JSON
{
  "name": "CompanyName",
  "url": "companynamewebsite",
  "headquarter": "City, State",

  "short_description": "Short description of the company with some hints.",
  "tags": [
    "", 
    ""
  ],
  "topic": ""
}

```