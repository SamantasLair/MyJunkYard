from manim import *


class EuclidianAlgorithm(Scene):
  def construct(self):
    m1 = 726
    n1 = 122
    r1 = m1 % n1
    a1 = m1//n1
    # Create initial Text objects
    mt = Text(str(m1), color=BLUE)
    nt = Text(str(n1), color=RED)
    rt = Text(str(r1), color=GREEN)
    at = Text(str(a1), color=YELLOW)
    equal = Text(" = ")
    times = Text(" * ")
    plus = Text(" + ")
    # Combine initial Text objects into a VGroup
    full = VGroup(mt, equal, nt, times, at,plus,rt).arrange(buff=0.5)

    self.play(Write(full))
    self.wait(1)

    m = m1
    n = n1
    r = m % n

    while r != 0:
      # Update variables for the next iteration
      m = n
      n = r
      r = m % n
      a = m//n

      # Create new Text objects with updated values
      mte = Text(str(m), color=BLUE)
      nte = Text(str(n), color=RED)
      rte = Text(str(r), color=GREEN)
      ate = Text(str(a), color=YELLOW)
      # Combine the new Text objects into a VGroup with the same arrangement
      new_full = VGroup(mte, equal, nte, times, ate,plus,rte).arrange(buff=0.5)

      # Use FadeTransform on submobjects to avoid collapsing
      self.play(FadeTransform(full, new_full))
      self.wait(1)

      # Update the original VGroup (`full`) with the new Text objects
      full = new_full

    self.play(FadeOut(full))
    self.play(Transform(full, Text(f'FPB dari ({m1},{n1}) adalah {n}')))
    self.wait(3)
