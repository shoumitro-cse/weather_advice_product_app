from accounts.models import ADMIN, VENDOR, CUSTOMER


class AdminMixin:
    error_message = {"error": "The user must be an admin."}

    def is_admin_user(self, *args, **kwargs):
        return self.request.user.user_type == ADMIN and self.request.user.is_superuser


class VendorMixin:
    error_message = {"error": "The user must be an vendor."}

    def is_vendor_user(self, *args, **kwargs):
        return self.request.user.user_type == VENDOR and not self.request.user.is_superuser


class CustomerMixin:
    error_message = {"error": "The user must be an customer."}

    def is_customer_user(self, *args, **kwargs):
        return self.request.user.user_type == CUSTOMER and not self.request.user.is_superuser


class UserMixin(AdminMixin, VendorMixin, CustomerMixin):

    def get_user(self):
        return self.request.user