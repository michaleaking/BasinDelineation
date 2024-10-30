import matplotlib.pyplot as plt 

def draw_perpendicular_line(x, y, u, v, length=0.1):
    """
    Draws a line perpendicular to the velocity field at a given point (x, y). 
    
    Args:
        x: x-coordinate of the point.
        y: y-coordinate of the point.
        u: x-component of the velocity field at (x, y).
        v: y-component of the velocity field at (x, y).
        length: Length of the perpendicular line to draw. 
    """
    # Calculate the perpendicular vector by swapping components and negating one
    perp_u = -v
    perp_v = u
    
    # Normalize the perpendicular vector
    mag = (perp_u**2 + perp_v**2)**0.5
    perp_u /= mag
    perp_v /= mag
    
    # Calculate the end points of the perpendicular line
    x_end1 = x - length * perp_u / 2
    y_end1 = y - length * perp_v / 2
    x_end2 = x + length * perp_u / 2
    y_end2 = y + length * perp_v / 2
    
    # Plot the line 
    plt.plot([x_end1, x_end2], [y_end1, y_end2], 'r', linewidth=1) 

# Example usage:
x, y = [0, 1, 2], [0, 1, 0]
u, v = [1, 0, -1], [0, 1, 0]  # Sample velocity field

for i in range(len(x)):
    draw_perpendicular_line(x[i], y[i], u[i], v[i])
    
plt.show()
