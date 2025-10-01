# UIBloatwareRegistry Explorer - Web Interface

A modern, responsive web interface for exploring and searching Android bloatware packages across different device manufacturers.

## Features

- Real-time Search: Instantly search packages by name or description
- Brand Filtering: Filter packages by device manufacturer
- Risk Level Filtering: Filter by risk level (safe, caution, dangerous, unknown)
- Responsive Design: Works seamlessly on desktop, tablet, and mobile
- Modern UI: Clean, intuitive interface with smooth animations

## Development

### Prerequisites

- Node.js 16+ and npm

### Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start development server:
   ```bash
   npm run dev
   ```

3. Open your browser to the URL shown (typically `http://localhost:5173`)

### Building for Production

```bash
npm run build
```

The built files will be in the `dist/` directory.

### Preview Production Build

```bash
npm run preview
```

## Tech Stack

- **React 18**: Modern React with hooks
- **Vite**: Fast build tool and dev server
- **CSS3**: Modern styling with CSS variables
- **GitHub Pages**: Automated deployment

## Data Source

The web interface loads data from `public/data.json`, which is automatically generated from the main `packages_registry.json` file during the GitHub Actions build process.
