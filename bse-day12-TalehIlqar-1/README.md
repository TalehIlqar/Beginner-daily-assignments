# JS  :rocket:

We require you to solve the following tasks. Remember to read the requirements first.

#### Topics you need to know and use to solve tasks

* Selecting DOM Elements in JavaScript
* Styling DOM Elements in JavaScript
* Working with Attributes
* Manipulating DOM Elements in JavaScript
* Navigating Between DOM Nodes


**Final Notes**: *Remember to solve and send assignments on time* :hourglass_flowing_sand:

# Assignments' list 

## Assignment 1  :star:  :star:

### Description

Here is a sample html file with a submit button. Now modify the style of the paragraph text through javascript code.

Sample HTML file :
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset=utf-8 />
    <title>JS DOM paragraph style</title>
  </head> 
  <body>
    <p id ='text'>JavaScript Exercises</p> 
    <div>
    <button id="jsstyle" onclick="js_style()">Style</button>
    </div>
  </body>
</html>
```
Clicking on the button the font, font size, and color of the paragraph text will be changed.


## Assignment 2  :star:  :star:

### Description

Write a JavaScript program to set the background color of a paragraph.


## Assignment 3  :star:  :star:

### Description

Here is a sample html file with a submit button. Write a JavaScript function to get the value of the href, hreflang, rel, target, and type attributes of the specified link.

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset=utf-8 />
  </head>
  <body>
    <p>
      <a id="tech" type="text/html" hreflang="en-us" rel="nofollow" target="_self" href="tech.edu.az">Tech Academy</a>
    </p>
    <button onclick="getAttributes()">Click here to get  attributes value</button>
  </body>
</html>
```

## Assignment 4  :star:  :star:  :star:

### Description

Write a JavaScript function to add rows to a table.
Sample HTML file :

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset=utf-8 />
    <title>Insert row in a table</title>
  </head>
  <body>
    <table id="sampleTable" border="1">
      <tr>
        <td>Row1 cell1</td>
        <td>Row1 cell2</td>
      </tr>
      <tr>
       <td>Row2 cell1</td>
       <td>Row2 cell2</td>
     </tr>
   </table>
   <br>
   <input type="button" onclick="insert_Row()" value="Insert row"> 
  </body>
</html>
```

## Assignment 5  :star:  :star:

### Description

Write a JavaScript program to remove items from a dropdown list.
Sample HTML file :
```
<!DOCTYPE html>
<html>
   <head>
      <meta charset=utf-8 />
      <title>Remove items from a dropdown list</title>
   </head>
   <body>
      <form>
        <select id="colorSelect">
           <option>Red</option>
           <option>Green</option>
           <option>White</option>
           <option>Black</option>
       </select>
      <input type="button" onclick="removecolor()" value="Select and Remove">
      </form>
   </body>
</html>
```

## Assignment 6  :star:  :star:  :star:  :star:

### Description

Write a JavaScript function that creates a table, accept row, column numbers from the user, and input row-column number as content (e.g. Row-0 Column-0) of a cell. 
Sample HTML file :
```
<!DOCTYPE html>
<html>
   <head>
      <meta charset=utf-8 />
      <title>Change the content of a cell</title>
      <style type="text/css">
          body {margin: 30px;}
      </style>  
   </head>
   <body>
      <table id="myTable" border="1">
      </table>
      <form>
         <input type="button" onclick="createTable()" value="Create the table">
      </form>
   </body>
</html>
```


## Assignment 7  :star:  :star:  :star:

### Description

Write a JavaScript program to display a random image (clicking on a button) from the following list.

Sample Image information :
```
"http://farm4.staticflickr.com/3691/11268502654_f28f05966c_m.jpg", width: "240", height: "160"
"http://farm1.staticflickr.com/33/45336904_1aef569b30_n.jpg", width: "320", height: "195"
"http://farm6.staticflickr.com/5211/5384592886_80a512e2c9.jpg", width: "500", height: "343"
```

**Powered by [TechAcademy](https://www.tech.edu.az/)**

