## https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_1/ed0d1659290e4afea1d3d13d1da22392/
## varA and varB, are assigned values, either numbers or strings

if (type(varA) == str or type(varB) == str):
  print('string involved')
elif varA > varB:
  print('bigger')
elif varA < varB:
  print('smaller')
elif varA == varB:
  print('equal')
