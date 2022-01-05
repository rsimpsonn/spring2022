SCOOP-SIZE = 15

cone = flip-vertical(triangle(SCOOP-SIZE * 2, "solid", "tan"))

overlay-xy(circle(SCOOP-SIZE, "solid", "pink"),
  0, 25,
  overlay-xy(circle(SCOOP-SIZE, "solid", "green"),
    0, 25,
    cone))