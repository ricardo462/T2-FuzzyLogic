# T2-FuzzyLogic
This is the implementation of the a Decision Support System (DSS) for the selection of a basketball team. There
were considered three caracteristics:
- Efectiveness: number of baskets of 25 attemps
- Height: in cm
- Speed: time on run 100 metres in seconds

These caracteristics are combined by the following rules:
- Rule 1: Efectiveness and Height (0.8)
- Rule 2: Efectiveness and Speed (0.95)
- Rule 3: Height and Speed (0.75)

In order to run the DSS, you have to run the file "main.py", where you can evaluate a player introducing its name, efectiveness, height and speed. Furthermore, you can choice among these methods to combine rules:

- Max(a,b)
- Sum-Product(a,b) = a+b-a*b
- Lukasiewicz(a,b) = min(a+b, 1)
- Drastic-sum(a,b) = a if b=0, b if a=0 and 1 otherwise


After introducing players you can compare them running the script "exporting.py", and if you want to compare your results using the rest of the methods you can run the file "testing_methods.py".