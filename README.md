<!DOCTYPE html>
 <html lang="en-US">
<body>

<h1>StockTracker</h1>
<p>This page is the offical documentation for downloading and running the code in this code base.</p>
<h2>Update:</h2>
<p>This project is no longer in develoment. Attempting to build this project will work because the required API keys and MongoDB servers code has been removed. This project has been made public so others may learn from it's existence.</p>

<h2>Preview</h2>
<img src="https://github.com/user-attachments/assets/afdd8c67-445b-49b8-aad0-a66940fecdfe" alt="Image of the app working" />

<h2>Notes about the READMEs</h2>
<p>It is very important that you read all README.md files before attempting a system test, or a unit test of certain systems here is a list of all README files:</p>

<ol>
 <li><a href="https://github.com/key6oardWarrior/StockTracker/blob/main/README.md">/main/README.md</a> (the one your reading)</li>
 <li><a href="https://github.com/key6oardWarrior/StockTracker/blob/main/Helper/README.md">/main/Helper/helper.py/README.md</a> (used for fixing bugs in imported package)</li>
 <li><a href="https://github.com/key6oardWarrior/StockTracker/blob/main/UnitTest/Login/README.md">/main/UnitTest/Login/README.md</a> (used for unit testing)</li>
 <li><a href="https://github.com/key6oardWarrior/StockTracker/blob/main/UnitTest/Helper/README.md">/main/UnitTest/Helper/README.md</a> (used for unit testing)</li>
 <li><a href="https://github.com/key6oardWarrior/StockTracker/blob/main/Robinhood_API/README.md">/main/Robinhoon_API/README.md</a> (used for find robin_stocks docs)</li>
 <li><a href="https://github.com/key6oardWarrior/StockTracker/blob/main/UnitTest/Database/README.md">/main/UnitTest/Database/README.md</a> (used for fixing SSL cert error and set <code>connectionString</code>)</li>
</ol>

<h2>How to Download and Setup</h2>
<ol>
	<li>Download <a href="https://www.python.org/downloads/release/python-3111/">Python v3.11.1</a>. The app most likely will run on older or newer versions of Python 3, but that has not been tested.</li>
	<li>Run <code>git clone <a href="https://github.com/key6oardWarrior/StockTracker">https://github.com/key6oardWarrior/StockTracker</a></code></li>
	<li><code>cd [dir that cloned StockTrader]</code></li>
	<li><code>py -m pip install -r Dependencies/requirements.txt</code> This will install all the need python dependencies. If you have any more issues read the other README.md files</li>
	<li><code>py installer.py</code></li>
	<li><code>py compile.py</code></li>
	<p>Please note that while running compile.py you may encounter an error that states, "Can't list [directory]." Please ignore this error message. A desktop shortcut will be created use that shortcut to run the application.</p>
</ol>

<h2>Note</h2>
<p>Nothing on this application is financial advice and there is no guarantee that any user will profit from using this application. Any data entered into this app will not be stored on the user's computer or another server. When a user wants to see "the last 5 days of trading" from congress members you will see the last 5 days that congress members reported their trades. For example, if the date is Jan 3, 2024 and congress member A sells 3 shares of Apple on June 5, 2022, but reports that trade on Jan 2, 2024 and a user requested to see the last 5 days of trading then the user will see that congress member A made the sale yesterday. Be sure to check the transaction date because it may be different from the reported date. Also keep in mind that the law requires congress persons to report their trades within 45 days after making the trade; however, many congress persons break the law and report their trades late (sometimes VERY late).</p>

 </body>
<html>
