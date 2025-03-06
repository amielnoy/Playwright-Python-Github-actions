import pytest
from playwright.sync_api import Page, expect

from enums.User import User
from tests.base_test import BaseTest


class TestCheckout(BaseTest):

    @pytest.mark.parametrize(
        "browser_context_args", [User.STANDARD_USER], indirect=True
    )
    def test_checkout_counter(self, browser_context_args, page: Page):
        page.evaluate("localStorage.setItem('cart-contents', '[4,0]');")
        page.reload()
        actual_site_ip = BaseTest.get_public_ip()
        expected_site_ip = "5.29.18.59"
        # Use Python's assert statement for string comparison
        assert (
            expected_site_ip in actual_site_ip
        ), f"Expected IP '{expected_site_ip}' not found in actual IP '{actual_site_ip}'"
        expect(page.get_by_test_id("shopping-cart-badge")).to_have_text("2")
