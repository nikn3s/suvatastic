from math import sqrt

def solve(a, b, c):
    if a == 0:
        exit()
    disc = b**2 - 4 * a * c
    if disc <= 0:
        print("Cant be >=0")
        return "Not real"
    else:
        x1 = (-b + sqrt(disc)) / (2 * a)
        x2 = (-b - sqrt(disc)) / (2 * a)
        return [x1, x2]


def calculateSUVAT(s, u, v, a, t, toFind):

  if toFind not in ['s', 'u', 'v', 'a', 't']:
    exit()

  # Displacement
  if toFind == "s":
    if u != "n" and v != "n" and t != "n":
      u = float(u)
      v = float(v)
      t = float(t)
      s = 0.5 * (v + u) * t
      return s
    elif v != "n" and a != "n" and t != "n":
      v = float(v)
      a = float(a)
      t = float(t)
      s = v * t - 0.5 * a * t**2
      return s
    elif u != "n" and a != "n" and t != "n":
      u = float(u)
      a = float(a)
      t = float(t)
      s = u * t + 0.5 * a * t**2
      return s
    elif v != 'n' and u != 'n' and a != 'n':
      v = float(v)
      u = float(u)
      a = float(a)
      s = (v**2 - u**2) / 2 * a
      return s
    else:
      return 0
  # Initial velocity
  elif toFind == "u":

    if v != 'n' and a != 'n' and t != 'n':
      v = float(v)
      a = float(a)
      t = float(t)
      u = v - a * t
      return u
    elif v != 'n' and a != 'n' and s != 'n':
      v = float(v)
      a = float(a)
      s = float(s)
      u = v - sqrt(v**2 - 2 * a * s)
      return u
    elif s != 'n' and v != 'n' and t != 'n':
      s = float(s)
      v = float(v)
      t = float(t)
      u = (s - 0.5 * v * t) / t
      return u
    elif s != 'n' and a != 'n' and t != 'n':
      s = float(s)
      a = float(a)
      t = float(t)
      u = (s - 0.5 * a * t**2) / t
      return t
  # Final velocity
  elif toFind == 'v':
    if u != 'n' and a != 'n' and t != 'n':
      u = float(u)
      a = float(a)
      t = float(t)
      v = u + a * t
      return v
    elif u != 'n' and a != 'n' and s != 'n':
      u = float(u)
      a = float(a)
      s = float(s)
      v = sqrt(u**2 + 2 * a * s)
      return v
    elif s != 'n' and a != 'n' and t != 'n':
      s = float(s)
      a = float(a)
      t = float(t)
      v = s + 0.5 * a * t**2
      return v
    elif s != 'n' and t != 'n' and u != 'n':
      s = float(s)
      t = float(t)
      u = float(u)
      v = 2 * s / 2 * t - u
      return v

  elif toFind == 'a':

    if v != 'n' and u != 'n' and t != 'n':
      v = float(v)
      u = float(u)
      t = float(t)
      a = (v - u) / t
      return a
    elif v != 'n' and u != 'n' and s != 'n':
      v = float(v)
      u = float(u)
      s = float(s)
      a = (v**2 - u**2) / 2 * s
      return a
    elif u != 'n' and t != 'n' and s != 'n':
      u = float(u)
      t = float(t)
      s = float(s)
      a = 2 * s / t**2 - 2 * u / t
      return a
    elif v != 'n' and t != 'n' and s != 'n':
      v = float(v)
      t = float(t)
      s = float(s)
      a = 2 * s / t**2 - 2 * v / t
      return a

  elif toFind == 't':

    if v != 'n' and u != 'n' and a != 'n':
      v = float(v)
      u = float(u)
      a = float(a)
      t = (v - u) / a
      return t
    elif s != 'n' and u != 'n' and v != 'n':
      s = float(s)
      u = float(u)
      v = float(v)
      t = (2 * s) / (u + v)
      return t
    elif s != 'n' and u != 'n' and a != 'n':
      s = -(float(s))
      u = float(u)
      a = float(a)
      t = solve(0.5 * a, u, s)
      return t
    elif s != 'n' and v != 'n' and a != 'n':
      s = -(float(s))
      v = float(v)
      a = float(a)
      t = solve(0.5 * a, v, s)
      return t