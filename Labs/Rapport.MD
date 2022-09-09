# Ai-rapport

Meningen med denna rapport är att visa hur vi kan förutspå huspriser med hjälp av maskininlärning och metoden linjär regression.


![Image](/assets/AI_model.png)
Första steget är att skapa upp en bild på vilken typ utav data vi behöver.
För detta projektet behöver vi en lista på hur huspriser har sett ut historiskt och information om husen.

Vi kan hämta data ifrån hemsidor med öppna databaser som www.Kaggle.com , filtypen vi är ute efter är comma seperated value <font size=4>**.csv**</font>

<font size=2.5>**. JSON**</font>  är också ett alternativ vi kan använda
Finns inte datan i ett format vi kan jobba i, tillexempel ett textdokument kan vi skriva ett program som letar rätt på väsentlig data och sätter dit kommatecken så att vi kan spara filen som <font size=4>**.csv**</font>


Vi importerar sedan datan in i Python med 
```python
import csv
whit open('house_prices_dataset.csv') as csv_file:
csv_read=csv.reader(csv_file, delimiter=",")
```
Ifall vi inte vill eller har möjlighet att ladda ner all data vi behöver för vårat projekt kan vi behöva importera direkt ifrån en data molntjänst, alternativt så har företaget vi arbetar på en server där våran data lagras.

Det är dags att behandla datan. Vi tar bort onödig data, märker vi tillexempel att antalet frukt träd vid fastigheten har mindre än 1% skillnad på priset kan vi ta bort detta. 

Viktigt att tänka på är också att ta bort extrema avvikelser ifrån datan då det kan ha negativa konsekvenser för våran modell.

Vi behöver också se över ifall vårat dataset saknar kritisk data. Säg att våran <font size=4>**.csv**</font> bara har data ifrån de senaste 10 åren och vi vill se dom senaste 15. Då måste vi hitta mer.  

När det är dags att välja modell är det viktigt att välja rätt algoritm, i detta fallet vet vi att variablerna i datan har ett tydligt samband så vi väljer Linjär regression.

Linjär regression används för att som sagt hitta sambandet mellan ett eller flera inmatningsvariabler (x) och en utdata variabel (y)

Så inmatningsvariabler kan i detta exempel vara:

- Antalet rum

- Geografiskt läge <font size="0.7">(Här är det klokt att dela upp datan mellan positivt och negativt geografisktläge, då bostäder vid havet är mer gynnsamma än de precis vid en motorväg)</font>

- Pris på närliggande hus

![Image](/assets/linear_model.png)
<font size="0.7">Här visualiserar vi datan med hjälp av en grid skapad i matplotlib </font>

Styrkor med modellen är att den är simpel, enkel att läsa och är bra för att hantera variabler som har enkla samband.

Svagheter dyker främst upp ifall sambandet mellan variablerna inte är linjär, modellen är vädligt svag när det finns mycket avvikande data.

Nu när vi har datan vi är ute efter är det dags att driftsätta våran modell så att den kan användas.

Det finns mängdvis med sätt att göra detta så låt oss titta på **Flask web framework**
Vi använder detta sättet då vi vill att modellen ska kunna användas som web-applikation

Första steget är att vi behöver bevara modellen. Detta för att göra modellen enklare för klienten att använda, att träna modellen och faktiskt använda den kräver helt olika resurser utav datorn. Så genom att bevara själva modellen, inte själva inlärningen så förenklar vi programmet.

När vi bevarat modellen kan vi Flask web framework för att skapa en REST API. Då kan vi tillexempel lägga den i molnet. 

Källor: (Spoiler ↓)
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