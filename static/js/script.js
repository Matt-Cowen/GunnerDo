document.addEventListener('DOMContentLoaded', () => {
    // Find all <tr> elements
    const trElements = document.querySelectorAll('tr');

    trElements.forEach((trElement) => {
        // Locate the specific <td> with id "task-progress" within the row
        const progressElement = trElement.querySelector('#task-progress');

        if (progressElement && progressElement.textContent.includes('Full-time')) {
            // Apply the class or styles if the text contains "Full-time"
            trElement.style.display = 'block'; // Change <tr> to block for styling
            Object.assign(trElement.style, {
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                position: 'fixed',
                top: '50%',
                right: '10px',
                transform: 'translateY(-50%)',
                width: '100px',
                height: '100px',
                borderRadius: '50%',
                backgroundColor: '#f0f0f0',
                boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
                zIndex: '1000',
            });
        }
    });
});
