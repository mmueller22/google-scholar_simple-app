# Product Requirements Document: Scholar Web App

## Overview
Transform the existing Google Scholar command-line tool into a self-hosted web application using Streamlit and Docker.

## Goals
- Provide a user-friendly web interface for Google Scholar searches
- Enable easy deployment via Docker
- Maintain all existing functionality from the CLI tool

## Features

### Core Functionality
- **Search Interface**: Web form with fields for author, keywords, publication, year range
- **Results Display**: Clean table/card view showing title, authors, citations, PDF links
- **Export Options**: Download results as CSV, BibTeX, or plain text
- **Advanced Search**: Support for phrase matching, exclusions, patents/citations toggle

### Technical Features
- **Docker Container**: Single container with all dependencies
- **Persistent Storage**: Save search history and exported files
- **Rate Limiting**: Built-in delays to respect Google Scholar's limits
- **Cookie Management**: Session persistence for higher query limits

## User Interface
- Simple single-page app with search form at top
- Real-time search results below form
- Export buttons for each result format
- Search history sidebar (optional)

## Technical Stack
- **Frontend**: Streamlit
- **Backend**: Enhanced scholar.py module
- **Container**: Docker with Python 3.9+
- **Dependencies**: BeautifulSoup4, Streamlit, Pandas

## Success Metrics
- Users can perform searches without command-line knowledge
- All CLI functionality accessible via web interface
- Single-command deployment via `docker run`
- Search results match CLI tool output

## Out of Scope
- User authentication/multi-tenancy
- Database storage
- Advanced analytics/visualization
- Mobile optimization
