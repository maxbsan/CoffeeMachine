# CoffeeMachine
This is a small proyect written in Python. 
It is a simple coffee machine with 5 options:

<ol>
  <li>Espresso</li>
  <li>Latte</li>
  <li>Cappuccino</li>
  <li>Report</li>
  <li>Off</li>
</ol>

## How it works?

<ul>
  <li>When the program starts the user will see a "What would you like" promt and only 3 options: espresso, latte, or cappuccino.</li>
  <li>When the user writes a valid selection it will check first if there are enough resources to prepare the coffee</li>
  <li>If there are enbough resources, it will ask the user how many coins want to insert to pay for the coffee. Otherwise it will return which resource is not enough.</li>
  <li>If the user "inserts" more coins than the total cost, it will return change and then "present" the selected coffee. If not enough money is "inserted" the operation is cancelled and returns to the "make selection" prompt.</li>
  <li>While not shown in the options, if the user types "Report" it will show the current respources available in the machine</li>
  <li>Also not shown, but if the user types "Off", the program will end "turning off the machine".</li>
  <li>If the user types anything else other than these 5 words, the machine will return an error indicating a not valid selection and to try again.</li>
</ul>

### Known bug:
When "inserting" the coins if the user types anything else other than a number, the program will crash. 
