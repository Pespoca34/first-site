const starField = document.querySelector('.stars');
const numberOfStars = 300; 

for (let i = 0; i < numberOfStars; i++) {
    const star = document.createElement('div');
    star.classList.add('star');
    
    const size = Math.random() * 4 + 1; 
    const positionX = Math.random() * window.innerWidth;
    const positionY = Math.random() * window.innerHeight; 
    const animationDuration = Math.random() * 10 + 10; 

    star.style.width = `${size}px`;
    star.style.height = `${size}px`;
    star.style.left = `${positionX}px`;
    star.style.top = `${positionY}px`;
    star.style.animationDuration = `${animationDuration}s`;

    starField.appendChild(star);
}
