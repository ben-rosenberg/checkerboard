# CHECKERBOARD

I'm really happy with this solution aside from the implementation of the color changing functionality. I'm sure there's a way to avoid the inline styling, but I couldn't figure out a way to use Jinja in the stylesheet itself. I also briefly tried using JavaScript by making `changeColor1()` and `changeColor2()` functions with a `querySelector()` and `style.backgroundColor()`, but I couldn't find a way to call the changeColor functions in a way that would pass in the string for the color from Jinja.