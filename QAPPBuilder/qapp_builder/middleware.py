# from django.urls import reverse
# from django.shortcuts import redirect


# class AuthenticationMiddlewareExempt:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.exempt_urls = [
#             reverse('home'),     # Update with your home page URL name
#             reverse('dashboard'),    # Update with your about page URL name
#             reverse('contact'),  # Update with your contact page URL name
#         ]

#     def __call__(self, request):
#         print('++++++++++++++++++++++++++++++++++++++++++++')
#         print('++++++++++++++++++++++++++++++++++++++++++++')
#         print('++++++++++++++++++++++++++++++++++++++++++++')
#         print(request.path_info)
#         print('++++++++++++++++++++++++++++++++++++++++++++')
#         print('++++++++++++++++++++++++++++++++++++++++++++')
#         print('++++++++++++++++++++++++++++++++++++++++++++')
#         if request.user.is_authenticated or request.path_info in self.exempt_urls:  # noqa: E501
#             # User is authenticated or the URL is exempt, so continue
#             return self.get_response(request)

#         # User is not authenticated and the URL is not exempt,
#         # redirect to the login page
#         return redirect('login')  # Update with your login URL name
