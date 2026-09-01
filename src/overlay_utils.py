import cv2
import numpy as np

def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size=None):
    """
    Overlays a transparent image onto a background image at the given coordinates.
    """
    bg_img = background_img.copy()
    
    if overlay_size is not None:
        img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)
    
    # Extract the alpha mask of the RGBA image, convert to RGB 
    b, g, r, a = cv2.split(img_to_overlay_t)
    overlay_color = cv2.merge((b, g, r))
    
    # Apply some simple masking 
    mask = cv2.medianBlur(a, 5)
    
    h, w, _ = overlay_color.shape
    roi = bg_img[y:y+h, x:x+w]
    
    # If the overlay is out of bounds, we simply don't draw it (or draw partially).
    # To keep it simple, if it goes out of bounds we'll skip drawing to avoid crash.
    # A more robust solution would slice both the overlay and roi.
    if roi.shape[0] != h or roi.shape[1] != w:
        return bg_img
        
    img1_bg = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(mask))
    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)
    
    bg_img[y:y+h, x:x+w] = cv2.add(img1_bg, img2_fg)
    
    return bg_img
