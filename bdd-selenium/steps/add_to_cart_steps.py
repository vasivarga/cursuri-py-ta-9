from behave import *


@when('I click Add to cart')
def step_impl(context):
    context.search_results_page.click_add_to_cart()

@then('Cart has "{number}" item in it')
def step_impl(context, number):
    context.search_results_page.verify_cart_quantity(number)