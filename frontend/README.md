# Tapin Frontend

## Setup

1. Install dependencies:
	```sh
	cd frontend
	npm install
	```
2. Start the development server:
    ```sh
    npm run dev
    ```

## Configuration

- API base URL is configurable via Vite env:
  - Create `.env` in `frontend/` and set:
    ```
    VITE_API_BASE=http://127.0.0.1:5000
    ```
  - Defaults to `http://127.0.0.1:5000` if unset.

## TODO
- Implement authentication and listings UI
- Integrate map for listing locations
- Apply design system and ensure responsiveness
