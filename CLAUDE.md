# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple image gallery website that displays a collection of images with a lightbox feature. The project consists of:

- `Index.html`: The main webpage with HTML, CSS, and JavaScript for the image gallery
- `thumbnailer.py`: A Python script to generate thumbnails from original images
- `Images/`: Directory containing the original images displayed in the gallery
- `thumbnails/`: Directory containing generated thumbnail versions of the images

## Development Commands

### Running the Website

To view the website locally, you can open the Index.html file in a web browser:

```bash
# On macOS
open Index.html

# Or use a local server if preferred
python -m http.server
# Then visit http://localhost:8000 in your browser
```

### Generating Thumbnails

To generate thumbnails from images, run the thumbnailer.py script:

```bash
# Make sure you have the Pillow library installed
pip install Pillow

# Run the script
python thumbnailer.py
```

## Project Structure

The website has a simple architecture:

1. **Gallery Interface**: The HTML file displays a grid of image thumbnails with CSS styling
2. **Lightbox Functionality**: JavaScript adds interactivity, allowing users to:
   - Click thumbnails to view larger images
   - Navigate between images with arrow buttons or keyboard keys
   - Close the lightbox by clicking outside or pressing Escape
3. **Image Processing**: The Python script creates optimized thumbnails from the original images

## Technical Implementation

- **Gallery Layout**: Uses CSS Grid for a responsive grid layout of thumbnails
- **Image Management**: 
  - Thumbnails are stored in the `thumbnails/` directory (220×160px)
  - Full-size images are stored in the `Images/` directory
- **JavaScript Functionality**:
  - Images are stored in a 2D array with paths to full images and thumbnails
  - Captions are automatically generated from filenames using the `makeCaption()` function
  - Event listeners handle clicks, keyboard navigation, and lightbox display
  - Navigation is circular (wraps from last to first image and vice versa)

## Current Status

- The site is configured to display thumbnail images from the 'thumbnails' directory
- When a thumbnail is clicked, the lightbox displays full-size images from the 'Images' directory
- The thumbnail dimensions are set to 220×160px in both the CSS and Python script
- The thumbnails have been generated and are ready for use

## Adding New Images

To add new images to the gallery:

1. Add the full-size image to the `Images/` directory
2. Run the thumbnailer script to generate a thumbnail:
   ```bash
   python thumbnailer.py
   ```
3. Update the `images` array in the JavaScript section of `Index.html` to include the new image:
   ```javascript
   ["Images/new_image_filename.png", "thumbnails/new_image_filename.png"],
   ```

## Modifying the Gallery Appearance

- Thumbnail size and grid layout can be adjusted in the CSS under `.gallery` and `.thumb img`
- Lightbox appearance can be modified in the CSS under `.lightbox` selectors
- Color scheme and typography can be changed in the CSS at the top of the file