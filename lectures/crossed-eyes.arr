use context essentials2021

# CS111 -- Lecture 2
# Extended Code Example on Images
# Kathi Fisler, 2018

# center the eyeball on the base
# overlay puts the first image on top of the second
overlay(circle(15, "solid", "blue"),
  circle(30, "solid", "tan"))

# to save typing, let's name the two pieces
base = circle(30, "solid", "tan")
ball = circle(15, "solid", "blue")

# re-create the centered image using the names
overlay(ball, base)

# sometimes, we want to align on edges instead of center
# overlay-align lets you specify alignment
overlay-align("right", "center", ball, base)

# try overlay-align to move the eyeball to the lower right
overlay-align("right", "bottom", ball, base)
# but this isn't quite right -- we need finer-grained control

# overlay-xy let you adjust relative positions of images.
# it initially aligns the images top-left, then moves the second
#  image to the right and down by the given numbers of pixels
overlay-xy(ball, -25, -25, base)

# if you don't like the negative nums, you can use underlay instead,
#  which puts the first image under the second, still shifting the 
#  second image
underlay-xy(base, 25, 25, ball)

# we have our left-eye image -- let's name it
left-eye = overlay-xy(ball, -25, -25, base)

# put two eyes together
beside(left-eye, left-eye)

# leverage symmetry to avoid writing second eye from scratch
beside(left-eye, flip-horizontal(left-eye))

# if want a frame around the eye, could expand above definition of
#  base (the definition would replace the one up top)
# base = overlay(circle(30, "solid", "tan"), circle(31, "outline", "black"))