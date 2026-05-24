import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.animation import FuncAnimation

def update_clock(frame):
    # Clear previous hands
    ax.clear()
    
    # Clock face
    circle = plt.Circle((0, 0), 1, color='white', ec='black', lw=12)
    ax.add_patch(circle)
    
    # Hour marks
    for i in range(12):
        angle = np.deg2rad(i * 30)
        x1 = 0.88 * np.cos(angle)
        y1 = 0.88 * np.sin(angle)
        x2 = 1.0 * np.cos(angle)
        y2 = 1.0 * np.sin(angle)
        ax.plot([x1, x2], [y1, y2], color='black', lw=6)
    
    # Numbers
    for i in range(1, 13):
        angle = np.deg2rad(i * 30 - 90)
        x = 0.72 * np.cos(angle)
        y = 0.72 * np.sin(angle)
        ax.text(x, y, str(i), ha='center', va='center', fontsize=18, fontweight='bold')
    
    # Current time
    now = datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second
    microsecond = now.microsecond
    
    # Smooth second hand movement
    total_seconds = second + microsecond / 1_000_000
    
    # Calculate angles
    hour_angle = np.deg2rad((hour + minute/60 + total_seconds/3600) * 30 - 90)
    min_angle  = np.deg2rad((minute + total_seconds/60) * 6 - 90)
    sec_angle  = np.deg2rad(total_seconds * 6 - 90)
    
    # Hour hand
    ax.plot([0, 0.5 * np.cos(hour_angle)], 
            [0, 0.5 * np.sin(hour_angle)], 
            color='black', lw=10, solid_capstyle='round')
    
    # Minute hand
    ax.plot([0, 0.78 * np.cos(min_angle)], 
            [0, 0.78 * np.sin(min_angle)], 
            color='black', lw=6, solid_capstyle='round')
    
    # Second hand
    ax.plot([0, 0.85 * np.cos(sec_angle)], 
            [0, 0.85 * np.sin(sec_angle)], 
            color='red', lw=2.5, solid_capstyle='round')
    
    # Center dot
    ax.plot(0, 0, 'o', color='darkred', markersize=18)
    ax.plot(0, 0, 'o', color='gold', markersize=10)
    
    # Title with live time
    ax.set_title(f"Live Wall Clock — {now.strftime('%I:%M:%S %p')}", 
                 fontsize=20, pad=20)
    
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')

# Create figure
fig, ax = plt.subplots(figsize=(9, 9))
fig.patch.set_facecolor('#f0f0f0')

# Create animation (updates every 200ms for smooth feel)
ani = FuncAnimation(fig, update_clock, interval=200, cache_frame_data=False)

plt.tight_layout()
plt.show()