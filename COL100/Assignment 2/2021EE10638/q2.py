circle_radius=float(input())
square_side=float(input())
rectangle_length=float(input())
rectangle_breadth=float(input())
parallelogram_base=float(input())
parallelogram_height=float(input())
trapezium_p1=float(input())
trapezium_p2=float(input())
trapezium_height=float(input())
pi=3.14
print(f"{pi*(circle_radius**2):.2f}",f"{square_side**2:.2f}", f"{rectangle_breadth*rectangle_length:.2f}", f"{parallelogram_base*parallelogram_height:.2f}", f"{trapezium_height*((trapezium_p1+trapezium_p2)/2):.2f}", sep='\n')

