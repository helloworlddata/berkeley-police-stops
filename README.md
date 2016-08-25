# Berkeley Police Department Stops


# Todos


- Have derive_dispositions return full data object
- Write script that calls derive_disposition()



# Links


https://data.cityofberkeley.info/Public-Safety/Berkeley-PD-Stop-Data/6e9j-pj9p

https://data.cityofberkeley.info/api/views/6e9j-pj9p/rows.csv?accessType=DOWNLOAD


# Announcement

http://www.ci.berkeley.ca.us/Police/Home/Berkeley_PD_s_Stop_Data_Now_on_City_s_Open_Data_Portal.aspx

> In our desire to be open and accountable to our community, the Berkeley Police Department voluntarily collects and publicly shares demographic stop data.  Collection of data can assist and contribute to the national policing discussion, focus our attention internally on implicit bias and increase trust by making policing in Berkeley more transparent to the community.

> On January 26, 2015 the Berkeley Police Department began collecting information for all vehicle (including bicycles) and pedestrian detentions (up to five persons).  This stop data is now available for public viewing on the City of Berkeley's Open Data Portal which can be accessed at https://data.cityofberkeley.info/Public-Safety/Stop-Data/6e9j-pj9p. The police detention categories on the Open Data Portal are traffic, suspicious vehicles, pedestrian and bicycle stops.  You will also find information on the incident number, date, time, location, and the demographic disposition listed in this data.

> This data contains information on police contacts between January 26, 2015 through the present. The Berkeley Police Department will be updating this information approximately every 60 days.

# From the data page
https://data.cityofberkeley.info/Public-Safety/Berkeley-PD-Stop-Data/6e9j-pj9p/about

https://data.cityofberkeley.info/Public-Safety/Stop-Data/6e9j-pj9p


Berkeley PD - Stop Data
This data was extracted from the Department’s Public Safety Server and covers the data beginning January 26, 2015. On January 26, 2015 the department began collecting data pursuant to General Order B-4 (issued December 31, 2014). Under that order, officers were required to provide certain data after making all vehicle detentions (including bicycles) and pedestrian detentions (up to five persons). This data set lists stops by police in the categories of traffic, suspicious vehicle, pedestrian and bicycle stops. Incident number, date and time, location and disposition codes are also listed in this data.
Address data has been changed from a specific address, where applicable, and listed as the block where the incident occurred. Disposition codes were entered by officers who made the stop. These codes included the person(s) race, gender, age (range), reason for the stop, enforcement action taken, and whether or not a search was conducted.
The officers of the Berkeley Police Department are prohibited from biased based policing, which is defined as any police-initiated action that relies on the race, ethnicity, or national origin rather than the behavior of an individual or information that leads the police to a particular individual who has been identified as being engaged in criminal activity.


## WTF is the dispositions header

From the Socrata data:

Ordered in the following sequence: 

## 1st Character = Race

- A (Asian) 
- B (Black) 
- H (Hispanic) 
- O (Other) 
- W (White) 


## 2nd Character = Gender

- F (Female) 
- M (Male) 




## 3rd Character = Age Range

- 1 (Less than 18) 
- 2 (18-29) 
- 3 (30-39) 
- 4 (Greater than 40) 


## 4th Character = Reason

- I (Investigation) 
- T (Traffic) 
- R (Reasonable Suspicion) 
- K (Probation/Parole) 
- W (Wanted) 

## 5th Character = Enforcement

- A (Arrest) 
- C (Citation) 
- O (Other) 
- W (Warning) 

## 6th Character =Car Search

- S (Search)
- N (No Search)


## Additional dispositions

- P - Primary case report
- M - MDT narrative only
- AR - Arrest report only (no case report submitted)
- IN - Incident report
- FC - Field Card
- CO - Collision investigation report
- MH - Emergency Psychiatric Evaluation TOW
- TOW - Impounded vehicle 0 or 00000
- 0 or 00000 - Officer made a stop of more than five persons 





# Stories

https://ww2.kqed.org/news/2015/10/10/berkeley-pd-releases-pedestrian-stop-data-after-charges-of-racial-profiling/

https://www.scribd.com/doc/283066052/Press-Release-Berkeley-Demographic-Results-2015

