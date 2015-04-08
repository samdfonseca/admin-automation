from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import css


class SidebarLocators(BaseLocatorGroup):
    DASHBOARD = css('li.dashboard')

    LOCATION_CONTROL = css('li.locations')
    CATEGORIES = css('li.categories')
    ITEM_CATEGORIES = css('li.locations li.categories a[href="/categories"]')
    MODIFIER_CATEGORIES = css('li.locations li.categories a[href="/modifier_categories"]')
    GROUPS = css('li.locations a[href="/groups"]')
    ITEMS = css('li.locations a[href="/items"]')
    MENUS = css('li.locations a[href="/menus"]')
    LOCATIONS = css('li.locations a[href="/locations"]')
    SECTIONS = css('li.locations a[href="/sections"]')
    TABLES = css('li.locations a[href="/tables"]')
    VARIANT_SETS = css('li.locations a[href="/option_types"]')
    MODIFIERS = css('li.locations a[href="/modifiers"]')
    ADDON_GROUPS = css('li.locations a[href="/addon_groups"]')

    SUITES = css('li.suites')
    SUITES_ACCOUNTS = css('li.suites a[href="/suite_accounts"]')
    SUITES_SETUP = css('li.suites a[href="/suites"]')
    SUITES_PREORDER = css('li.suites a[href="/pre_orders"]')

    EVENTS = css('li.events')
    EVENTS_CALENDAR = css('li.events a[href="/events"]')
    EVENTS_TEMPLATES = css('li.events a[href="/event_templates"]')
    ORDERS = css('li.events a[href="/orders"]')
    TIPS = css('li.events a[href="/tips"]')
    CASHROOM = css('li.events a[href="/cashroom"]')

    INVENTORY = css('li.inventory')
    STATUS = css('li.inventory a[href="/inventory"]')
    INVENTORY_CATEGORIES = css('li.inventory a[href="/inventory_categories"]')
    INVENTORY_TRANSFERS = css('li.inventory a[href="/inventory_transfers"]')
    INVENTORY_MOVEMENTS = css('li.inventory a[href="/inventory_movements"]')
    STANDSHEETS = css('li.inventory a[href="/standsheets"]')
    STOCK_ITEMS = css('li.inventory a[href="/stock_items"]')
    RECIPES = css('li.inventory a[href="/recipes"]')
    VENDORS = css('li.inventory a[href="/vendors"]')
    INVENTORY_AUDITS = css('li.inventory a[href="/inventory_audits"]')
    PURCHASE_AND_RECEIVING = css('li.inventory a[href="/purchase_orders"]')
    WAREHOUSES = css('li.inventory a[href="/warehouses"]')

    REPORTING = css('li.reports')
    REPORTS = css('li.reports a[href="/reports"]')
    REPORT_TEMPLATES = css('li.reports a[href="/report_templates"]')

    ORDER_TAKERS = css('li.order-takers')
    DEVICES = css('li.terminals')
    ALERTS = css('li.alerts')

    BUCKS = css('li.bucks')
    BUCKS_CARD_SEARCH = css('li.bucks a[href="/bucks#/"]')
    BUCKS_ADD_NEW_CARD = css('li.bucks a[href="/bucks#/add_card"]')
    BUCKS_ALLOCATE_CARDS = css('li.bucks a[href="/bucks#/allocate"]')
    BUCKS_IMPORT_EXPORT = css('li.bucks a[href="/bucks#/import"]')
