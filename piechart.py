import pygal
piechart=pygal.Pie()

piechart.title='TB IN STATES OF INDIA'
piechart.add('Delhi',36)
piechart.add('Gujarat',64)
piechart.add('Haryana',51)
piechart.add('Madhya Pradesh',49)
piechart.add('Uttar Pradesh',56)
piechart.add('West Bengal',60)
piechart.add('Orissa',54)
piechart.add('kerala',55)

piechart.render()
