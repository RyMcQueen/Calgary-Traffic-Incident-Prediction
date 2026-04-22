# Calgary Traffic Incident Prediction

A data analytics and machine learning project analyzing 60,000+ real traffic incident records in Calgary merged with 9 years of Environment Canada weather data. Built as a university group project (Group C, University of Lethbridge, April 2026) with personal responsibility for the Linear Regression and Random Forest models.

## Tech Stack
- Python (Pandas, scikit-learn)
- Jupyter Notebook
- Tableau (exploratory visualization and dashboard)

## Dataset
Two real-world datasets merged on date:
- **Traffic Incidents 2016-2026** — 60,000+ incident records including location, quadrant, and timestamp
- **Climate Data 2016-2026** — Daily weather observations from Calgary International Airport including temperature, precipitation, snowfall, and wind

## Features Used
- Day of week, month, season, weekend indicator
- Mean, min, and max temperature
- Total snowfall, rainfall, snow on ground
- Wind gust direction and speed

## Models and Results
| Model | MAE | RMSE | R2 |
|---|---|---|---|
| Voting Regressor | 5.16 | 6.88 | 0.403 |
| Random Forest | 5.24 | 6.98 | 0.385 |
| Linear Regression | 5.49 | 7.12 | 0.360 |

Full results for all 9 models are documented in the notebook.

## Key Finding
Limited predictability across all models reflected data constraints rather than model failure. Weather alone is not a strong predictor of daily incident counts due to missing variables including real-time traffic conditions, road-specific details, and city events. Ensemble methods handled the non-linear relationships best.

## Personal Contribution
Built and evaluated the Linear Regression and Random Forest models end to end, including feature input, model training, and evaluation using MAE, RMSE, and R2 score.
