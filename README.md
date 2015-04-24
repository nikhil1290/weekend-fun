## 3637 - weekend-fun API

### Profile
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
		"POC" : "Indiana University",
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

_Only applicable when ```profile_id``` is specified._ 

