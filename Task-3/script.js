document.addEventListener("keypress",function(event) {
    play(event.key);
});

function play(keys)
{
    switch(keys){

        case "w":
            
            var plate = new Audio("sounds/crash.mp3");
            plate.play();
            break;
        
        case "a":
            
            var plate = new Audio("sounds/kick-bass.mp3");
            plate.play();
            break;
        case "s":
            
            var plate = new Audio("sounds/snare.mp3");
            plate.play();
            break;
        case "d":
            
            var plate = new Audio("sounds/tom-1.mp3");
            plate.play();
            break;
        case "j":
            
            var plate = new Audio("sounds/tom-2.mp3");
            plate.play();
            break;
        case "k":
            
            var plate = new Audio("sounds/tom-3.mp3");
            plate.play();
            break;
        case "l":
            
            var plate = new Audio("sounds/tom-4.mp3");
            plate.play();
            break;
        
        default: console.log('no key pressed');
            
    }   

}

