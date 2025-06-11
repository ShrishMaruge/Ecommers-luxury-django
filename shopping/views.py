from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, FileResponse
from .models import Product, CartItem, ShippingDetail
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime

def home(request):
    categories = ["MEN CLOTHES", "Refrigerator", "BAGS", "girls tshirt", "mens shoes"]
    category = request.GET.get('category')
    query = request.GET.get('q', '')
    products = Product.objects.filter(category=category) if category in categories else Product.objects.all()
    if query:
        products = products.filter(name__icontains=query)
    cart_count = CartItem.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    return render(request, 'home.html', {'pro': products, 'categories': categories, 'query': query, 'cart_count': cart_count})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    messages.success(request, f"Added {product.name} to cart.")
    return redirect('home')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.info(request, "Item removed from cart.")
    return redirect('view_cart')

@login_required
def update_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    messages.success(request, "Quantity updated.")
    return redirect('view_cart')

@login_required
def minus_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        messages.success(request, "Quantity decreased.")
    else:
        cart_item.delete()
        messages.info(request, "Item removed from cart.")
    return redirect('view_cart')

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def save_shipping_details(request):
    if request.method == 'POST':
        ShippingDetail.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            shipping_method=request.POST.get('shipping_method')
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def buy_now(request, product_id):
    CartItem.objects.filter(user=request.user).delete()
    product = get_object_or_404(Product, id=product_id)
    CartItem.objects.create(user=request.user, product=product, quantity=1)
    return redirect('checkout')

@login_required
def download_invoice(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    p.setFont("Helvetica-Bold", 20)
    p.drawCentredString(width / 2, height - 50, "Luxury Invoice")
    p.setFont("Helvetica", 12)
    p.drawString(50, height - 80, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    y = height - 120
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "Product")
    p.drawString(300, y, "Quantity")
    p.drawString(400, y, "Total Price")
    y -= 20
    p.setFont("Helvetica", 12)
    for item in cart_items:
        p.drawString(50, y, item.product.name)
        p.drawString(300, y, str(item.quantity))
        p.drawString(400, y, f"${item.total_price():.2f}")
        y -= 20
        if y < 100:
            p.showPage()
            y = height - 50
    y -= 20
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, f"Total Amount: ${total_price:.2f}")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="Luxury-Invoice.pdf")

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
        messages.error(request, "Username already taken.")
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next')
            return redirect(next_url if next_url else 'home')
        messages.error(request, "Invalid credentials.")
    return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('home')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import CartItem, ShippingDetail

@login_required
def profile_view(request):
    user = request.user
    recent_cart_items = CartItem.objects.filter(user=user).order_by('-id')[:5]
    order_history = ShippingDetail.objects.filter(user=user).order_by('-created_at')

    # Calculate total price for recent cart items
    cart_total = sum(item.total_price() for item in recent_cart_items)

    return render(request, 'profile.html', {
        'user': user,
        'recent_cart_items': recent_cart_items,
        'order_history': order_history,
        'cart_total': cart_total,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]

    return render(request, 'product_detail.html', {'product': product , 'related_products':related_products})
