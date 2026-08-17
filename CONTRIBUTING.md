# Contributing Guide

Thank you for contributing to the Enterprise AI Document Intelligence Pipeline. This project values small, reviewable changes, readable code, and reliable data-pipeline behavior.

## Local setup

```bash
git clone https://github.com/archana24v-web/enterprise-ai-document-intelligence-pipeline.git
cd enterprise-ai-document-intelligence-pipeline
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
pip install -r requirements.txt
```

## Development workflow

1. Create a branch with a clear name, such as `feat/add-metadata-filtering`.
2. Keep each change focused on one problem.
3. Add or update tests when changing pipeline behavior.
4. Run the test suite before opening a pull request.
5. Write a commit message that explains the intent of the change.

## Run tests

```bash
pytest -q
```

GitHub Actions also runs this test suite automatically for pushes and pull requests.

## Code guidelines

- Keep ingestion, transformation, validation, and storage concerns separated.
- Do not commit secrets, API keys, virtual environments, or generated vector-store files.
- Use clear function names and type hints for public functions.
- Prefer small, testable functions over large multi-purpose functions.
- Update the README or architecture documentation when behavior changes.

## Pull-request checklist

- [ ] The change has a focused purpose.
- [ ] Tests pass locally.
- [ ] No credentials or private documents are included.
- [ ] Documentation reflects the change.
- [ ] The pull-request description explains the problem and solution.
