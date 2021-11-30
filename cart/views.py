from django.shortcuts import render,redirect,reverse
from django.shortcuts import get_object_or_404
from nBookapp.models import Book
from Accounts.models import Student
from cart.models import Order, OrderItem
from cart.extras import generate_order_id
from django.contrib import messages
# Create your views here.

def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Student, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

def add_to_cart(request, **kwargs):
    
    user_profile = get_object_or_404(Student, user=request.user)
    # filter products by id
    book = Book.objects.filter(id=kwargs.get('item_id', "")).first()
    book.IsOrdered= True
    # create orderItem of the selected book
    order_item, status = OrderItem.objects.get_or_create(book=book)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    #messages.info(request, "item added to cart")
    return redirect(reverse('Book_List_User'))



def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('cart:order_summary'))

def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'order_summary.html', context)

def checkout(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'checkout.html', context)


