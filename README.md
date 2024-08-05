## UL finder
### Description
Python script receives the URL to a website as a command line
argument, retrieves the HTML web page content, finds the HTML 
unordered list with the most direct children, 
and returns the last list item from that list.

### Start script
Script is writen with `Python3`. For the script to work properly, 
make sure you have installed `Python 3.11` version on your machine.

*Start script* by executing `greatest_ul_last_li`. 
You should correspond url of a html file as argument by `-u, --url`
option. 

### Simple server
If you need to use `example.html`, you may start python simple 
server in new terminal window. Make sure you are in `ul_finder` directory.

```python3 -m http.server```

Next you could use URL: `http://localhost:8000/example.html`