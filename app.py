import os
from flask import Flask, render_template, request, redirect, url_for

#buat instance
app = Flask(__name__)

#definisi route dasar
@app.route('/')
def home():
    return "Hello World! Ini halaman utama."

#penambahan route /about
@app.route('/about')
def about():
    return "<h1> Tentang Kami</h1><p>Ini adalah halaman about.</p><ul><li>Item1</li></ul>"

@app.route('/contact')
def contact():
    return "<h1>Hubungi kami</h1><p>email@contoh.com</p>"

@app.route('/user/<username>')
def show_user(username):
    if username == "admin":
        return "Akses ditolak", 403  # Return 403 Forbidden for admin
    return render_template('user.html', username=username)
    # The line below will NEVER execute because of the return above
    # return f"Hello, {username}!"  # <-- This should be removed

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post ID: {post_id}"


@app.route('/user/<username>/<int:post_id>')
def user_profile(username, post_id):
    return render_template('user.html',
                           username=username,
                           post_id=post_id)


@app.route('/math', methods=['GET'])
def math_form():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return redirect(url_for('math_operations', num1=num1, num2=num2))
    except ValueError:
        return "Invalid input - please enter numbers only", 400

# Route for displaying results
@app.route('/math/<float:num1>/<float:num2>')
def math_operations(num1, num2):
    results = {
        'penjumlahan': num1 + num2,
        'pengurangan': num1 - num2,
        'perkalian': num1 * num2,
        'pembagian': num1 / num2 if num2 != 0 else "Error: Division by zero"
    }
    return render_template('math.html', 
                         num1=num1,
                         num2=num2,
                         results=results)

@app.route('/product/<string:product_name>')
def show_product(product_name):
    return render_template('product.html', product_name=product_name)


#jalankan server
if __name__ == '__main__':
    app.run(debug=True, port=3900)