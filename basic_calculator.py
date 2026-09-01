{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def main():\
    print("=== Stress and Strain Calculator ===")\
    print()\
\
    # Get user inputs and convert to float data types\
    force = float(input("Enter applied force (in Newtons, N): "))\
    area = float(input("Enter cross-sectional area (in square meters, m\'b2): "))\
    original_length = float(input("Enter original length (in meters, m): "))\
    change_in_length = float(input("Enter change in length (in meters, m): "))\
\
    # Perform calculations using arithmetic operators\
    stress = force / area\
    strain = change_in_length / original_length\
\
    # Display inputs and formatted output using f-strings\
    print()\
    print("=== Input Summary ===")\
    print(f"Applied Force (F): \{force:,.2f\} N")\
    print(f"Cross-Sectional Area (A): \{area:,.6f\} m\'b2")\
    print(f"Original Length (L\uc0\u8320 ): \{original_length:,.4f\} m")\
    print(f"Change in Length (\uc0\u916 L): \{change_in_length:,.6f\} m")\
\
    print()\
    print("=== Calculated Results ===")\
    print(f"Stress (\uc0\u963 ): \{stress:,.2f\} Pa")\
    print(f"Strain (\uc0\u949 ): \{strain:,.6f\} (dimensionless)")\
\
if __name__ == "__main__":\
    main()}