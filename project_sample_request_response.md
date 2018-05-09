# trainX Autonomous Vechicle Schedule Optimization API

## Request 

```
{ "trainXRequest": {
"version": "1.0",
"originLocation": {
  "address": "4160  Cass Ave Suite B Detroit, MI 48201"
},
"calendar": [
        {
            "title": "Beyond Juicery",
            "address": "2501 Russell St, Detroit, MI 48207",
            "date": "05/08/2018",
            "planned_arrival":"08:30am",
            "planned_departure":"08:45am"
          },
          { 
            "title": "Kuzzo's Chicken and Whaffles",
            "address": "19345 Livernois Ave, Detroit, MI 48221",
            "date": "05/08/2018",
            "planned_arrival": "10:30am",
            "planned_departure": "11:30am"
          },
          { 
            "title": "Wholefoods",
            "address": "115 Mack Ave, Detroit, MI 48201",
            "date": "05/08/2018",
            "planned_arrival": "05:30pm",
            "planned_departure": "06:15pm"
          }
        
]
}
}
```


## Response

```
{ "trainXResponse": {
"version": "1.0",
"originLocation": {
  "address": "4160  Cass Ave Suite B Detroit, MI 48201"
},
"calendar": [
        {
            "title": "Beyond Juicery",
            "address": "2501 Russell St, Detroit, MI 48207",
            "date": "05/08/2018",
            "planned_arrival":"08:30am",
            "planned_departure":"08:45am",
            "recommended_arrival": "09:00am",
            "recommended_departure:" "09:15am"
          },
          { 
            "title": "Kuzzo's Chicken and Whaffles",
            "address": "19345 Livernois Ave, Detroit, MI 48221",
            "date": "05/08/2018",
            "planned_arrival": "10:30am",
            "planned_departure": "11:30am",
            "recommended_arrival": "02:00pm",
            "recommended_departure:" "03:30pm"
          },
          { 
            "title": "Wholefoods",
            "address": "115 Mack Ave, Detroit, MI 48201",
            "date": "05/08/2018",
            "planned_arrival": "05:30pm",
            "planned_departure": "06:15pm"
            "recommended_arrival": "09:00pm",
            "recommended_departure:" "10:00pm"
          }
        
]
}
}
```
