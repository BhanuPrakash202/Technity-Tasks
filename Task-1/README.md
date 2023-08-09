<h1>Approach</h1>
1.<strong>Initial Setup: </strong>Started with background and navbar design.<br>
2.<strong>Layout Structures: </strong>Used flexbox for text and image alignment.<br>
3.<strong>Icon Usage: </strong>Added icons from Google search for visual enhancement.<br>
4.<strong>Finalization: </strong>Tweaked text styles, adjusted area sizes.<br><br>
HTML code:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="styles.css">
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
    <title>Document</title>
    <script src="https://kit.fontawesome.com/c7dc5382f5.js" crossorigin="anonymous"></script>
</head>
<body>
    <div class="plate">
        <nav>
            <div class="logo">
                <a href="##">Create.co</a>
            </div>
            <ul class="pages">
                <li><a href="#">Home</a></li>
                <li><a href="#">Service</a></li>
                <li><a href="#">Team</a></li>
                <li><a href="#">Blog</a></li>
                <li><a href="#">Contact Us</a></li>
            </ul>
            <ul class="pages-right">
                <li><a href="#" id="pages a">Login</a></li>
                <li><a href="#" class="getstart">Getting Started</a></li>
            </ul>
        </nav>
    
    
        <div class="inner-plate">   
            <div class="text">
                <p><strong class="blue"> Grow Your Business<br>
                    With</strong> <strong class="red"> Social Media <br>marketing</strong></p>
                <p class="desc">Lorem ipsum dolor sit amet,consectetur adipiscing <br> elit. Aliquam consectetur venenatis blandit. Praesent<br>vehicula, libero non pretium vulputate minecraft op</p>
                <input type="text" name="" id="" placeholder="Email Address" class="Email"><button>Learn more</button><br><br>
                <i class="fa-brands fa-square-instagram" style="color: #5654b3;"></i>
                <i class="fa-brands fa-square-facebook" style="color: #5654b3;"></i>
                <i class="fa-brands fa-square-twitter" style="color: #5654b3"></i>
                <i class="fa-brands fa-square-youtube" style="color: #5654b3"></i>
                <i class="fa-brands fa-square-whatsapp" style="color: #5654b3"></i>
            </div>
            <img src="BASE.png" alt="">
        </div>

</div>

</body>
</html>
```

CSS code:
```
body{
    background-color: #e3f0ff;
    overflow: hidden;
}

.plate{
    padding: 13px;
    margin: 35px;
    border: 25px;
}

nav {
    color: #fff;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
}
  
.logo a {
    font-weight: bolder;
    font-size: 35px;
    color: #2d2c62;
    text-decoration: none;
    font-weight:bold;
    align-content: left;
}
  
.pages {
    list-style: none;
    display:flex;
    justify-content:space-around; 
    color: #2d2c62;

}
  
.pages li {
    margin-right: 30px;
    margin-left: 50px;
    font-size: 13px;
}
  
.pages li a {
    color: #2d2c62;
    text-decoration: none;
}
  
.pages-right {
    list-style: none;
    display: flex;
    font-size: 13px;
}
  
  .pages-right li {
    margin-right: 40px;
  }
  
  .pages-right li a {
    color: 2d2c62;
    text-decoration: none;
  }
.getstart{
    background:#5654b3 ;
    padding: 15px 25px;
    color: white;
    border-radius: 10px;
   
}

img{
    flex: 1;
    width: 55%;
    float: right;
    padding-top: 40px;
    justify-content: left;
    position: fixed;
}

.inner-plate{
    display: flex;
    justify-content: right;

}

.text{
    flex: 1;
    font-size: 40px;
    padding-top: 65px;
}

.blue{
    color:#2d2c62;
}

.red{
    color: #fa676d;
}

.desc{
    font-size:medium;
    color:#a091da;
    font-weight: lighter;
}

input{
    
    border-top-left-radius: 15px;
    border-bottom-left-radius: 15px;
    border: 0;
    padding: 20px;
}

button{
    border: 0;
    background-color: #5654b3;
    color: white;
    padding: 20px 45px;
    border-top-right-radius: 15px;
    border-bottom-right-radius: 15px;
}

i{
    font-size: 30px;
}

html *{
    font-family:"Montserrat";
}
```
