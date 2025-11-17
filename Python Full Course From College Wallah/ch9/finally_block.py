try:
    file = open("data.txt", "r")
except:
    print("File not found")
finally:
    print("This always runs")
