from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from cart.models import CartItem
from products.models import Product  # ✅ Direct import now safe
import json
import os

class Command(BaseCommand):
    help = "Import cart items with user, product name, and quantity"

    def handle(self, *args, **kwargs):
        # Locate the JSON file relative to this script
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, "carts_filtered.json")

        # Load JSON data
        try:
            with open(file_path, "r") as f:
                entries = json.load(f)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"❌ File not found: {file_path}"))
            return
        except json.JSONDecodeError:
            self.stderr.write(self.style.ERROR("❌ Failed to parse JSON file."))
            return

        # Import each cart item
        created_count = 0
        for item in entries:
            try:
                user = User.objects.get(id=item["user"])
            except User.DoesNotExist:
                self.stderr.write(self.style.WARNING(f"⚠️ Skipped: User ID {item['user']} not found."))
                continue

            try:
                product = Product.objects.get(name=item["product"])
            except Product.DoesNotExist:
                self.stderr.write(self.style.WARNING(f"⚠️ Skipped: Product '{item['product']}' not found."))
                continue

            quantity = item.get("quantity", 1)

            CartItem.objects.create(
                user=user,
                product=product,
                quantity=quantity
            )
            created_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Imported {created_count} cart items successfully."))
