# Backend Code Generation Rules

## Must Follow

- Use FastAPI
- Use Pydantic v2
- Use SQLAlchemy 2.x
- Use PostgreSQL

## Architecture

Follow Clean Architecture

layers:

- api
- service
- repository
- domain

## Output

Must follow backend_codegen.schema.json

Do not output markdown.

Do not output explanations.

Output valid JSON only.