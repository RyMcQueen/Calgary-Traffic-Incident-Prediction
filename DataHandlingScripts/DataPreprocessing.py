#Some script to do some EDA stuff that I Want 
import os
import pandas as pd

base = os.path.dirname(__file__)

print("Basic Record Info")

climateLocation = os.path.join(base,"Data/Climate, aggregated 2016-2026(1).csv")
trafficLocation = os.path.join(base,"Data/Traffic Incidents, 2016-2026.csv")
traffic = pd.read_csv(trafficLocation, na_values=["", " ", "NA", "NULL"])
climate = pd.read_csv(climateLocation, na_values=["", " ", "NA", "NULL"])

#This to end of basic is just info, dont think we need it
traffic.head()
climate.head()

traffic.columns
climate.columns

traffic.info()
climate.info()

#traffic.shape
#climate.shape

#print(climate.columns.tolist())
print("End of Basic Info Getting into other stuff")

print("\nClimate Missing Values")
print(climate.isnull().sum())

print("\nTraffic Missing Values")
print(traffic.isnull().sum())

#Filling in empty columns 
climate["Snow on Grnd (cm)"] = climate["Snow on Grnd (cm)"].fillna(0)
climate["Total Snow (cm)"] = climate["Total Snow (cm)"].fillna(0)
#Gust Speed Conversion to numeric 
climate["Spd of Max Gust (km/h)"] = pd.to_numeric(
    climate["Spd of Max Gust (km/h)"], errors="coerce"
)
climate["Spd of Max Gust (km/h)"]=climate["Spd of Max Gust (km/h)"].fillna(0)
#Wind Direction Stuff 
climate["Dir of Max Gust (10s deg)"]=pd.to_numeric(
    climate["Dir of Max Gust (10s deg)"], errors="coerce"
)
climate["Dir of Max Gust (10s deg)"] = climate["Dir of Max Gust (10s deg)"].fillna(0)

#Now For traffic 
#Quadrant extraction from incident info if missing
#Extract Q from the end of the incidnet info string
traffic["extracted_quadrant"] = traffic["INCIDENT INFO"].str.extract(r'\b(NE|NW|SE|SW)\b$', expand=False)
#if Q missing, fill in using extracted q
traffic["QUADRANT"] = traffic["QUADRANT"].fillna(traffic["extracted_quadrant"])
#if non extracted (unknown)
traffic["QUADRANT"]=traffic["QUADRANT"].fillna("Unknown")
#Drop Helper column 
traffic.drop(columns=["extracted_quadrant"], inplace=True)


#Convert Date Columns for traffic 
traffic["START_DT"] = pd.to_datetime(traffic["START_DT"])
traffic["MODIFIED_DT"] = pd.to_datetime(traffic["MODIFIED_DT"], errors="coerce")
climate["Date/Time"] = pd.to_datetime(climate["Date/Time"])
#----------------------------------------------------
#Test for me to make sure it all went through 
print("\nRemaining Climate Missing Values")
print(climate.isnull().sum())

print("\nRemaining Traffic Missing Values")
print(traffic.isnull().sum())

#----------------------------------------------------
#Create Derived Variables (Data Reconstruction)
traffic["hour"]=traffic["START_DT"].dt.hour
traffic["day_of_week"] = traffic["START_DT"].dt.day_name()
traffic["month"] = traffic["START_DT"].dt.month
traffic["date"] = traffic["START_DT"].dt.date

#Making some Seasonal Varaibles 
def get_season(month):
    if month in [12,1,2]:
        return "Winter"
    elif month in [3,4,5]:
        return "Spring"
    elif month in [6,7,8]:
        return "Summer"
    else:
        return "Fall"

traffic["season"]=traffic["month"].apply(get_season)

#exporting the cleaned files for now 
#MaybeGPT can help or will be be smushing the files together after we combine the incidents 
#idk what is best becasue we kinda wanted to look at specific incidents at some point but maybe
#Well change our toon just to get it all condences... idk 


# Export cleaned datasets
cleanFolder = os.path.join(base, "CleanData")

os.makedirs(cleanFolder, exist_ok=True)

climate_output = os.path.join(cleanFolder, "climate_cleaned.csv")
traffic_output = os.path.join(cleanFolder, "traffic_cleaned.csv")

climate.to_csv(climate_output, index=False)
traffic.to_csv(traffic_output, index=False)

print("\nClean datasets exported successfully")
print(climate_output)
print(traffic_output)