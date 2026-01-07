inner_radius = 22.5 / 2   # 7.5
outer_radius = 37.5 / 2   # 12.5
start_angle = 30
end_angle = 180

def sector(radius, start_angle, end_angle, num_points=100):
    theta = np.linspace(np.radians(start_angle), np.radians(end_angle), num_points)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return x, y

fig, ax = plt.subplots()
ax.set_aspect('equal')

x_outer, y_outer = sector(outer_radius, start_angle, end_angle)
x_inner, y_inner = sector(inner_radius, start_angle, end_angle)

mask_outer = (x_outer >= -20) & (x_outer <= 20)
mask_inner = (x_inner >= -20) & (x_inner <= 20)

x_outer_masked = x_outer[mask_outer]
y_outer_masked = y_outer[mask_outer]
x_inner_masked = x_inner[mask_inner]
y_inner_masked = y_inner[mask_inner]

ax.fill_between(x_outer_masked, y_outer_masked, color='blue', alpha=0.7)
ax.fill_between(x_inner_masked, y_inner_masked, color='white', zorder=5)

ax.set_xlim(-20, 20)
ax.set_ylim(min(y_outer_masked.min(), y_inner_masked.min()),
            max(y_outer_masked.max(), y_inner_masked.max()))

area_outer = simps(y_outer_masked, x_outer_masked)
area_inner = simps(y_inner_masked, x_inner_masked)

plt.axis('off')
plt.title("Area Swiped by Wind Screen Wiper for Given Conditions")

shaded_area_cm2 = shaded_area * 100
print(f"Area Swiped by Wind Screen Wiper for Given Conditions: {shaded_area_cm2:.2f} cm²")