# 3637 - weekend-fun API
***

## Profile

```
/v1/profile/<int:profile_id>
```

### Resource

```
[
	{ 
		"id" : 1,
	   "name" : "Nikhil",
	   "number" : xxx-xxx-xxxx,
	    "address" : "Indianapolis",
	"company" : "Indiana University",
         "title" : "Test Engineer"
	}
]
```

### Methods

### GET

When ```profile_id``` is specified, returns resources of that particular ```profile```.When ```profile_id``` is omitted, returns the resource of all ```profiles```

### Resource
```
[
	{ 
		"id" : 1,
	   "name" : "Nikhil",
	   "number" : "xxx-xxx-xxxx",
	    "address" : "Indianapolis",
		"company" : "Indiana University",
         "title" : "Test Engineer"
	},
	. . .

    . . .
]
```

### POST

Creates a new ```profile``` and returns that ```resource```.
<table>
<tr>
    <th>Arguments</th>
    <th>Description</th>
	<th> Type </th>
  </tr>
  <tr>
		<td>name</td>
		<td> Name of the person </td>
		<td> String </td> 
 </tr>
<tr>
		<td>number</td>
		<td> Mobile Number </td>
		<td> String </td> 
 </tr>
<tr>
		<td>address</td>
		<td> current residence address </td>
		<td> String </td> 
 </tr>
<tr>
		<td>company</td>
		<td> Name of the company</td>
		<td> String </td> 
 </tr>
<tr>
		<td>title</td>
		<td> Working title</td>
		<td> String </td> 
 </tr>
</table>

### DELETE
_Only applicable when ```profile_id```is specified._ 

## Participants

```
/v1/participants/<int: participant_id>
```

### Resource
```[
  {
	"id" : 25,
	"weekend_id" : 10,
	 "profile_id" : 1,
  }
]
```
### GET
 
Returns single resource when ```id``` is specified. Returns list of all ```participant_ids``` when ```weekend_id``` is specified.Returns ```true``` or ```False``` if both ```weekend_id``` or ```participant_id``` are specified.

### POST
Creates and returns a new resource when ```weekend_id``` and ```profile_id``` are specified.

### DELETE
Applicable when ```participant_id``` is specified or both ```weekend_id``` and ```profile_id``` are specified.

## Expenses

```
/v1/expenses/<int:expense_id>
```

### Resource
```
[
 {
	"id" : 22,
	"weekend_id" : 10,
     "expense_type" : "biryani",
    "quantity" : 2,
    "amount: 25,
	"profie_id" : 1
	"date" : 4/27/2015,
 }
]
```
### GET

Returns single ```expense``` resource when ```id``` is specified. If ```weekend_id``` is specified, returns all the ```expenses``` for that ```weekend```.If both are omitted, returns all the ```expenses``` for all the weekends.

```
[
 {
	"id" : 22,
	"weekend_id" : 10,
     "expense_type" : "biryani",
    "quantity" : 2,
    "amount: 25,
	"profie_id" : 1
	"date" : 4/27/2015,
 },
 . . .

 . . .
]
```

### POST
Creates and returns a new expense resource.

<table>
<tr>
    <th>Arguments</th>
	<th> Type </th>
  </tr>
  <tr>
		<td>weekend_id</td>
		<td> int</td> 
 </tr>
<tr>
		<td>expense_type</td>
		<td> String </td> 
 </tr>
<tr>
		<td>quantity</td>
		<td> float </td> 
 </tr>
<tr>
		<td>amount</td>
		<td>float </td> 
 </tr>
<tr>
		<td>profile_id</td>
		<td> int </td> 
 </tr>
</table>

### DELETE
_Only applicable when ```expense_id``` is specified.


## Weekend

```
/v1/weekend/<int:weekend_id>
```

### Resource
```
[
	{
	"id" : 10
	"week_of" : 4/28/2015,
	"place" : "Columbus",
	"href"  : {
		 "participants" : "http://127.0.0.1:5000/participants/?weekend_id=10",
		  "expenses" :  "http://127.0.0.1:5000/expenses/?weekend_id=10"
		}				
	}
]
```
### GET

When ```weekend_id``` is specified returns a single resource.If it is omitted, returns all the resources.

```
[
	{
	   "id" : 10
		"week_of" : 4/28/2015,
		"place" : "Columbus",
		 "href"  : {
		 	 "participants" : "http://127.0.0.1:5000/participants/?weekend_id=10",
		         "expenses" :  "http://127.0.0.1:5000/expenses/?weekend_id=10"
			}				

	},
	. . .
  
        . . .
]
```

### POST

Creates a new ```weekend``` resource and returns that resource.
<table>
<tr>
    <th>Arguments</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
  <tr>
	<td>week_of</td>
	<td> weekend for the week. </td>
	<td>Date </td> 
 </tr>
<tr>
	<td>Place</td>
	<td>Place of Congress </td>
	<td> String </td> 
 </tr>
</table>

### DELETE
_Only applicable when ```weekend_id``` is specified.
