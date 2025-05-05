from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('dataset.csv')

@app.route('/')
def home():
    # Get basic statistics
    total_orders = len(df)
    total_revenue = df['OrderValue'].sum()
    avg_order_value = df['OrderValue'].mean()
    
    # Get top districts
    top_districts = df['District'].value_counts().head(5).to_dict()
    
    # Get payment type distribution
    payment_types = df['PaymentType'].value_counts().to_dict()
    
    # Get order source distribution
    order_sources = df['OrderSource'].value_counts().to_dict()
    
    return render_template('index.html',
                         total_orders=total_orders,
                         total_revenue=total_revenue,
                         avg_order_value=avg_order_value,
                         top_districts=top_districts,
                         payment_types=payment_types,
                         order_sources=order_sources)

@app.route('/data')
def get_data():
    # Return first 10 rows of data
    return jsonify(df.head(10).to_dict('records'))

if __name__ == '__main__':
    app.run(debug=True) 