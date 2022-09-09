# Ai-rapport

Meningen med denna rapport är att visa hur vi kan förutspå huspriser med hjälp av maskininlärning och metoden linjär regression.


![Image](/assets/AI_model.png)

<font size=2>Första steget är att skapa upp en bild på vilken typ utav data vi behöver.
För detta projekt behöver vi en data set som visar hur huspriser har sett ut historiskt samt attribut om husen i sig.</font>

Vi kan hämta data ifrån hemsidor med öppna databaser så som www.Kaggle.com 

Filtypen vi är ute efter är comma seperated value <font size=4>**.csv**</font>

<font size=2.5>**. JSON**</font>  är ett alternativ som kan användas.
Finns inte datan i de format vi kan jobba i, tillexempel textdokument kan vi skriva ett program som letar rätt på väsentlig data och sätter dit kommatecken så att filen kan sparas som <font size=4>**.csv**</font>


Sedan importeras datan in i Python med 
```python
import csv
whit open('house_prices_dataset.csv') as csv_file:
csv_read=csv.reader(csv_file, delimiter=",")
```
Ifall man inte vill eller har möjlighet att ladda ner samtlig data man är i behov utav för projektet kan man istället behöva importera direkt ifrån en data molntjänst, alternativt har företaget vi arbetar på en server där vår data lagras.

Det är dags att behandla datan. 
Vi tar bort onödig data, märker man tillexempel att antalet fruktträd vid fastigheten har mindre än 1% skillnad på slutpriset är detta en onödig datapunkt. 

Viktigt att tänka på är även att ta bort extrema avvikelser ifrån datan då det kan ha negativa konsekvenser för vår modell.

Vi behöver även se över ifall vårat data-set saknar kritisk data. Säg att våran <font size=4>**.csv**</font> bara har data ifrån de senaste 10 åren och vi vill se dom senaste 15. Då måste vi leta upp mer data kring de år vi saknar.  

När det är dags att välja modell är det viktigt att vi välja rätt algoritm, i detta fallet vet man att variablerna i datan har ett tydligt samband så vi väljer Linjär regression i detta fall.

Linjär regression används som tidigare nämnt för att finna sambandet mellan ett eller flera inmatningsvariabler (x) samt en utdata variabel (y)

Så inmatningsvariabler kan i detta exempel vara:

- Antalet rum

- Geografiskt läge <font size="0.7">(Här är det klokt att dela upp datan mellan positivt och negativt geografisktläge, då bostäder vid havet är mer gynnsamma än de belägna vid en motorväg)</font>

- Pris på närliggande hus

![Image](/assets/linear_model.png)
<font size="0.7">Här visualiserar vi datan med hjälp av en grid skapad i matplotlib </font>

Styrkorna med denna modell är att den är simpel, enkel att läsa samt bra för att hantera variabler som har enkla samband.

Svagheter med modellen dyker främst upp ifall sambandet mellan variablerna inte är linjär, modellen är svag när det finns mycket avvikande data.

Nu när vi har datan man är ute efter är det dags att driftsätta våran modell så att den kan användas i praktiken.

Det finns mängdvis med sätt att göra detta på, men låt oss titta på **Flask web framework**
Man använder detta sätt så att modellen kan användas som en web-applikation.

Första steget är att man behöver bevara modellen. 
Detta gör vi för att modellen enklare ska kunna nyttjas på ett enkelt sätt av användaren, att träna modellen och faktiskt använda den kräver helt olika resurser utav datorn. Så genom att bevara själva modellen, inte själva inlärningen så förenklas programmet.

När vi bevarat modellen kan vi med hjälp av Flask web framework skapa en REST API. 
Då kan vi tillexempel lägga den i molnet. 

Källor:
>! 
Dataset:
https://www.kaggle.com/datasets/lespin/house-prices-dataset
Linearregression
https://science.nu/courses/regression-att-prediktera-och-inferera-fran-data/lektion/linjar-regression-regressionsanalys-och-korrelation/ 
Preparedata
https://machinelearningmastery.com/how-to-prepare-data-for-machine-learning/
Plotting Linear Regression
https://www.tutorialspoint.com/linear-regression-with-matplotlib-numpy
Deploying Models
https://towardsdatascience.com/3-ways-to-deploy-machine-learning-models-in-production-cdba15b00e 
Hands-On Unsupervised Learning Using Python - Ankur A. Patel - Oreilly Media