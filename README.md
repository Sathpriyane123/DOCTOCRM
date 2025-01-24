# Docoto Customer Relationship Software

## Overview
Docoto Customer Relationship Software is a web-based application designed to help businesses manage customer interactions, improve relationships, and optimize sales processes. This system provides tools for tracking customer data, managing leads, and analyzing customer behavior, all through an integrated platform.

## Features
- **Customer Management**: Register, update, and view customer profiles.
- **Lead Management**: Track and manage potential customer leads.
- **Sales Tracking**: Monitor sales activities and performance.
- **Reports and Analytics**: Generate detailed reports for customer insights and sales trends.
- **Task Management**: Assign and manage tasks for team members.
- **Communication Tools**: Log and track customer interactions via calls, emails, and meetings.

## Technologies Used
### Backend:
- **Python**: Programming language.
- **Django**: Backend framework for building robust web applications.

### Frontend:
- **HTML5**: Markup language for structuring content.
- **CSS3**: Styling the web pages.
- **Bootstrap**: Responsive design and styling framework.
- **JavaScript**: Adding interactivity to the web pages.

### Database:
- **SQLite** (default Django database) or MySql (optional).

### Tools and Libraries:
- **Django REST Framework**: For building RESTful APIs.
- **jQuery**: Simplify DOM manipulation and AJAX requests.
- **Font Awesome**: For icons.
- **Chart.js**: For creating reports and data visualization.

## Installation
### Prerequisites
- Python 3.9+
- Node.js (optional for advanced JS features)
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sathpriyane123/DOCTOCRM.git
   cd DOCTOCRM
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`.

## Usage
1. **Login**: Use the superuser credentials to log in as an admin.
2. **Dashboard**: Access the dashboard to view key metrics and navigate through the system.
3. **Manage Customers**: Add, update, or delete customer profiles.
4. **Leads**: Track and manage sales leads.
5. **Sales Tracking**: Monitor and update sales activities.
6. **Reports**: Generate and download customer and sales reports.



## Future Enhancements
- Integration with third-party email and communication platforms.
- Advanced AI-driven insights for customer behavior prediction.
- Mobile-friendly version for on-the-go management.
- Multi-language support for global usability.


## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## Contact
For queries or support, please contact:
- **Name**: Sathpriyan
- **Email**: sathpriyaneshaji@gmail.com

