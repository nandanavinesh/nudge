import pandas as pd
import sqlite3
from sklearn.linear_model import LinearRegression
import numpy as np

def get_dataframe():
    conn = sqlite3.connect('nudge.db')
    df = pd.read_sql_query('''
        SELECT date, social_media, productive_screen, 
               tasks_completed, sleep_hours, mood 
        FROM logs ORDER BY date ASC
    ''', conn)
    conn.close()
    return df

def calculate_productivity_score(row):
    score = (
        (row['productive_screen'] * 15) +
        (row['tasks_completed'] * 10) +
        (row['sleep_hours'] * 5) +
        (row['mood'] * 3) -
        (row['social_media'] * 8)
    )
    return round(max(0, min(100, score)), 1)

def get_insights(df):
    insights = []
    
    if len(df) < 3:
        return ["Log at least 3 days to see insights!"]
    
    corr_social = df['social_media'].corr(df['productivity_score'])
    corr_sleep = df['sleep_hours'].corr(df['productivity_score'])
    corr_productive = df['productive_screen'].corr(df['productivity_score'])

    if corr_social < -0.3:
        insights.append(f"On high social media days your productivity drops significantly. Try capping it at 1hr.")
    
    if corr_sleep > 0.3:
        high_sleep = df[df['sleep_hours'] >= 7]['productivity_score'].mean()
        low_sleep = df[df['sleep_hours'] < 7]['productivity_score'].mean()
        if not np.isnan(high_sleep) and not np.isnan(low_sleep):
            diff = round(high_sleep - low_sleep, 1)
            insights.append(f"You're {diff} points more productive on days you sleep 7+ hours.")

    if corr_productive > 0.3:
        insights.append(f"More productive screen time strongly correlates with better days for you.")

    best_day = df.loc[df['productivity_score'].idxmax()]
    insights.append(f"Your best day was {best_day['date']} with a score of {best_day['productivity_score']}.")

    return insights

def predict_tomorrow(df):
    if len(df) < 3:
        return None
    
    features = ['social_media', 'productive_screen', 'tasks_completed', 'sleep_hours', 'mood']
    X = df[features]
    y = df['productivity_score']
    
    model = LinearRegression()
    model.fit(X, y)
    
    last_row = df[features].iloc[-1].values.reshape(1, -1)
    prediction = model.predict(last_row)[0]
    return round(max(0, min(100, prediction)), 1)

def get_analysis():
    df = get_dataframe()
    
    if df.empty:
        return {'error': 'No data yet'}
    
    df['productivity_score'] = df.apply(calculate_productivity_score, axis=1)
    
    insights = get_insights(df)
    prediction = predict_tomorrow(df)
    
    chart_data = {
        'dates': df['date'].tolist(),
        'productivity_scores': df['productivity_score'].tolist(),
        'social_media': df['social_media'].tolist(),
        'productive_screen': df['productive_screen'].tolist(),
        'sleep_hours': df['sleep_hours'].tolist()
    }
    
    return {
        'insights': insights,
        'prediction': prediction,
        'chart_data': chart_data,
        'average_score': round(df['productivity_score'].mean(), 1)
    }