Setup Instructions
1. Prerequisites
    Python 3.x installed on your system.
    MySQL installed on your system.
2. Clone the Repository
    `git clone https://github.com/JaiPrasanth077/Ini8.git`
    `cd Ini8`
3. Install Dependencies
    Install the required Python dependencies using pip:
       `pip install mysql-connector-python`
4. Set Up MySQL Database
    Ensure MySQL is running on your local machine.
    Create a MySQL database named "Registration", with the following query:
          ` create table registration(
               id int primary key auto_increment,
               name varchar(255) not null,
               email varchar(255) not null,
               DOB date,
               contactnum varchar(20) unique
               );`
5. Run the Application
    Run the Python script (crud.py) to start the registration system:
       Upon running the application, you will be presented with a menu where you can choose various options:
           1. Create a new registration.
           2. Read existing registration details.
           3. Update registration information.
           4. Delete a registration.
           5. Exit the application.
       Follow the prompts to perform the desired operation.



If you have any questions or encounter any issues,please let me know.Thanks in advance!!
