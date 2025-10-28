from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tekeliler-tekstil-2025-secret-key'

# Örnek ürün veritabanı
PRODUCTS = [
    {
        'id': 1,
        'name': 'Lüks El Dokuma Halı',
        'category': 'hali',
        'price': 15000,
        'image': 'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800&auto=format&fit=crop&q=85',
        'description': 'Geleneksel Türk motifli, el dokuması premium halı',
        'stock': 5,
        'rating': 4.8
    },
    {
        'id': 2,
        'name': 'Modern Geometrik Kilim',
        'category': 'kilim',
        'price': 8500,
        'image': 'https://images.unsplash.com/photo-1582582621959-48d27397dc69?w=800&auto=format&fit=crop&q=85',
        'description': 'Modern tasarım geometrik desenli kilim',
        'stock': 10,
        'rating': 4.5
    },
    {
        'id': 3,
        'name': 'İpek Jakar Perde',
        'category': 'perde',
        'price': 3500,
        'image': 'https://cdn.dsmcdn.com/ty6/product/media/images/20200621/16/3263664/74922583/0/0_org_zoom.jpg',
        'description': 'İpek karışımlı lüks jakar perde',
        'stock': 15,
        'rating': 4.7
    },
    {
        'id': 4,
        'name': 'Vintage Anadolu Halısı',
        'category': 'hali',
        'price': 12000,
        'image': 'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=800&auto=format&fit=crop&q=85',
        'description': 'Vintage görünümlü özel dokuma Anadolu halısı',
        'stock': 3,
        'rating': 4.9
    },
    {
        'id': 5,
        'name': 'Çift Taraflı Kilim',
        'category': 'kilim',
        'price': 6500,
        'image': 'https://img.vivense.com/1920x1280/images/0628214a84414a39a1963af165824eee.jpg',
        'description': 'İki tarafı da kullanılabilen dayanıklı kilim',
        'stock': 8,
        'rating': 4.4
    },
    {
        'id': 6,
        'name': 'Blackout Stor Perde',
        'category': 'perde',
        'price': 2500,
        'image': 'https://images.unsplash.com/photo-1540518614846-7eded433c457?w=800&auto=format&fit=crop&q=85',
        'description': 'Işık geçirmez, modern stor perde',
        'stock': 20,
        'rating': 4.6
    }
]

@app.route('/')
def index():
    featured_products = PRODUCTS[:3]
    return render_template('index.html', featured_products=featured_products)

@app.route('/products')
def products():
    category = request.args.get('category', 'all')
    if category == 'all':
        filtered_products = PRODUCTS
    else:
        filtered_products = [p for p in PRODUCTS if p['category'] == category]
    return render_template('products.html', products=filtered_products, category=category)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return "Ürün bulunamadı", 404

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    data = request.get_json()
    # Gerçek uygulamada burada e-posta gönderme veya veritabanına kaydetme işlemi yapılır
    print(f"Yeni iletişim formu: {data}")
    return jsonify({'status': 'success', 'message': 'Mesajınız alındı!'})

@app.route('/api/search')
def search():
    query = request.args.get('q', '').lower()
    results = [p for p in PRODUCTS if query in p['name'].lower() or query in p['description'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

