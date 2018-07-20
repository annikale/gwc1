//Global Score
let nameScore = 0;
let computerScore = 0;
let name;
const logo = "bplogo.png";


//Say Hi to the Player
//Listen for the click on the "Click Me" button
document.getElementById("name-button").addEventListener("click", function(){
  //get the value in the text box
  name = document.querySelector(".player-name").value;
  //say hello to the player using their stated name
  alert("Hi " + name + ". Are you ready to play?");
});

//Randomize the images
//A function is a recipe we can use over and over.
//Name a function based on what it is doing
function randomizeImage(){
  //An array of our images
  const image = ["blackpanther.png", "killmonger.png", "shuri.png"];
  //Get a random number
  let imageNumber = Math.floor(Math.random() * 3);
  console.log(imageNumber);
  //Choose the image based on the random number
  let newImage = image[imageNumber]
  return (newImage);
}

//Find the winner
function findWinner(nameScore, computerScore){
    $("#text").text("Your score is: " + nameScore + ". The computer score is " + computerScore + ".");
    //if your score is 15 - update the score in the DOM
  if (nameScore === 15){
      $("#text").text(name + ", You won!");
    } else if (computerScore === 15) {
      $("#text").text("Sorry, " + name + " the computer won!");
    }
}

//Click on a Card
$(".cards").on("click", ".face-card", function(){
  let randomImage = randomizeImage();
  $(this).closest("img").attr("src", randomImage);
  if (randomImage === "shuri.png") {
    nameScore += 5;
    findWinner(nameScore, computerScore);
  } else if (randomImage === "claw.png"){
  } else {
    computerScore += 5;
    findWinner(nameScore, computerScore);
      }
  $("#tryagain-button").on("click", () => {
    $(this).attr("src", logo);
  });
});


