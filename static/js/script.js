function kickBall() {
    const ball = document.getElementById("football");
    const result = document.getElementById("result");
  
    // Step 1: Reset ball position instantly
    ball.style.transition = "none"; // Disable move animation
    ball.style.transform = "translate(0, 0)"; // Move ball back to the starting position
    
    // Allow the browser to render the reset position
    setTimeout(() => {
      // Step 2: Re-enable transition for smooth animation
      ball.style.transition = "transform 0.8s ease-out ";  //Move animation
  
      // Define the area (this can be customized)
      const maxWidth = 700; // Custom area width max
      const minWidth = 600; // Custom area width min
      const maxHeight = 120; // Custom area height max & min
  
      // Generate random positions within the defined area
      const randomX = Math.floor(Math.random() * (maxWidth - minWidth + 1)) + minWidth; // Random X within the area
      const randomY = Math.floor(Math.random() * maxHeight); // Random Y within the area
  
      // Move ball to random position
      ball.style.transform = `translate(${randomX}px, ${-randomY}px)`; // You can adjust the Y-axis transformation as needed
  
      // Define preset messages
      const messages = [
        '"We Won the League in Manchester..."',
        '"We are the Arsenal"',
        '"North London is red"',
        '"Come on you Gunners!"',
        '"Victoria Concordia Crescit"',
        '"We don\'t buy superstars, we make them"',
        '"The Arsenal way"',
        '"Always believe"',
        '"Once a Gooner, always a Gooner"'
      ];
  
      // Randomly choose a message from the array
      const randomMessage = messages[Math.floor(Math.random() * messages.length)];
  
      // Check if the ball is inside a defined "goal area" after animation
      setTimeout(() => {
        // Consider a goal area within a specific region (x: 0-500, y: 0-100)
        if (randomX > 500 && randomX < 800 && randomY > 0 && randomY < 200) {
          result.innerText = randomMessage;
          result.style.color = "black";
        }
      }, 1000); // Wait for the animation to finish
    }, 50); // Small delay to visually reset the ball
  }
  
  // Get the modal element and button
  const modal = document.getElementById("myModal");
  const modalButtons = document.querySelectorAll(".modal-btn");
  
  modalButtons.forEach((button) => {
    button.addEventListener("click", () => {

      //show the modal
      modal.style.display = "flex";

      // Hide the modal after 3 seconds
      setTimeout(() => {
        modal.style.display = "none";
      }, 3000); //1000 milliseconds = 1 seconds
    });
  });

  document.addEventListener("DOMContentLoaded", function () {
    const messages = document.getElementById("message-display");
    if (messages) {
      setTimeout(() => {
        messages.style.display = "none";
      }, 5000);
    }
  });
  