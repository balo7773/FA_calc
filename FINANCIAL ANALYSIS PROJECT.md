**FINANCIAL ANALYSIS PROJECT**

Overview:

* Name → FA APP  
* Purpose → To run an analysis on the company’s financial report, and give insight into the company’s performance as seen in the report.  
* Scope:  
  * What it will do;  
    * Calculate financial ratios by the user providing input (**spanning from a single FY to multiple FYs**).  
    * Give insight based on the ratios given.  
    * Plot graphs based on ratios and past FY input.  
    * Predict future FY performance using simulation methods (**OPTIONAL**).  
  * What it won’t do;  
    * It won’t take inputs from PDF or any other document for now.  
    * It won’t make an investment decision for the user, only provide insight based on the input the user has given.

Requirements

* Core Features:  
  * A dialog box for the user to provide input  
  * Calculation of financial ratios and user-defined financial ratios  
  * Plotting of graphs  
  * Giving a final summary/insight based on what the user provides as input  
  * Compare the financial performance between companies (up to 5\) with a showcasing graph of their performance, also giving a final summary/insight on them.  
* Optional Features:  
  * Print the final report in HTML or PDF format  
  * Read the financial report from documents such as Excel, PDF, and SQL format  
  * Use of AI to streamline the process  
  * Fetching data from online sources using APIs to calculate ratios and give a summary without user input  
  * Optimization of a portfolio based on various financial instruments' risk and returns  
* Non-Functional Features:  
  * Should be able to accept up to 8 FY reports as input, and speed should not be affected either in processing or giving the final result  
  * Processing and Output should be returned quickly without much time being used  
  * Invalid financial inputs should be treated as an error so as not to crash the program  
  * Errors and edge cases should be taken note of  
  * Logs should be recorded

Design

* Tech Stack:  
  * Backend:  
    * Django or Fast Api  
    * Database: Mysql or mongodb  
    * Graph plotter: Plotly or matplotlib  
    * Numerical computing: Numpy and Scikit learn  
    * Data Structure and Analysis: Pandas  
    * ORM: SQLALCHEMY or ODM: PyMongo  
    * Language: Python  
  * Frontend:  
    * Reactjs or Jinja template  
    * HTML, CSS, and JS  
* Architecture Sketch:  
  * User gives input through the frontend  
  * Frontend sends an API request to the backend  
  * Backend receives the request, validates input, processes it, and sends it back to the frontend  
  * The result is sent to the frontend, and it is displayed to the user through the  frontend  
* UI mockups/wireframes(contractual):  
  * Home page:  
    * Navbar  
      * Home  
      * Financial Analyzer
      * Heatmap(from TradingView to know trending stocks)  
      * Curated Indices (previously 'Specific stocks checkout')
      * About Project  
      * Login/sign up button  
    * Carousel after the nav bar, saying something about companies  
    * A nice 3d spinning Naira currency  
    * A beautiful layout to be decided by the UI designer  
    * Footer  
  * Financial Analyzer page:  
    * Box to choose which sector to be analyzed due to the variation of different FY reporting standards  
    * Box to choose how many years are to be analyzed  
    * Inputs are given based on sector standards  
    * Toggle button to enable user-defined ratios  
    * A button that sends inputs to the backend for processing  
  * Heatmap page:  
    * Stock on the ngx gain and loss shown by TradingView heatmap  
    * Clicking on each stock takes you to a personal page where a chart is shown and other info provided by TradingView (optional)

  * Curated Indices page:  
    * Hardcoded analysis of specific stocks showing their past performance and present performance to be updated through the admin panel  
    * These specific stocks will be classified into:  
      * Dangote Index or Dang Index  
      * Mr TOE index  
      * BUA index  
      * Top Oil and Gas Index  
  * About page:  
    * Contains the purpose of the project and the contact information of the engineers  
  * User page:  
    * Contains user info  
    * NB: not necessarily compulsory except the user wants to do analysis of multiple sectors

Deployment

* At first, local servers(PC)  
* Virtual Servers(if cost allows, we use dedicated VM)  
* Docker for containerization   
* Nginx and HAProxy (remind me what this is used for)

Timeline:

* To be discussed with my partner since it's a personal project

Risk/Constraints

* Wrong result provided to the user, there should be a flag button for this, or feedback  
* A hacker is trying to hack the user's info  
* Code compromised or stolen by a hacker