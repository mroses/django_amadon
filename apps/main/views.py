from django.shortcuts import render, redirect

# Create your views here.
def index(req):
    return render(req, 'main/index.html')

def buy(req):
    req.session['total_items'] = 0
    req.session['total_cost'] = 0

    price = {
        '1015': '19.99',
        '1016': '24.99',
        '1017': '4.99',
        '1018': '49.99'
    }   

    req.session['product_num'] = req.POST['product_id']   

    total_item_price = float(price[req.POST['product_id']]) * int(req.POST['quantity'])
    req.session['total_item_price'] = total_item_price

    req.session['item_quantity'] = req.POST['quantity']

    req.session['total_items'] += int(req.session['item_quantity'])
    req.session['total_cost'] = float(req.session['total_item_price']) * int(req.POST['quantity'])

    return redirect('/main/checkout')

def checkout(req):
    return render(req, 'main/checkout.html')

def goback(req):
    req.session.clear()
    return redirect('/')
