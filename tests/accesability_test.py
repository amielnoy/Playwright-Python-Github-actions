import allure
import pytest


class TestAccessibility:
    #suppose to fail because of 3 moderate violations
    @pytest.mark.xfail
    @allure.title("Test Accessibility with Default Counts")
    def test_accessibility_default_counts(self, axe_playwright, page):
        axe_playwright.check_accessibility(page)

    @pytest.mark.xfail
    @pytest.mark.nondestructive
    @allure.title("Test Accessibility with Custom Counts")
    def test_accessibility_no_violations_allowed(self, axe_playwright, page):
        axe_playwright.check_accessibility(
            page,
            maximum_allowed_violations_by_impact={
                "minor": 0,
                "moderate": 0,
                "serious": 0,
                "critical": 0,
            },
        )
    @pytest.mark.nondestructive
    @allure.title("Test Accessibility with Custom Counts")
    def test_accessibility_custom_counts(self, axe_playwright, page):
        axe_playwright.check_accessibility(
            page,
            maximum_allowed_violations_by_impact={
                "minor": 4,
                "moderate": 4,
                "serious": 1,
                "critical": 0,
            },
        )

    @pytest.mark.nondestructive
    @allure.title("Test Accessibility with Custom Counts")
    def test_accessibility_custom_counts(self, axe_playwright, page):
        axe_playwright.check_accessibility(
            page,
            maximum_allowed_violations_by_impact={
                "minor": 2,
                "moderate": 5,
                "serious": 0,
                "critical": 0,
            },
        )
    @pytest.mark.nondestructive
    @allure.title("Test Accessibility with Custom Counts")
    def test_accessibility_custom_counts(self, axe_playwright, page):
        axe_playwright.check_accessibility(
            page,
            maximum_allowed_violations_by_impact={
                "minor": 5,
                "moderate": 5,
                "serious": 1,
                "critical": 0,
            },
        )
