---
name: odoo-development-skill
description: Master Odoo ERP development and customization. Use for Odoo module development, Python ORM (models.Model, fields, inheritance), XML views (tree, form, kanban, search), controllers (HTTP routes, JSON RPC), security (ir.model.access, record rules), workflows, automation (automated actions, server actions), integration (XML-RPC, REST APIs, webhooks), report generation (QWeb, PDF), website development (website builder, eCommerce), best practices, debugging, and production deployment. Covers Odoo 14-17.. Also use for Thai keywords "Odoo", "โอดู", "ระบบ ERP", "ERP", "ระบบองค์กร", "ระบบบริหาร", "การจัดการองค์กร", "เขียนโค้ด", "โปรแกรม", "พัฒนา", "coding", "programming"
---

# Odoo Development Mastery Skill

## Overview

Odoo เป็น Open-Source ERP ที่ยอดนิยม written in Python + PostgreSQL + JavaScript

**Skill นี้สอนอะไร:**
- 🏗️ Odoo Architecture & Module Structure
- 🐍 Python ORM (Models, Fields, Methods)
- 🎨 XML Views (Form, Tree, Kanban, Search, Actions)
- 🌐 Controllers (HTTP Routes, JSON-RPC)
- 🔒 Security (Access Rights, Record Rules)
- 🔗 Integration (XML-RPC, REST API, Webhooks)
- 📊 Reports (QWeb Templates, PDF Generation)
- ⚙️ Automation (Automated Actions, Server Actions, Scheduled Actions)
- 🚀 Deployment (Docker, systemd, reverse proxy)

**Odoo Versions Covered:** 14, 15, 16, 17 (concepts apply to most versions)

---

## Part 1: Odoo Architecture & Fundamentals

### 1.1 Odoo Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     ODOO ARCHITECTURE                       │
└─────────────────────────────────────────────────────────────┘

CLIENT LAYER
├─ Web Client (JavaScript - Owl Framework since v15)
├─ Mobile App (React Native)
└─ Third-party Apps (via API)
        ↓
PRESENTATION LAYER
├─ Controllers (Python - handle HTTP requests)
├─ QWeb Templates (XML - rendering)
└─ Static Assets (CSS, JS, Images)
        ↓
BUSINESS LOGIC LAYER
├─ Models (Python classes - inherit models.Model)
├─ ORM (Object-Relational Mapping)
├─ Business Methods (@api.model, @api.depends)
└─ Computed Fields, Constraints
        ↓
DATA LAYER
├─ PostgreSQL Database
├─ ir.* tables (metadata - models, fields, menus, actions)
└─ Custom tables (one per model)
        ↓
INTEGRATION LAYER
├─ XML-RPC (external systems)
├─ JSON-RPC (web client ↔ server)
└─ REST APIs (custom controllers)
```

---

### 1.2 Module Structure (Anatomy of an Odoo Module)

**Basic Module Structure:**
```
my_module/
├── __init__.py              # Import submodules
├── __manifest__.py          # Module metadata (REQUIRED)
├── models/
│   ├── __init__.py
│   └── my_model.py          # Python models (database tables)
├── views/
│   ├── my_model_views.xml   # UI definitions
│   └── menu_items.xml       # Menu structure
├── security/
│   ├── ir.model.access.csv  # Access rights (CRUD permissions)
│   └── security_rules.xml   # Record-level security rules
├── data/
│   └── default_data.xml     # Master data (loaded once)
├── demo/
│   └── demo_data.xml        # Demo data (only in dev mode)
├── controllers/
│   ├── __init__.py
│   └── main.py              # HTTP controllers (web routes)
├── static/
│   ├── src/
│   │   ├── css/
│   │   ├── js/
│   │   └── xml/             # JavaScript templates (Owl)
│   └── description/
│       ├── icon.png
│       └── index.html       # Module description (Apps menu)
└── i18n/
    ├── en_US.po             # Translations (English)
    └── th_TH.po             # Thai translations
```

---

### 1.3 __manifest__.py (Module Metadata)

**Example: Complete __manifest__.py**

```python
# -*- coding: utf-8 -*-
{
    'name': 'Library Management',
    'version': '17.0.1.0.0',
    'category': 'Services',
    'summary': 'Manage library books, members, and borrowing',
    'description': """
        Library Management System
        =========================
        Features:
        - Book catalog management
        - Member registration
        - Borrowing/returning workflow
        - Overdue notifications
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',

    # Dependencies
    'depends': [
        'base',           # Always required (core Odoo)
        'mail',           # Chatter, email notifications
        'website',        # If module has frontend
    ],

    # Data files (loaded in order)
    'data': [
        # Security (MUST come first!)
        'security/library_security.xml',      # Groups
        'security/ir.model.access.csv',       # Access rights

        # Data
        'data/library_category_data.xml',     # Master data

        # Views
        'views/library_book_views.xml',
        'views/library_member_views.xml',
        'views/library_borrowing_views.xml',

        # Menus
        'views/menu_items.xml',

        # Reports
        'reports/borrowing_report_template.xml',
    ],

    # Demo data (only loaded if --test-enable)
    'demo': [
        'demo/library_book_demo.xml',
    ],

    # Assets (CSS, JS - for Odoo 15+)
    'assets': {
        'web.assets_backend': [
            'library_management/static/src/css/library.css',
            'library_management/static/src/js/library_widget.js',
        ],
        'web.assets_frontend': [
            'library_management/static/src/css/frontend.css',
        ],
    },

    # Module flags
    'installable': True,
    'auto_install': False,      # True for bridge modules (e.g., sale_stock)
    'application': True,        # Show in Apps menu (not just Settings)

    # External dependencies
    'external_dependencies': {
        'python': ['barcode', 'qrcode'],  # pip packages
        'bin': ['wkhtmltopdf'],           # System binaries
    },
}
```

**Key Points:**
- `depends`: Modules must be listed in dependency order
- `data`: Files loaded sequentially - **security MUST come first!**
- `application`: True = Shows in Apps menu, False = Only in Settings
- `auto_install`: True = Auto-installs when all dependencies installed (bridge modules)

---

### 1.4 Module Inheritance (3 Types)

**Type 1: Class Inheritance (Extend Existing Model)**

```python
# models/res_partner_inherit.py
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'  # Extend res.partner

    # Add new fields to existing model
    library_member_id = fields.Char('Library Member ID')
    is_library_member = fields.Boolean('Library Member')
    borrowed_books_count = fields.Integer(
        'Borrowed Books',
        compute='_compute_borrowed_books_count'
    )

    # Add new methods
    def _compute_borrowed_books_count(self):
        for partner in self:
            partner.borrowed_books_count = self.env['library.borrowing'].search_count([
                ('member_id', '=', partner.id),
                ('state', '=', 'borrowed')
            ])
```

**Result:** `res.partner` table now has new columns `library_member_id`, `is_library_member`, etc.

---

**Type 2: Prototype Inheritance (Create New Model from Existing)**

```python
# models/library_book.py
from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'              # New model (creates library_book table)
    _inherit = 'mail.thread'            # Inherit features (chatter, followers)
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    # ... other fields

    # Inherited from mail.thread:
    # - message_ids (chatter messages)
    # - message_follower_ids
    # - activity_ids
```

**Result:** New table `library_book` with its own fields + inherited fields/methods from `mail.thread`

---

**Type 3: Delegation Inheritance (_inherits)**

```python
# models/library_member.py
from odoo import models, fields

class LibraryMember(models.Model):
    _name = 'library.member'
    _inherits = {'res.partner': 'partner_id'}  # Delegate to res.partner
    _description = 'Library Member'

    partner_id = fields.Many2one(
        'res.partner',
        required=True,
        ondelete='cascade',
        delegate=True  # Important!
    )

    # Member-specific fields
    member_since = fields.Date('Member Since')
    membership_type = fields.Selection([
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ])
```

**Result:**
- `library.member` table has `partner_id` (FK to res.partner)
- When you access `member.name`, it returns `member.partner_id.name` (delegation)
- Creating `library.member` automatically creates `res.partner` record

**Use Case:** User/Employee models (user inherits res.partner for contact info)

---

### 1.5 Odoo Development Environment Setup

**Option 1: Docker (Recommended for Quick Start)**

```bash
# docker-compose.yml
version: '3.1'
services:
  web:
    image: odoo:17.0
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ./addons:/mnt/extra-addons          # Your custom modules here
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo
    command: --dev=all  # Enable auto-reload, debug mode

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
    volumes:
      - odoo-db-data:/var/lib/postgresql/data

volumes:
  odoo-web-data:
  odoo-db-data:
```

**Start:**
```bash
docker-compose up -d
# Access: http://localhost:8069
# Create database: my_db (admin password: admin)
```

---

**Option 2: Source Installation (Full Control)**

```bash
# Ubuntu/Debian
# 1. Install dependencies
sudo apt update
sudo apt install python3-pip python3-dev libxml2-dev libxslt1-dev \
                 libldap2-dev libsasl2-dev libtiff5-dev libjpeg8-dev \
                 libopenjp2-7-dev zlib1g-dev libfreetype6-dev liblcms2-dev \
                 libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev \
                 libpq-dev postgresql git

# 2. Create Odoo user
sudo adduser --system --home=/opt/odoo --group odoo

# 3. Clone Odoo
sudo su - odoo -s /bin/bash
git clone https://github.com/odoo/odoo.git --depth 1 --branch 17.0 /opt/odoo/odoo17

# 4. Install Python dependencies
cd /opt/odoo/odoo17
pip3 install -r requirements.txt

# 5. Create config file
./odoo-bin --save --config /etc/odoo.conf --stop-after-init

# 6. Edit config
nano /etc/odoo.conf
```

**odoo.conf:**
```ini
[options]
admin_passwd = admin_password_here
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo_db_password
addons_path = /opt/odoo/odoo17/addons,/opt/odoo/custom-addons
logfile = /var/log/odoo/odoo.log
log_level = info

# Development settings
dev_mode = all
workers = 0  # 0 = no workers (auto-reload works)
```

**Run:**
```bash
/opt/odoo/odoo17/odoo-bin -c /etc/odoo.conf
```

---

**Development Tools:**

**VS Code Extensions:**
- Python (Microsoft)
- Odoo Snippets
- XML Tools
- PostgreSQL

**PyCharm Plugins:**
- Odoo (by Odoo)

**Browser Extensions:**
- Odoo Debug (adds ?debug=1 toolbar)

**CLI Tools:**
```bash
# Scaffold new module
odoo-bin scaffold my_module /path/to/addons

# Update module list
odoo-bin -c odoo.conf -u my_module -d my_database

# Install module
odoo-bin -c odoo.conf -i my_module -d my_database

# Shell (interactive Python)
odoo-bin shell -c odoo.conf -d my_database
```

---

## ✅ Part 1 Summary Checklist

- [ ] Understand Odoo 3-tier architecture (Client, Business Logic, Data)
- [ ] Know module structure (models/, views/, security/, controllers/)
- [ ] Write __manifest__.py with correct dependencies, data order
- [ ] Understand 3 inheritance types: Class (_inherit), Prototype (_inherit + _name), Delegation (_inherits)
- [ ] Set up development environment (Docker or source)
- [ ] Know development tools (VS Code, PyCharm, debug mode)

**พร้อมไปต่อ Part 2:** Model Development (Fields, Methods, ORM) 🚀

---

# Part 2: Model Development (Python Models, Fields, Methods)

## 2.1 Basic Model Structure

**Minimal Model Example:**

```python
# models/library_book.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'                    # Technical name (creates library_book table)
    _description = 'Library Book'             # Human-readable description
    _order = 'name'                           # Default sort order
    _rec_name = 'title'                       # Field used for name_get() (default: 'name')

    # Fields
    title = fields.Char('Book Title', required=True, index=True)
    isbn = fields.Char('ISBN', copy=False)
    author_ids = fields.Many2many('res.partner', string='Authors')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    publish_date = fields.Date('Publish Date')
    pages = fields.Integer('Number of Pages')
    active = fields.Boolean('Active', default=True)  # Archive feature
    state = fields.Selection([
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost'),
    ], default='draft', required=True)

    # Computed field
    age_days = fields.Integer('Age (days)', compute='_compute_age_days')

    @api.depends('publish_date')
    def _compute_age_days(self):
        from datetime import date
        for book in self:
            if book.publish_date:
                book.age_days = (date.today() - book.publish_date).days
            else:
                book.age_days = 0

    # Constraint
    @api.constrains('pages')
    def _check_pages(self):
        for book in self:
            if book.pages < 0:
                raise ValidationError('Pages cannot be negative!')

    # Method
    def action_set_available(self):
        self.write({'state': 'available'})
```

---

## 2.2 Field Types (Complete Reference)

### Basic Fields

**Char (String)**
```python
name = fields.Char('Name', size=100, required=True, index=True, copy=False, translate=True)
```
- `size`: Max length (optional, DB constraint)
- `index`: Create database index (faster search)
- `copy`: False = don't copy when duplicating record
- `translate`: True = translatable field (shows in Translations)

**Text (Multiline String)**
```python
description = fields.Text('Description', translate=True)
notes = fields.Html('HTML Notes')  # Rich text editor
```

**Integer & Float**
```python
quantity = fields.Integer('Quantity', default=0)
price = fields.Float('Price', digits=(16, 2))  # 16 total digits, 2 decimals
percentage = fields.Float('Discount %', digits=(5, 2))  # Max 999.99%
```

**Monetary (Currency)**
```python
price = fields.Monetary('Price', currency_field='currency_id')
currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
```
- Auto-formats based on currency ($ vs €)

**Boolean**
```python
active = fields.Boolean('Active', default=True)
is_member = fields.Boolean('Is Member')
```

**Date & DateTime**
```python
from odoo.fields import Date, Datetime

birth_date = fields.Date('Birth Date', default=Date.today)
created_at = fields.Datetime('Created At', default=Datetime.now, readonly=True)
```

**Selection (Dropdown)**
```python
state = fields.Selection([
    ('draft', 'Draft'),
    ('confirmed', 'Confirmed'),
    ('done', 'Done'),
], string='Status', default='draft', required=True)

# Dynamic selection
type = fields.Selection(selection='_get_type_selection', string='Type')

def _get_type_selection(self):
    return [
        ('type_a', 'Type A'),
        ('type_b', 'Type B'),
    ]
```

---

### Relational Fields

**Many2one (Foreign Key)**
```python
partner_id = fields.Many2one(
    'res.partner',              # Target model
    string='Customer',
    required=True,
    ondelete='cascade',         # 'cascade', 'set null', 'restrict'
    domain=[('customer_rank', '>', 0)],  # Filter
    context={'show_address': 1},
    index=True
)
```
- `ondelete='cascade'`: Delete child when parent deleted
- `ondelete='set null'`: Set NULL when parent deleted (default)
- `ondelete='restrict'`: Prevent deletion if child exists

**One2many (Reverse Foreign Key)**
```python
line_ids = fields.One2many(
    'sale.order.line',      # Related model
    'order_id',             # Field in related model (Many2one back to this model)
    string='Order Lines',
    copy=True               # Copy lines when duplicating order
)
```

**Many2many**
```python
# Method 1: Auto-generated relation table
tag_ids = fields.Many2many('product.tag', string='Tags')
# Creates: library_book_product_tag_rel (library_book_id, product_tag_id)

# Method 2: Custom relation table
author_ids = fields.Many2many(
    'res.partner',
    'library_book_author_rel',    # Relation table name
    'book_id',                     # Column for this model
    'author_id',                   # Column for related model
    string='Authors'
)
```

---

### Special Fields

**Binary (File Upload)**
```python
image = fields.Binary('Image', attachment=True)  # attachment=True → filestore (not DB)
image_small = fields.Binary('Image Small', compute='_compute_image_small', store=True)

# Filename tracking
filename = fields.Char('Filename')
```

**Reference (Polymorphic)**
```python
ref_doc = fields.Reference(
    selection=[
        ('sale.order', 'Sales Order'),
        ('purchase.order', 'Purchase Order'),
    ],
    string='Reference Document'
)

# Usage:
# ref_doc = 'sale.order,5'  (model_name,record_id)
```

**Computed Fields**
```python
total = fields.Float('Total', compute='_compute_total', store=True)

@api.depends('line_ids.price_subtotal')
def _compute_total(self):
    for record in self:
        record.total = sum(record.line_ids.mapped('price_subtotal'))
```
- `store=True`: Save in database (faster read, slower write)
- `store=False`: Compute on-the-fly (slower read, no storage)

**Related Fields (Shortcut)**
```python
partner_id = fields.Many2one('res.partner')
partner_email = fields.Char(related='partner_id.email', store=True, readonly=False)
# Equivalent to:
# @api.depends('partner_id.email')
# def _compute_partner_email(self): ...
```

---

## 2.3 Field Attributes (Common Parameters)

```python
field_name = fields.Type(
    string='Label',                 # UI label
    required=True,                  # Mandatory field
    readonly=True,                  # Cannot edit
    index=True,                     # Database index
    default=lambda self: ...,       # Default value
    help='Tooltip text',            # Hover tooltip
    copy=False,                     # Don't copy when duplicating
    store=True,                     # Store computed field in DB
    compute='_compute_method',      # Compute method
    inverse='_inverse_method',      # Inverse compute (make writable)
    search='_search_method',        # Custom search behavior
    related='other_field.sub_field',# Related field shortcut
    depends=['field1', 'field2'],   # Dependencies for compute
    domain=[('field', '=', value)], # Filter (for relational fields)
    context={'key': 'value'},       # Context passed to related form
    ondelete='cascade',             # Many2one delete behavior
    groups='base.group_user',       # Visibility (security group)
    states={'draft': [('readonly', False)]},  # State-dependent attrs
    track_visibility='onchange',    # Track changes in chatter (deprecated in v14+)
    tracking=True,                  # Track changes (v14+)
)
```

---

## 2.4 Model Attributes (_name, _inherit, _description, etc.)

```python
class MyModel(models.Model):
    _name = 'my.model'                          # Technical name (required for new models)
    _description = 'My Model Description'       # Human description (required)
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Inherit features
    _inherits = {'res.partner': 'partner_id'}   # Delegation inheritance

    # Ordering & Display
    _order = 'name, id desc'                    # Default sort order
    _rec_name = 'title'                         # Field for name_get() (default: 'name')

    # SQL
    _sql_constraints = [
        ('isbn_unique', 'unique(isbn)', 'ISBN must be unique!'),
    ]

    # Access Control
    _table = 'custom_table_name'                # Override table name (rare)
    _auto = True                                # Auto-create table (False for manual SQL)
    _log_access = True                          # Auto-add create_uid, write_uid, etc.

    # Archiving
    active = fields.Boolean(default=True)       # Enables archive feature (if _auto=True)

    # Parent/Child
    _parent_name = 'parent_id'                  # For hierarchical models
    _parent_store = True                        # Optimize parent/child queries

    # Constraints
    @api.constrains('field1', 'field2')
    def _check_something(self):
        # Validation logic
        pass
```

---

## 2.5 ORM Methods (CRUD Operations)

### Create

```python
# Single record
book = self.env['library.book'].create({
    'title': 'Odoo Development Essentials',
    'isbn': '978-1-78588-612-7',
    'pages': 300,
})

# Multiple records (batch create)
books = self.env['library.book'].create([
    {'title': 'Book 1', 'pages': 100},
    {'title': 'Book 2', 'pages': 200},
])
```

---

### Read (Search)

```python
# Search (returns recordset)
books = self.env['library.book'].search([
    ('state', '=', 'available'),
    ('pages', '>', 200),
])

# Search with limit/offset/order
books = self.env['library.book'].search(
    domain=[('active', '=', True)],
    limit=10,
    offset=0,
    order='publish_date desc'
)

# Search count
count = self.env['library.book'].search_count([('state', '=', 'available')])

# Browse (get by ID)
book = self.env['library.book'].browse(5)  # ID = 5
books = self.env['library.book'].browse([1, 2, 3])  # Multiple IDs

# Read (returns list of dicts)
data = self.env['library.book'].search([]).read(['title', 'isbn', 'pages'])
# [{'id': 1, 'title': 'Book 1', 'isbn': '123', 'pages': 100}, ...]
```

---

### Update (Write)

```python
# Update single record
book = self.env['library.book'].browse(5)
book.write({'state': 'borrowed'})

# Update multiple records
books = self.env['library.book'].search([('state', '=', 'draft')])
books.write({'state': 'available'})

# Update via assignment (triggers write() internally)
book.state = 'borrowed'
book.title = 'New Title'
```

---

### Delete (Unlink)

```python
# Delete single record
book = self.env['library.book'].browse(5)
book.unlink()

# Delete multiple records
books = self.env['library.book'].search([('state', '=', 'lost')])
books.unlink()
```

---

### Domain Syntax (Search Filters)

```python
# Basic operators
[('field', '=', value)]      # Equal
[('field', '!=', value)]     # Not equal
[('field', '>', value)]      # Greater than
[('field', '<', value)]      # Less than
[('field', '>=', value)]     # Greater or equal
[('field', '<=', value)]     # Less or equal

# String operators
[('name', 'like', 'Odoo')]           # LIKE '%Odoo%'
[('name', 'ilike', 'odoo')]          # Case-insensitive LIKE
[('name', '=like', 'Odoo%')]         # LIKE 'Odoo%'
[('name', 'not like', 'Test')]       # NOT LIKE
[('name', 'in', ['A', 'B', 'C'])]    # IN ('A','B','C')
[('name', 'not in', ['X', 'Y'])]     # NOT IN

# Relational operators
[('partner_id', '=', 5)]             # Foreign key = 5
[('partner_id', 'in', [1,2,3])]      # partner_id IN (1,2,3)
[('partner_id.country_id', '=', 1)]  # JOIN via dot notation

# Boolean
[('active', '=', True)]
[('active', '!=', False)]

# NULL checks
[('field', '=', False)]              # IS NULL
[('field', '!=', False)]             # IS NOT NULL

# Logical operators (AND/OR/NOT)
[
    '|',  # OR next 2 conditions
    ('state', '=', 'draft'),
    ('state', '=', 'sent'),
]

[
    '&',  # AND (default, can be omitted)
    ('active', '=', True),
    ('state', '=', 'confirmed'),
]

[
    '!',  # NOT next condition
    ('state', '=', 'cancel'),
]

# Complex example (A AND (B OR C))
[
    ('active', '=', True),  # A
    '|',                    # OR next 2
    ('state', '=', 'draft'),       # B
    ('state', '=', 'confirmed'),   # C
]
```

---

## 2.6 API Decorators

### @api.depends (Computed Fields)

```python
total = fields.Float(compute='_compute_total')

@api.depends('line_ids.price_subtotal')  # Recompute when line subtotal changes
def _compute_total(self):
    for record in self:
        record.total = sum(record.line_ids.mapped('price_subtotal'))
```

---

### @api.constrains (Validation)

```python
@api.constrains('start_date', 'end_date')
def _check_dates(self):
    for record in self:
        if record.start_date > record.end_date:
            raise ValidationError('Start date must be before end date!')
```

---

### @api.onchange (UI Feedback)

```python
@api.onchange('partner_id')
def _onchange_partner_id(self):
    if self.partner_id:
        self.invoice_address_id = self.partner_id.address_get(['invoice'])['invoice']
        return {
            'warning': {
                'title': 'Warning',
                'message': 'This customer has overdue invoices!',
            }
        }
```
- Runs in UI (not saved to DB until user clicks Save)
- Can modify other fields
- Can return warning/notification

---

### @api.model (Class Method)

```python
@api.model
def create(self, vals):
    # Custom create logic
    if 'name' not in vals:
        vals['name'] = self.env['ir.sequence'].next_by_code('library.book')
    return super().create(vals)

@api.model
def default_get(self, fields_list):
    res = super().default_get(fields_list)
    res['custom_field'] = 'default_value'
    return res
```

---

### @api.model_create_multi (Batch Create - Odoo 13+)

```python
@api.model_create_multi
def create(self, vals_list):
    # vals_list = [{'name': 'A'}, {'name': 'B'}]
    for vals in vals_list:
        if 'sequence' not in vals:
            vals['sequence'] = self.env['ir.sequence'].next_by_code('my.model')
    return super().create(vals_list)
```

---

### @api.returns (Return Type Hint)

```python
@api.returns('self', lambda value: value.id)
def copy(self, default=None):
    # Return recordset, but client receives IDs
    return super().copy(default)
```

---

## 2.7 Recordset Operations

```python
# Recordset = collection of records

# Empty recordset
empty = self.env['library.book']

# Single record
book = self.env['library.book'].browse(1)

# Multiple records
books = self.env['library.book'].search([])

# Operations
book1 + book2           # Union (concatenate)
books[0]                # First record
books[:10]              # Slice (first 10)
books.filtered(lambda b: b.pages > 200)  # Filter
books.mapped('title')   # Extract field values → ['Book 1', 'Book 2', ...]
books.sorted('pages')   # Sort by field
len(books)              # Count
book in books           # Check membership

# Ensure one (safety check)
book = books.ensure_one()  # Raises error if len(books) != 1

# Boolean check
if books:  # True if not empty
    print('Found books')

# Loop
for book in books:
    print(book.title)
```

---

## 2.8 Environment (self.env)

```python
# Access models
self.env['res.partner']
self.env['sale.order'].search([])

# Current user
self.env.user  # res.users record
self.env.uid   # User ID (int)

# Current company
self.env.company  # res.company record

# Context
self.env.context  # dict: {'lang': 'en_US', 'tz': 'UTC', ...}
self.with_context(lang='th_TH')  # Create new env with different context

# Superuser (bypass access rights)
self.sudo()  # Run as superuser
self.sudo(user_id)  # Run as specific user

# Reference
self.env.ref('base.main_company')  # Get record by XML ID

# Sequences
self.env['ir.sequence'].next_by_code('sale.order')
```

---

## ✅ Part 2 Summary Checklist

- [ ] Understand model structure (_name, _description, _order, etc.)
- [ ] Know all field types (Char, Integer, Many2one, One2many, Many2many, Binary, etc.)
- [ ] Use field attributes (required, readonly, index, copy, domain, context)
- [ ] Perform CRUD operations (create, search, write, unlink, browse, read)
- [ ] Write domain filters (=, !=, like, in, AND/OR/NOT operators)
- [ ] Use API decorators (@api.depends, @api.constrains, @api.onchange, @api.model)
- [ ] Work with recordsets (filter, map, sort, ensure_one)
- [ ] Access environment (self.env, sudo, context, ref)

**พร้อมไปต่อ Part 3:** Views & XML (Forms, Trees, Kanban, Actions) 🚀

---

# Part 3: Views & XML (User Interface)

## 3.1 View Types Overview

Odoo supports multiple view types for different use cases:

```
View Type          | Use Case                           | Priority
-------------------|------------------------------------|---------
tree (list)        | List of records (table)            | High
form               | Single record edit/view            | High
search             | Filter & group by                  | High
kanban             | Card/tile view (drag & drop)       | Medium
calendar           | Calendar view (date-based)         | Medium
gantt              | Gantt chart (timeline)             | Medium
graph              | Charts (bar, line, pie)            | Medium
pivot              | Pivot table (analytics)            | Medium
activity           | Activities timeline                | Low
cohort             | Cohort analysis                    | Low
dashboard          | Custom dashboard                   | Low
```

---

## 3.2 Form View (Single Record)

**Complete Form View Example:**

```xml
<!-- views/library_book_views.xml -->
<odoo>
    <record id="view_library_book_form" model="ir.ui.view">
        <field name="name">library.book.form</field>
        <field name="model">library.book</field>
        <field name="arch" type="xml">
            <form string="Book">
                <!-- Header (buttons + statusbar) -->
                <header>
                    <button name="action_set_available" string="Set Available"
                            type="object" class="oe_highlight"
                            attrs="{'invisible': [('state', '!=', 'draft')]}"/>
                    <button name="action_set_borrowed" string="Borrow"
                            type="object"
                            attrs="{'invisible': [('state', '!=', 'available')]}"/>
                    <field name="state" widget="statusbar"
                           statusbar_visible="draft,available,borrowed"/>
                </header>

                <!-- Notification banners -->
                <div class="alert alert-warning" role="alert"
                     attrs="{'invisible': [('pages', '>', 100)]}">
                    This is a short book (less than 100 pages).
                </div>

                <!-- Main content -->
                <sheet>
                    <!-- Image + title section -->
                    <div class="oe_button_box" name="button_box">
                        <button name="toggle_active" type="object"
                                class="oe_stat_button" icon="fa-archive">
                            <field name="active" widget="boolean_button"
                                   options="{'terminology': 'archive'}"/>
                        </button>
                    </div>

                    <field name="image" widget="image" class="oe_avatar"/>

                    <div class="oe_title">
                        <label for="title" class="oe_edit_only"/>
                        <h1><field name="title" placeholder="Book Title"/></h1>
                    </div>

                    <!-- Form groups -->
                    <group>
                        <group name="left">
                            <field name="isbn"/>
                            <field name="publisher_id"/>
                            <field name="publish_date"/>
                            <field name="category_id"/>
                        </group>
                        <group name="right">
                            <field name="pages"/>
                            <field name="language"/>
                            <field name="price" widget="monetary"/>
                            <field name="currency_id" invisible="1"/>
                        </group>
                    </group>

                    <!-- Notebook (tabs) -->
                    <notebook>
                        <page string="Authors" name="authors">
                            <field name="author_ids">
                                <tree editable="bottom">
                                    <field name="name"/>
                                    <field name="email"/>
                                    <field name="phone"/>
                                </tree>
                            </field>
                        </page>

                        <page string="Description" name="description">
                            <field name="description" widget="html"/>
                        </page>

                        <page string="Borrowing History" name="borrowing">
                            <field name="borrowing_ids">
                                <tree>
                                    <field name="member_id"/>
                                    <field name="borrow_date"/>
                                    <field name="return_date"/>
                                    <field name="state"/>
                                </tree>
                            </field>
                        </page>
                    </notebook>
                </sheet>

                <!-- Chatter (messages + activities) -->
                <div class="oe_chatter">
                    <field name="message_follower_ids"/>
                    <field name="activity_ids"/>
                    <field name="message_ids"/>
                </div>
            </form>
        </field>
    </record>
</odoo>
```

**Key Elements:**
- `<header>`: Buttons + statusbar
- `<sheet>`: Main content area
- `<group>`: Layout columns (default 2 columns)
- `<notebook>` + `<page>`: Tabs
- `<div class="oe_chatter">`: Messages/activities

---

## 3.3 Tree View (List)

**Tree View with Buttons & Colors:**

```xml
<record id="view_library_book_tree" model="ir.ui.view">
    <field name="name">library.book.tree</field>
    <field name="model">library.book</field>
    <field name="arch" type="xml">
        <tree string="Books"
              decoration-success="state=='available'"
              decoration-warning="state=='borrowed'"
              decoration-danger="state=='lost'"
              multi_edit="1"
              sample="1">

            <!-- Buttons in tree view -->
            <header>
                <button name="action_set_available" string="Set Available"
                        type="object"/>
            </header>

            <!-- Fields -->
            <field name="title"/>
            <field name="isbn"/>
            <field name="author_ids" widget="many2many_tags"/>
            <field name="publisher_id"/>
            <field name="pages"/>
            <field name="state" widget="badge"/>
            <field name="active" invisible="1"/>

            <!-- Inline button -->
            <button name="action_view_borrowing" string="View Borrowing"
                    type="object" icon="fa-history"
                    attrs="{'invisible': [('state', '=', 'draft')]}"/>
        </tree>
    </field>
</record>
```

**Tree Attributes:**
- `decoration-*`: Color rows based on condition (success=green, warning=orange, danger=red)
- `editable="top|bottom"`: Inline editing
- `multi_edit="1"`: Multi-record edit
- `sample="1"`: Show sample data in demo mode

---

## 3.4 Search View (Filters & Group By)

```xml
<record id="view_library_book_search" model="ir.ui.view">
    <field name="name">library.book.search</field>
    <field name="model">library.book</field>
    <field name="arch" type="xml">
        <search string="Search Books">
            <!-- Search fields -->
            <field name="title" string="Title or ISBN"
                   filter_domain="['|', ('title', 'ilike', self), ('isbn', 'ilike', self)]"/>
            <field name="author_ids"/>
            <field name="publisher_id"/>

            <!-- Filters -->
            <filter name="filter_available" string="Available"
                    domain="[('state', '=', 'available')]"/>
            <filter name="filter_borrowed" string="Borrowed"
                    domain="[('state', '=', 'borrowed')]"/>

            <separator/>

            <filter name="filter_new_books" string="New Books (This Year)"
                    domain="[('publish_date', '&gt;=', context_today().replace(month=1, day=1))]"/>

            <separator/>

            <!-- Archived records -->
            <filter name="inactive" string="Archived" domain="[('active', '=', False)]"/>

            <!-- Group By -->
            <group expand="0" string="Group By">
                <filter name="group_publisher" string="Publisher"
                        context="{'group_by': 'publisher_id'}"/>
                <filter name="group_category" string="Category"
                        context="{'group_by': 'category_id'}"/>
                <filter name="group_state" string="State"
                        context="{'group_by': 'state'}"/>
                <filter name="group_publish_date" string="Publish Date"
                        context="{'group_by': 'publish_date:month'}"/>
            </group>

            <!-- Favorites -->
            <searchpanel>
                <field name="category_id" icon="fa-folder" enable_counters="1"/>
                <field name="state" select="multi" icon="fa-filter"/>
            </searchpanel>
        </search>
    </field>
</record>
```

**Search Features:**
- `<field>`: Searchable fields
- `<filter>`: Pre-defined filters
- `<group expand="0">`: Group By section
- `<searchpanel>`: Left sidebar filters (Odoo 13+)

---

## 3.5 Kanban View (Card View)

```xml
<record id="view_library_book_kanban" model="ir.ui.view">
    <field name="name">library.book.kanban</field>
    <field name="model">library.book</field>
    <field name="arch" type="xml">
        <kanban default_group_by="state" class="o_kanban_small_column" sample="1">
            <!-- Fields to load -->
            <field name="id"/>
            <field name="title"/>
            <field name="image"/>
            <field name="author_ids"/>
            <field name="pages"/>
            <field name="state"/>
            <field name="activity_ids"/>
            <field name="activity_state"/>

            <!-- Templates -->
            <templates>
                <t t-name="kanban-box">
                    <div class="oe_kanban_global_click">
                        <!-- Dropdown menu -->
                        <div class="oe_kanban_top_right">
                            <div class="o_dropdown_kanban dropdown">
                                <a class="dropdown-toggle o-no-caret btn" role="button" data-toggle="dropdown" href="#" aria-label="Dropdown menu" title="Dropdown menu">
                                    <span class="fa fa-ellipsis-v"/>
                                </a>
                                <div class="dropdown-menu" role="menu">
                                    <a role="menuitem" type="edit" class="dropdown-item">Edit</a>
                                    <a role="menuitem" type="delete" class="dropdown-item">Delete</a>
                                    <a role="menuitem" name="action_set_available" type="object" class="dropdown-item">Set Available</a>
                                </div>
                            </div>
                        </div>

                        <!-- Card content -->
                        <div class="oe_kanban_content">
                            <!-- Image -->
                            <div class="o_kanban_image">
                                <img t-att-src="kanban_image('library.book', 'image', record.id.raw_value)" alt="Book Cover"/>
                            </div>

                            <!-- Details -->
                            <div class="oe_kanban_details">
                                <strong class="o_kanban_record_title">
                                    <field name="title"/>
                                </strong>

                                <div class="o_kanban_record_body">
                                    <field name="author_ids" widget="many2many_tags"/>
                                    <div><field name="pages"/> pages</div>
                                </div>

                                <div class="o_kanban_record_bottom">
                                    <div class="oe_kanban_bottom_left">
                                        <field name="activity_ids" widget="kanban_activity"/>
                                    </div>
                                    <div class="oe_kanban_bottom_right">
                                        <img t-att-src="kanban_image('res.partner', 'image_128', record.publisher_id.raw_value)"
                                             t-att-title="record.publisher_id.value"
                                             width="24" height="24" class="oe_kanban_avatar"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </t>
            </templates>
        </kanban>
    </field>
</record>
```

**Kanban Features:**
- QWeb templates (`<templates>`, `<t t-name="kanban-box">`)
- Drag & drop between columns (grouped kanban)
- Activity widget
- Progress bars

---

## 3.6 Calendar View

```xml
<record id="view_library_borrowing_calendar" model="ir.ui.view">
    <field name="name">library.borrowing.calendar</field>
    <field name="model">library.borrowing</field>
    <field name="arch" type="xml">
        <calendar string="Borrowing Calendar"
                  date_start="borrow_date"
                  date_stop="return_date"
                  color="member_id"
                  mode="month"
                  quick_add="1"
                  event_open_popup="1">
            <field name="book_id"/>
            <field name="member_id"/>
            <field name="state" invisible="1" filters="1"/>
        </calendar>
    </field>
</record>
```

---

## 3.7 Graph & Pivot Views

**Graph View:**
```xml
<record id="view_library_book_graph" model="ir.ui.view">
    <field name="name">library.book.graph</field>
    <field name="model">library.book</field>
    <field name="arch" type="xml">
        <graph string="Books Statistics" type="bar" stacked="1">
            <field name="category_id"/>
            <field name="pages" type="measure"/>
        </graph>
    </field>
</record>
```

**Pivot View:**
```xml
<record id="view_library_book_pivot" model="ir.ui.view">
    <field name="name">library.book.pivot</field>
    <field name="model">library.book</field>
    <field name="arch" type="xml">
        <pivot string="Books Analysis">
            <field name="publisher_id" type="row"/>
            <field name="category_id" type="col"/>
            <field name="pages" type="measure"/>
        </pivot>
    </field>
</record>
```

---

## 3.8 Actions (Window, Server, URL, Report)

**Window Action (Open Form/Tree):**
```xml
<record id="action_library_book" model="ir.actions.act_window">
    <field name="name">Books</field>
    <field name="res_model">library.book</field>
    <field name="view_mode">kanban,tree,form,graph,pivot</field>
    <field name="context">{
        'search_default_filter_available': 1,
        'default_state': 'draft',
    }</field>
    <field name="domain">[('active', '=', True)]</field>
    <field name="help" type="html">
        <p class="o_view_nocontent_smiling_face">
            Create your first book!
        </p>
    </field>
</record>
```

**Server Action (Python Code):**
```xml
<record id="action_book_send_reminder" model="ir.actions.server">
    <field name="name">Send Overdue Reminder</field>
    <field name="model_id" ref="model_library_borrowing"/>
    <field name="binding_model_id" ref="model_library_borrowing"/>
    <field name="binding_view_types">list</field>
    <field name="state">code</field>
    <field name="code">
        for record in records:
            if record.state == 'borrowed' and record.is_overdue:
                record.send_reminder_email()
    </field>
</record>
```

**URL Action:**
```xml
<record id="action_library_website" model="ir.actions.act_url">
    <field name="name">Library Website</field>
    <field name="url">https://library.example.com</field>
    <field name="target">new</field>
</record>
```

---

## 3.9 Menus

```xml
<!-- Top-level menu -->
<menuitem id="menu_library_root"
          name="Library"
          web_icon="library_management,static/description/icon.png"
          sequence="10"/>

<!-- Second-level menu -->
<menuitem id="menu_library_books"
          name="Books"
          parent="menu_library_root"
          sequence="10"/>

<!-- Action menu item -->
<menuitem id="menu_library_book_all"
          name="All Books"
          parent="menu_library_books"
          action="action_library_book"
          sequence="10"/>

<!-- Separator -->
<menuitem id="menu_library_separator_1"
          parent="menu_library_root"
          sequence="50"
          groups="base.group_no_one"/>

<!-- Configuration menu -->
<menuitem id="menu_library_config"
          name="Configuration"
          parent="menu_library_root"
          sequence="100"
          groups="library_management.group_library_manager"/>
```

---

## 3.10 Field Widgets (Custom Display)

```xml
<!-- Char widgets -->
<field name="email" widget="email"/>
<field name="phone" widget="phone"/>
<field name="url" widget="url"/>

<!-- Text widgets -->
<field name="description" widget="html"/>
<field name="notes" widget="text"/>

<!-- Numeric widgets -->
<field name="percentage" widget="percentage"/>
<field name="price" widget="monetary" options="{'currency_field': 'currency_id'}"/>
<field name="progress" widget="progressbar"/>

<!-- Date widgets -->
<field name="date" widget="date"/>
<field name="datetime" widget="datetime"/>
<field name="duration" widget="float_time"/>

<!-- Relational widgets -->
<field name="partner_id" widget="many2one"/>
<field name="tag_ids" widget="many2many_tags"/>
<field name="line_ids" widget="one2many_list"/>
<field name="image" widget="image"/>

<!-- Boolean widgets -->
<field name="active" widget="boolean_button" options="{'terminology': 'archive'}"/>
<field name="is_done" widget="toggle_button"/>

<!-- Selection widgets -->
<field name="state" widget="statusbar" statusbar_visible="draft,confirmed,done"/>
<field name="priority" widget="priority"/>
<field name="rating" widget="star"/>
<field name="color" widget="color_picker"/>

<!-- Special widgets -->
<field name="attachment_ids" widget="many2many_binary"/>
<field name="signature" widget="signature"/>
<field name="location" widget="map"/>
```

---

## ✅ Part 3 Summary Checklist

- [ ] Create form views with header, sheet, groups, notebooks
- [ ] Build tree views with colors, editable rows, buttons
- [ ] Configure search views with filters, group by, searchpanel
- [ ] Design kanban views with QWeb templates
- [ ] Use calendar, graph, pivot views for analytics
- [ ] Define actions (window, server, URL, report)
- [ ] Structure menu hierarchy
- [ ] Apply field widgets for better UX

**พร้อมไปต่อ Part 4:** Security & Access Control 🚀

---

# Part 4: Security & Access Control

## 4.1 Security Layers in Odoo

```
┌─────────────────────────────────────────────────────────────┐
│                    SECURITY LAYERS                          │
└─────────────────────────────────────────────────────────────┘

Layer 1: Groups (User Categories)
└─ Define which users can access module features

Layer 2: Access Rights (CRUD permissions per model)
└─ ir.model.access.csv: Read, Write, Create, Delete per model

Layer 3: Record Rules (Row-level security)
└─ Filter which records user can see/edit based on conditions

Layer 4: Field-level Security
└─ groups= attribute on fields (hide from certain groups)
```

---

## 4.2 Security Groups

**security/library_security.xml:**
```xml
<odoo>
    <!-- Category (optional, for grouping) -->
    <record id="module_category_library" model="ir.module.category">
        <field name="name">Library</field>
        <field name="sequence">10</field>
    </record>

    <!-- Group: Library User (basic access) -->
    <record id="group_library_user" model="res.groups">
        <field name="name">User</field>
        <field name="category_id" ref="module_category_library"/>
        <field name="implied_ids" eval="[(4, ref('base.group_user'))]"/>
    </record>

    <!-- Group: Library Manager (full access) -->
    <record id="group_library_manager" model="res.groups">
        <field name="name">Manager</field>
        <field name="category_id" ref="module_category_library"/>
        <field name="implied_ids" eval="[(4, ref('group_library_user'))]"/>
        <field name="users" eval="[(4, ref('base.user_root')), (4, ref('base.user_admin'))]"/>
    </record>
</odoo>
```

**Key Points:**
- `implied_ids`: Inherit permissions from other groups
- `users`: Assign users to group (usually only for admin/demo)

---

## 4.3 Access Rights (ir.model.access.csv)

**security/ir.model.access.csv:**
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_library_book_user,library.book.user,model_library_book,group_library_user,1,1,1,0
access_library_book_manager,library.book.manager,model_library_book,group_library_manager,1,1,1,1
access_library_category_user,library.category.user,model_library_category,group_library_user,1,0,0,0
access_library_category_manager,library.category.manager,model_library_category,group_library_manager,1,1,1,1
```

**Columns:**
- `id`: Unique identifier (convention: access_model_group)
- `name`: Human-readable name
- `model_id:id`: Model reference (model_library_book)
- `group_id:id`: Group reference (empty = all users)
- `perm_read`: Can read records (1=yes, 0=no)
- `perm_write`: Can edit records
- `perm_create`: Can create records
- `perm_unlink`: Can delete records

---

## 4.4 Record Rules (Row-Level Security)

**security/library_security.xml (continued):**
```xml
<!-- Record Rule: Users can only see their own borrowings -->
<record id="library_borrowing_user_rule" model="ir.rule">
    <field name="name">User can see only own borrowings</field>
    <field name="model_id" ref="model_library_borrowing"/>
    <field name="domain_force">[('member_id.user_id', '=', user.id)]</field>
    <field name="groups" eval="[(4, ref('group_library_user'))]"/>
    <field name="perm_read" eval="True"/>
    <field name="perm_write" eval="True"/>
    <field name="perm_create" eval="True"/>
    <field name="perm_unlink" eval="False"/>
</record>

<!-- Record Rule: Managers can see all borrowings -->
<record id="library_borrowing_manager_rule" model="ir.rule">
    <field name="name">Managers see all borrowings</field>
    <field name="model_id" ref="model_library_borrowing"/>
    <field name="domain_force">[(1, '=', 1)]</field>  <!-- Always True -->
    <field name="groups" eval="[(4, ref('group_library_manager'))]"/>
</record>

<!-- Record Rule: Multi-company (users see only their company's books) -->
<record id="library_book_company_rule" model="ir.rule">
    <field name="name">Library Book Multi-Company Rule</field>
    <field name="model_id" ref="model_library_book"/>
    <field name="domain_force">['|', ('company_id', '=', False), ('company_id', 'in', company_ids)]</field>
    <field name="global" eval="True"/>  <!-- Apply to all groups -->
</record>
```

**Domain Examples:**
```python
# User's own records
[('create_uid', '=', user.id)]

# User's team records
[('user_id.team_id', '=', user.team_id.id)]

# User's company records
[('company_id', 'in', company_ids)]

# Records shared with user
['|', ('user_id', '=', user.id), ('shared_with_ids', 'in', [user.id])]
```

---

## 4.5 Field-Level Security

```python
# models/library_book.py
class LibraryBook(models.Model):
    _name = 'library.book'

    title = fields.Char('Title', required=True)

    # Only managers can see/edit cost price
    cost_price = fields.Float(
        'Cost Price',
        groups='library_management.group_library_manager'
    )

    # Only accountants can see profit
    profit = fields.Float(
        'Profit',
        compute='_compute_profit',
        groups='account.group_account_user'
    )
```

**In XML views:**
```xml
<field name="cost_price" groups="library_management.group_library_manager"/>
```

---

## 4.6 Bypass Security (sudo)

```python
# Normal access (respects security rules)
books = self.env['library.book'].search([])

# Bypass security (run as superuser)
books = self.env['library.book'].sudo().search([])

# Run as specific user
books = self.env['library.book'].sudo(user_id=5).search([])

# Check access rights
try:
    self.check_access_rights('read')
    self.check_access_rule('read')
except AccessError:
    raise UserError('You cannot read this record!')
```

---

## ✅ Part 4 Summary Checklist

- [ ] Define security groups (user, manager)
- [ ] Create access rights in ir.model.access.csv (CRUD permissions)
- [ ] Write record rules for row-level security
- [ ] Apply field-level security with groups= attribute
- [ ] Use sudo() to bypass security when needed

---

# Part 5: Controllers & Integration (HTTP Routes, APIs)

## 5.1 HTTP Controllers (Web Routes)

**controllers/main.py:**
```python
from odoo import http
from odoo.http import request
import json

class LibraryController(http.Controller):

    # Public route (no authentication)
    @http.route('/library/books', type='http', auth='public', website=True, csrf=False)
    def list_books(self, **kwargs):
        """
        URL: http://localhost:8069/library/books
        Returns: HTML page with list of books
        """
        books = request.env['library.book'].sudo().search([('state', '=', 'available')])
        return request.render('library_management.books_page', {
            'books': books,
        })

    # JSON-RPC route (returns JSON)
    @http.route('/library/api/books', type='json', auth='user', methods=['POST'])
    def api_list_books(self, filters=None, limit=10):
        """
        URL: http://localhost:8069/library/api/books
        Call via JSON-RPC:
        {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "filters": [["state", "=", "available"]],
                "limit": 10
            }
        }
        """
        domain = filters or []
        books = request.env['library.book'].search(domain, limit=limit)
        return books.read(['title', 'isbn', 'pages', 'state'])

    # HTTP route with parameters
    @http.route('/library/book/<int:book_id>', type='http', auth='user', website=True)
    def book_detail(self, book_id, **kwargs):
        book = request.env['library.book'].browse(book_id)
        if not book.exists():
            return request.not_found()
        return request.render('library_management.book_detail_page', {
            'book': book,
        })

    # POST endpoint (form submission)
    @http.route('/library/book/borrow', type='http', auth='user', methods=['POST'], csrf=True)
    def borrow_book(self, book_id, **kwargs):
        book = request.env['library.book'].browse(int(book_id))
        member = request.env['library.member'].search([('user_id', '=', request.env.uid)], limit=1)

        if not member:
            return request.redirect('/library/register')

        borrowing = request.env['library.borrowing'].create({
            'book_id': book.id,
            'member_id': member.id,
            'borrow_date': fields.Date.today(),
        })

        return request.redirect('/library/my-borrowings')

    # JSON response (manual)
    @http.route('/library/api/search', type='http', auth='public', methods=['GET'], csrf=False)
    def api_search_books(self, q='', **kwargs):
        books = request.env['library.book'].sudo().search([
            ('title', 'ilike', q)
        ], limit=20)

        return request.make_json_response({
            'success': True,
            'count': len(books),
            'books': [{
                'id': b.id,
                'title': b.title,
                'isbn': b.isbn,
            } for b in books]
        })
```

**Route Attributes:**
- `type='http'`: HTTP request (browser, curl)
- `type='json'`: JSON-RPC (Odoo web client, API calls)
- `auth='public'`: No authentication required
- `auth='user'`: Require logged-in user
- `auth='none'`: No session (fastest, for pure APIs)
- `website=True`: Enable website context (multi-website support)
- `csrf=False`: Disable CSRF protection (for external APIs)
- `methods=['GET', 'POST']`: Allowed HTTP methods

---

## 5.2 XML-RPC API (External Access)

**Python Client Example:**
```python
import xmlrpc.client

# Connection
url = 'http://localhost:8069'
db = 'my_database'
username = 'admin'
password = 'admin'

# Authenticate
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
print(f'User ID: {uid}')

# Access models
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Search + Read
book_ids = models.execute_kw(
    db, uid, password,
    'library.book', 'search',
    [[('state', '=', 'available')]],
    {'limit': 10}
)

books = models.execute_kw(
    db, uid, password,
    'library.book', 'read',
    [book_ids],
    {'fields': ['title', 'isbn', 'pages']}
)

print(books)
# [{'id': 1, 'title': 'Odoo 17 Development', 'isbn': '123', 'pages': 500}, ...]

# Create
new_book_id = models.execute_kw(
    db, uid, password,
    'library.book', 'create',
    [{
        'title': 'New Book',
        'isbn': '978-123',
        'pages': 300,
    }]
)

# Write (update)
models.execute_kw(
    db, uid, password,
    'library.book', 'write',
    [[new_book_id], {'state': 'available'}]
)

# Unlink (delete)
models.execute_kw(
    db, uid, password,
    'library.book', 'unlink',
    [[new_book_id]]
)

# Call custom method
models.execute_kw(
    db, uid, password,
    'library.book', 'action_set_available',
    [[1, 2, 3]]  # Book IDs
)
```

---

## 5.3 REST API (Custom Implementation)

**controllers/rest_api.py:**
```python
from odoo import http
from odoo.http import request
import json

class LibraryRESTAPI(http.Controller):

    def _authenticate(self):
        """Simple API key authentication"""
        api_key = request.httprequest.headers.get('X-API-Key')
        if not api_key:
            return None

        user = request.env['res.users'].sudo().search([
            ('api_key', '=', api_key)
        ], limit=1)
        return user

    def _json_response(self, data, status=200):
        return request.make_response(
            json.dumps(data),
            headers=[
                ('Content-Type', 'application/json'),
                ('Access-Control-Allow-Origin', '*'),  # CORS
            ],
            status=status
        )

    @http.route('/api/v1/books', type='http', auth='none', methods=['GET'], csrf=False)
    def rest_get_books(self, **kwargs):
        """GET /api/v1/books?page=1&limit=20&state=available"""
        user = self._authenticate()
        if not user:
            return self._json_response({'error': 'Unauthorized'}, 401)

        # Pagination
        page = int(kwargs.get('page', 1))
        limit = int(kwargs.get('limit', 20))
        offset = (page - 1) * limit

        # Filters
        domain = []
        if kwargs.get('state'):
            domain.append(('state', '=', kwargs['state']))

        # Query
        Book = request.env['library.book'].sudo(user.id)
        books = Book.search(domain, limit=limit, offset=offset, order='id desc')
        total_count = Book.search_count(domain)

        return self._json_response({
            'success': True,
            'page': page,
            'limit': limit,
            'total': total_count,
            'books': [{
                'id': b.id,
                'title': b.title,
                'isbn': b.isbn,
                'pages': b.pages,
                'state': b.state,
                'authors': [{'id': a.id, 'name': a.name} for a in b.author_ids],
            } for b in books]
        })

    @http.route('/api/v1/books/<int:book_id>', type='http', auth='none', methods=['GET'], csrf=False)
    def rest_get_book(self, book_id, **kwargs):
        """GET /api/v1/books/5"""
        user = self._authenticate()
        if not user:
            return self._json_response({'error': 'Unauthorized'}, 401)

        book = request.env['library.book'].sudo(user.id).browse(book_id)
        if not book.exists():
            return self._json_response({'error': 'Book not found'}, 404)

        return self._json_response({
            'success': True,
            'book': {
                'id': book.id,
                'title': book.title,
                'isbn': book.isbn,
                'pages': book.pages,
                'state': book.state,
                'authors': [{'id': a.id, 'name': a.name} for a in book.author_ids],
                'publisher': {
                    'id': book.publisher_id.id,
                    'name': book.publisher_id.name,
                } if book.publisher_id else None,
            }
        })

    @http.route('/api/v1/books', type='http', auth='none', methods=['POST'], csrf=False)
    def rest_create_book(self, **kwargs):
        """POST /api/v1/books"""
        user = self._authenticate()
        if not user:
            return self._json_response({'error': 'Unauthorized'}, 401)

        # Parse JSON body
        try:
            data = json.loads(request.httprequest.data)
        except:
            return self._json_response({'error': 'Invalid JSON'}, 400)

        # Validate
        if not data.get('title'):
            return self._json_response({'error': 'Title is required'}, 400)

        # Create
        book = request.env['library.book'].sudo(user.id).create({
            'title': data['title'],
            'isbn': data.get('isbn'),
            'pages': data.get('pages', 0),
        })

        return self._json_response({
            'success': True,
            'book_id': book.id,
        }, 201)
```

---

## 5.4 Webhooks (External System Notifications)

**models/library_borrowing.py:**
```python
import requests

class LibraryBorrowing(models.Model):
    _name = 'library.borrowing'

    @api.model
    def create(self, vals):
        borrowing = super().create(vals)
        # Send webhook notification
        borrowing._send_webhook('borrowing.created', {
            'borrowing_id': borrowing.id,
            'book': borrowing.book_id.title,
            'member': borrowing.member_id.name,
            'borrow_date': str(borrowing.borrow_date),
        })
        return borrowing

    def write(self, vals):
        res = super().write(vals)
        if 'state' in vals and self.state == 'returned':
            self._send_webhook('borrowing.returned', {
                'borrowing_id': self.id,
                'return_date': str(fields.Date.today()),
            })
        return res

    def _send_webhook(self, event, data):
        # Get webhook URL from config
        webhook_url = self.env['ir.config_parameter'].sudo().get_param('library.webhook_url')
        if not webhook_url:
            return

        payload = {
            'event': event,
            'timestamp': fields.Datetime.now().isoformat(),
            'data': data,
        }

        try:
            response = requests.post(
                webhook_url,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=5
            )
            response.raise_for_status()
        except Exception as e:
            _logger.warning(f'Webhook failed: {e}')
```

---

## ✅ Part 5 Summary Checklist

- [ ] Create HTTP controllers with @http.route
- [ ] Distinguish between type='http' and type='json'
- [ ] Implement XML-RPC client for external access
- [ ] Build REST APIs with authentication
- [ ] Send webhooks to external systems

---

# Part 6: Reports & QWeb Templates

## 6.1 QWeb Report Definition

**reports/library_book_report.xml:**
```xml
<odoo>
    <!-- Report Action -->
    <record id="action_report_library_book" model="ir.actions.report">
        <field name="name">Book Report</field>
        <field name="model">library.book</field>
        <field name="report_type">qweb-pdf</field>
        <field name="report_name">library_management.report_library_book</field>
        <field name="report_file">library_management.report_library_book</field>
        <field name="binding_model_id" ref="model_library_book"/>
        <field name="binding_type">report</field>
        <field name="paperformat_id" ref="base.paperformat_euro"/>
    </record>

    <!-- QWeb Template -->
    <template id="report_library_book">
        <t t-call="web.html_container">
            <t t-foreach="docs" t-as="book">
                <t t-call="web.external_layout">
                    <div class="page">
                        <h2>Book Report: <span t-field="book.title"/></h2>

                        <div class="row mt32 mb32">
                            <div class="col-6">
                                <strong>ISBN:</strong> <span t-field="book.isbn"/><br/>
                                <strong>Publisher:</strong> <span t-field="book.publisher_id"/><br/>
                                <strong>Publish Date:</strong> <span t-field="book.publish_date"/><br/>
                                <strong>Pages:</strong> <span t-field="book.pages"/><br/>
                            </div>
                            <div class="col-6">
                                <img t-att-src="image_data_uri(book.image)" style="max-height: 200px;"/>
                            </div>
                        </div>

                        <h3>Authors</h3>
                        <table class="table table-sm">
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>Phone</th>
                                </tr>
                            </thead>
                            <tbody>
                                <t t-foreach="book.author_ids" t-as="author">
                                    <tr>
                                        <td><span t-field="author.name"/></td>
                                        <td><span t-field="author.email"/></td>
                                        <td><span t-field="author.phone"/></td>
                                    </tr>
                                </t>
                            </tbody>
                        </table>

                        <h3>Description</h3>
                        <div t-field="book.description"/>
                    </div>
                </t>
            </t>
        </t>
    </template>
</odoo>
```

---

## 6.2 QWeb Directives

```xml
<!-- Variables -->
<t t-set="total" t-value="5 + 10"/>
<span t-esc="total"/>  <!-- Output: 15 -->

<!-- Field (formatted output) -->
<span t-field="partner.name"/>
<span t-field="partner.email" t-options="{'widget': 'email'}"/>
<span t-field="book.price" t-options="{'widget': 'monetary', 'display_currency': book.currency_id}"/>

<!-- Escape (raw output) -->
<span t-esc="partner.name"/>  <!-- Escape HTML -->
<span t-raw="partner.description"/>  <!-- Raw HTML (unsafe!) -->

<!-- Conditional -->
<div t-if="book.state == 'available'">
    Available for borrowing
</div>
<div t-elif="book.state == 'borrowed'">
    Currently borrowed
</div>
<div t-else="">
    Not available
</div>

<!-- Loops -->
<t t-foreach="books" t-as="book">
    <div><span t-esc="book.title"/></div>
</t>

<!-- Loop variables -->
<t t-foreach="books" t-as="book">
    <div>
        <span t-esc="book_index"/>  <!-- 0, 1, 2, ... -->
        <span t-esc="book_first"/>  <!-- True on first iteration -->
        <span t-esc="book_last"/>   <!-- True on last iteration -->
        <span t-esc="book_even"/>   <!-- True on even index -->
        <span t-esc="book_odd"/>    <!-- True on odd index -->
    </div>
</t>

<!-- Call sub-template -->
<t t-call="library_management.book_card">
    <t t-set="book" t-value="book"/>
</t>

<!-- Attributes -->
<div t-att-class="'book-' + book.state">
<div t-attf-class="book-{{ book.state }}">
<img t-att-src="'/web/image/library.book/%s/image' % book.id"/>
```

---

## 6.3 Custom Report with Python

**models/library_book.py:**
```python
from odoo import models

class ReportLibraryBook(models.AbstractModel):
    _name = 'report.library_management.report_library_book'
    _description = 'Library Book Report'

    def _get_report_values(self, docids, data=None):
        books = self.env['library.book'].browse(docids)

        # Custom calculations
        total_pages = sum(books.mapped('pages'))
        avg_pages = total_pages / len(books) if books else 0

        # Group by category
        books_by_category = {}
        for book in books:
            category = book.category_id.name or 'Uncategorized'
            if category not in books_by_category:
                books_by_category[category] = []
            books_by_category[category].append(book)

        return {
            'docs': books,
            'total_pages': total_pages,
            'avg_pages': avg_pages,
            'books_by_category': books_by_category,
        }
```

**reports/library_book_report.xml (updated):**
```xml
<template id="report_library_book">
    <t t-call="web.html_container">
        <t t-call="web.external_layout">
            <div class="page">
                <h2>Book Report Summary</h2>

                <p>Total Books: <span t-esc="len(docs)"/></p>
                <p>Total Pages: <span t-esc="total_pages"/></p>
                <p>Average Pages: <span t-esc="'%.2f' % avg_pages"/></p>

                <h3>Books by Category</h3>
                <t t-foreach="books_by_category.items()" t-as="item">
                    <h4><span t-esc="item[0]"/></h4>
                    <ul>
                        <t t-foreach="item[1]" t-as="book">
                            <li><span t-field="book.title"/> (<span t-field="book.pages"/> pages)</li>
                        </t>
                    </ul>
                </t>
            </div>
        </t>
    </t>
</template>
```

---

## 6.4 Excel Reports (xlsx)

**__manifest__.py:**
```python
'external_dependencies': {
    'python': ['xlsxwriter'],
},
```

**models/library_book.py:**
```python
import io
import base64
from odoo import models, fields
from odoo.exceptions import UserError

class LibraryBook(models.Model):
    _name = 'library.book'

    def action_export_xlsx(self):
        """Export books to Excel"""
        try:
            import xlsxwriter
        except ImportError:
            raise UserError('Please install xlsxwriter: pip install xlsxwriter')

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Books')

        # Header format
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#4CAF50',
            'font_color': 'white',
        })

        # Headers
        headers = ['ID', 'Title', 'ISBN', 'Pages', 'State']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header, header_format)

        # Data
        row = 1
        for book in self:
            worksheet.write(row, 0, book.id)
            worksheet.write(row, 1, book.title)
            worksheet.write(row, 2, book.isbn or '')
            worksheet.write(row, 3, book.pages)
            worksheet.write(row, 4, book.state)
            row += 1

        # Adjust column widths
        worksheet.set_column('B:B', 30)  # Title column

        workbook.close()
        output.seek(0)

        # Return download action
        attachment = self.env['ir.attachment'].create({
            'name': 'books_export.xlsx',
            'type': 'binary',
            'datas': base64.b64encode(output.read()),
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'new',
        }
```

---

## ✅ Part 6 Summary Checklist

- [ ] Create QWeb reports with ir.actions.report
- [ ] Use QWeb directives (t-foreach, t-if, t-field, t-esc)
- [ ] Customize reports with Python (AbstractModel)
- [ ] Generate Excel reports with xlsxwriter

---

# Part 7: Best Practices & Real Examples

## 7.1 Module Development Best Practices

**1. Follow Odoo Coding Guidelines**
```python
# ✅ Good: Clear naming, docstrings, type hints
class LibraryBook(models.Model):
    """Library Book Management"""
    _name = 'library.book'
    _description = 'Library Book'

    def action_set_available(self):
        """Mark book as available for borrowing"""
        self.write({'state': 'available'})
        return True

# ❌ Bad: No docstrings, unclear names
class Book(models.Model):
    _name = 'lib.book'

    def avail(self):
        self.write({'s': 'a'})
```

**2. Proper Model Structure**
```python
# ✅ Good: Logical grouping
class LibraryBook(models.Model):
    _name = 'library.book'

    # 1. Private attributes (_name, _description, etc.)
    # 2. Fields (in logical groups)
    # 3. Compute methods
    # 4. Constrains
    # 5. Onchange methods
    # 6. CRUD overrides
    # 7. Action methods
    # 8. Business logic methods
```

**3. Use SQL Constraints**
```python
# ✅ Good: Database-level constraint
_sql_constraints = [
    ('isbn_unique', 'unique(isbn)', 'ISBN must be unique!'),
]

# ❌ Bad: Only Python constraint (slower, can be bypassed)
@api.constrains('isbn')
def _check_isbn_unique(self):
    if self.search_count([('isbn', '=', self.isbn)]) > 1:
        raise ValidationError('ISBN must be unique!')
```

**4. Efficient Recordset Operations**
```python
# ✅ Good: Batch operations
books = self.env['library.book'].search([('state', '=', 'draft')])
books.write({'state': 'available'})

# ❌ Bad: Loop with single writes
books = self.env['library.book'].search([('state', '=', 'draft')])
for book in books:
    book.write({'state': 'available'})  # N queries!
```

**5. Use @api.depends Correctly**
```python
# ✅ Good: Explicit dependencies
@api.depends('line_ids.price_subtotal')
def _compute_total(self):
    for record in self:
        record.total = sum(record.line_ids.mapped('price_subtotal'))

# ❌ Bad: Missing dependencies (won't recompute)
def _compute_total(self):
    for record in self:
        record.total = sum(record.line_ids.mapped('price_subtotal'))
```

---

## 7.2 Performance Optimization

**1. Avoid N+1 Queries**
```python
# ✅ Good: Prefetch related data
books = self.env['library.book'].search([]).mapped('publisher_id.name')

# ❌ Bad: N queries (1 for books + N for publishers)
books = self.env['library.book'].search([])
for book in books:
    print(book.publisher_id.name)  # Query per book!
```

**2. Use read() for List Views**
```python
# ✅ Good: Lightweight read
books_data = self.env['library.book'].search([]).read(['title', 'isbn'])

# ❌ Bad: Load entire recordset
books = self.env['library.book'].search([])
for book in books:
    data = {'title': book.title, 'isbn': book.isbn}
```

**3. Limit Search Results**
```python
# ✅ Good: Pagination
books = self.env['library.book'].search([], limit=100, offset=0)

# ❌ Bad: Load all records
books = self.env['library.book'].search([])
```

**4. Use SQL for Bulk Operations**
```python
# ✅ Good: Direct SQL (when performance critical)
self.env.cr.execute("""
    UPDATE library_book
    SET state = 'available'
    WHERE state = 'draft'
""")

# ❌ Bad: ORM (slower for bulk updates)
books = self.env['library.book'].search([('state', '=', 'draft')])
books.write({'state': 'available'})
```

---

## 7.3 Common Patterns & Solutions

**Pattern 1: Sequence Generator**
```python
# data/ir_sequence_data.xml
<record id="seq_library_book" model="ir.sequence">
    <field name="name">Library Book Sequence</field>
    <field name="code">library.book</field>
    <field name="prefix">BOOK-</field>
    <field name="padding">5</field>
    <field name="number_next">1</field>
</record>

# models/library_book.py
@api.model
def create(self, vals):
    if not vals.get('name'):
        vals['name'] = self.env['ir.sequence'].next_by_code('library.book') or 'New'
    return super().create(vals)
```

**Pattern 2: Scheduled Actions (Cron)**
```xml
<record id="cron_send_overdue_reminders" model="ir.cron">
    <field name="name">Send Overdue Reminders</field>
    <field name="model_id" ref="model_library_borrowing"/>
    <field name="state">code</field>
    <field name="code">model.send_overdue_reminders()</field>
    <field name="interval_number">1</field>
    <field name="interval_type">days</field>
    <field name="numbercall">-1</field>  <!-- Repeat forever -->
    <field name="doall" eval="False"/>
</record>
```

```python
# models/library_borrowing.py
def send_overdue_reminders(self):
    overdue_borrowings = self.search([
        ('state', '=', 'borrowed'),
        ('return_date', '<', fields.Date.today()),
    ])
    for borrowing in overdue_borrowings:
        borrowing.member_id.send_email_reminder()
```

**Pattern 3: Automated Actions (Workflow)**
```xml
<record id="automated_action_book_borrowed" model="base.automation">
    <field name="name">Notify when book borrowed</field>
    <field name="model_id" ref="model_library_borrowing"/>
    <field name="trigger">on_create</field>
    <field name="state">code</field>
    <field name="code">
        for record in records:
            record.book_id.message_post(
                body="Book borrowed by %s" % record.member_id.name,
                subject="Book Borrowed"
            )
    </field>
</record>
```

---

## 7.4 Real-World Example: Complete Module

**Scenario:** Library Management with Borrowing Workflow

**Module Structure:**
```
library_management/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── library_book.py
│   ├── library_member.py
│   ├── library_borrowing.py
│   └── library_category.py
├── views/
│   ├── library_book_views.xml
│   ├── library_member_views.xml
│   ├── library_borrowing_views.xml
│   └── menu_items.xml
├── security/
│   ├── library_security.xml
│   └── ir.model.access.csv
├── data/
│   ├── ir_sequence_data.xml
│   └── library_category_data.xml
├── reports/
│   └── borrowing_report.xml
├── controllers/
│   └── main.py
└── static/
    └── description/
        └── icon.png
```

**Key Implementation:**

**models/library_borrowing.py:**
```python
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class LibraryBorrowing(models.Model):
    _name = 'library.borrowing'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Library Borrowing'
    _order = 'borrow_date desc'

    name = fields.Char('Reference', required=True, default='New', readonly=True)
    book_id = fields.Many2one('library.book', 'Book', required=True, tracking=True)
    member_id = fields.Many2one('library.member', 'Member', required=True, tracking=True)
    borrow_date = fields.Date('Borrow Date', default=fields.Date.today, required=True)
    due_date = fields.Date('Due Date', compute='_compute_due_date', store=True)
    return_date = fields.Date('Return Date', tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('lost', 'Lost'),
    ], default='draft', required=True, tracking=True)

    is_overdue = fields.Boolean('Overdue', compute='_compute_is_overdue')
    days_overdue = fields.Integer('Days Overdue', compute='_compute_is_overdue')

    @api.depends('borrow_date')
    def _compute_due_date(self):
        for record in self:
            if record.borrow_date:
                record.due_date = record.borrow_date + timedelta(days=14)
            else:
                record.due_date = False

    @api.depends('due_date', 'return_date', 'state')
    def _compute_is_overdue(self):
        today = fields.Date.today()
        for record in self:
            if record.state == 'borrowed' and record.due_date < today:
                record.is_overdue = True
                record.days_overdue = (today - record.due_date).days
            else:
                record.is_overdue = False
                record.days_overdue = 0

    @api.constrains('book_id', 'state')
    def _check_book_available(self):
        for record in self:
            if record.state == 'borrowed':
                other_borrowing = self.search([
                    ('book_id', '=', record.book_id.id),
                    ('state', '=', 'borrowed'),
                    ('id', '!=', record.id),
                ])
                if other_borrowing:
                    raise ValidationError('This book is already borrowed!')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('library.borrowing') or 'New'
        return super().create(vals)

    def action_confirm(self):
        self.write({'state': 'borrowed'})
        self.book_id.write({'state': 'borrowed'})
        self.message_post(body="Book borrowed successfully")

    def action_return(self):
        self.write({
            'state': 'returned',
            'return_date': fields.Date.today(),
        })
        self.book_id.write({'state': 'available'})
        self.message_post(body="Book returned successfully")
```

---

## ✅ Part 7 Summary Checklist

- [ ] Follow Odoo coding guidelines (naming, docstrings)
- [ ] Structure models logically (fields, compute, business logic)
- [ ] Use SQL constraints for uniqueness
- [ ] Optimize recordset operations (batch writes, avoid N+1)
- [ ] Implement common patterns (sequences, cron, automated actions)
- [ ] Build complete modules with proper structure

---

# Final Summary: Your Odoo Development Expertise

## What You've Mastered (~2,500 Lines of Knowledge)

**Part 1: Architecture & Setup** ✅
- Odoo 3-tier architecture
- Module structure (__manifest__.py, models/, views/, security/)
- Development environment setup (Docker, source)
- 3 inheritance types (Class, Prototype, Delegation)

**Part 2: Models & ORM** ✅
- Field types (Char, Integer, Many2one, One2many, Binary, etc.)
- Field attributes (required, readonly, compute, domain)
- CRUD operations (create, search, write, unlink)
- Domain filters, API decorators (@api.depends, @api.constrains)
- Recordset operations, Environment (self.env)

**Part 3: Views & XML** ✅
- Form views (header, sheet, groups, notebooks)
- Tree views (colors, editable, buttons)
- Search views (filters, group by)
- Kanban, Calendar, Graph, Pivot views
- Actions (window, server, URL), Menus
- Field widgets

**Part 4: Security** ✅
- Security groups (user, manager)
- Access rights (ir.model.access.csv)
- Record rules (row-level security)
- Field-level security
- sudo() bypass

**Part 5: Controllers & APIs** ✅
- HTTP controllers (@http.route)
- XML-RPC API (external access)
- REST API implementation
- Webhooks

**Part 6: Reports** ✅
- QWeb reports (ir.actions.report)
- QWeb directives (t-foreach, t-if, t-field)
- Custom reports with Python
- Excel reports (xlsxwriter)

**Part 7: Best Practices** ✅
- Coding guidelines
- Performance optimization (avoid N+1, use read())
- Common patterns (sequences, cron, automated actions)
- Real-world complete module example

---

## Quick Reference: Common Tasks

**Create a new module:**
```bash
odoo-bin scaffold my_module /path/to/addons
```

**Update module:**
```bash
odoo-bin -c odoo.conf -u my_module -d my_database
```

**Debug mode:**
```
http://localhost:8069/?debug=1
```

**Access Odoo shell:**
```bash
odoo-bin shell -c odoo.conf -d my_database
```

**Common commands in shell:**
```python
# Search records
self.env['res.partner'].search([('is_company', '=', True)], limit=10)

# Create record
self.env['res.partner'].create({'name': 'Test Company', 'is_company': True})

# Access current user
self.env.user.name
```

---

## Resources for Continued Learning

**Official Documentation:**
- Odoo Developer Documentation: https://www.odoo.com/documentation/17.0/developer.html
- Odoo API Reference: https://www.odoo.com/documentation/17.0/developer/reference.html

**GitHub:**
- Odoo Source Code: https://github.com/odoo/odoo
- Odoo Community Addons: https://github.com/OCA

**Communities:**
- Odoo Forums: https://www.odoo.com/forum
- Odoo Community Association: https://odoo-community.org

**Books:**
- "Odoo 17 Development Essentials" by Daniel Reis
- "Odoo Development Cookbook" by Holger Brunn

---

## 🎓 Congratulations!

You've completed the **Odoo Development Skill**. You now have comprehensive knowledge of:

✅ Odoo architecture and module development
✅ Python ORM (models, fields, methods, decorators)
✅ XML views (form, tree, kanban, search, calendar)
✅ Security (groups, access rights, record rules)
✅ Controllers & APIs (HTTP, JSON-RPC, XML-RPC, REST)
✅ Reports (QWeb, PDF, Excel)
✅ Best practices and real-world patterns

**Total Content:** ~2,500 lines of expert-level Odoo development knowledge

**Next Steps:**
1. Build your own custom module (start simple!)
2. Contribute to OCA (Odoo Community Association)
3. Practice by customizing existing modules
4. Join Odoo forums and help others

**Remember:** Odoo development is 60% Python + 30% XML + 10% JavaScript. Master Python ORM and XML views first!

Good luck on your Odoo development journey! 🚀

---

---

## 🔧 CODING ULTIMATE STACK: Must Load Together

**This skill is Layer 3: Implementation of THE CODING ULTIMATE STACK system.**

### Same Layer (Implementation - Load All 8):
- `python-best-practices-skill` - Pythonic code, PEP 8, type hints
- `javascript-modern-skill` - ES6+, async/await, modern JS
- `code-quality-standards-skill` - Clean code, SOLID, refactoring, code smells
- `automation-workflows-skill` - Workflow automation, batch processing
- `document-conversion-skill` - MD → PDF, HTML → PDF, Pandoc
- `excel-expert-skill` - Data manipulation, advanced Excel
- `ffmpeg-video-processing-skill` - Video processing pipelines

### Next Layer (Quality & Testing - Load 3-5):
- `code-quality-standards-skill` - Clean code, SOLID, refactoring, code smells
- `debug-methodology-skill` - Codex systematic debugging, trace execution
- `security-best-practices-skill` - OWASP, authentication, security audit
- `git-safety-skill` - Safe version control, branching strategies

### Deployment Layer (Load 2-3):
- `git-safety-skill` - Safe version control, branching strategies
- `automation-workflows-skill` - Workflow automation, batch processing
- `security-best-practices-skill` - OWASP, authentication, security audit

### Auto-Loading Modes:
- **Default Stack (12 skills):** Triggers on "code", "เขียนโค้ด", "programming"
- **Aggressive Stack (18 skills):** Triggers on "architecture", "scalability", "รีแฟคเตอร์"
- **Ultimate Stack (25 skills):** Triggers on "ultimate stack", "production-ready", "ช่วยเต็มที่"

### Pro Workflow:
1. **Novice:** Use this skill alone → Basic implementation
2. **Intermediate:** This + 2-3 same-layer skills → 2-3x quality
3. **Expert:** Full Layer 3 + all layers → Production-grade code

**Power Level:** This skill + full stack = 800/1000 (maximum development expertise)
