// Wait for the HTML document to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {

    // --- Select the buttons and their target sections ---

    // Select the "Get Started" button
    const getStartedBtn = document.querySelector('.btn-primary');

    // Select the "Explore Modules" button
    const exploreModulesBtn = document.querySelector('.btn-secondary');

    // Select the target for the "Get Started" button (the Admin module card)
    const adminModuleTarget = document.getElementById('admin-operations');

    // Select the target for the "Explore Modules" button (the entire modules section)
    const modulesSectionTarget = document.getElementById('modules-section');


    // --- Add click event listeners to the buttons ---

    // Add functionality to the "Get Started" button
    if (getStartedBtn && adminModuleTarget) {
        getStartedBtn.addEventListener('click', function(event) {
            // Prevent the default link behavior (jumping to the top of the page)
            event.preventDefault();

            // Scroll the admin module into view with a smooth animation,
            // positioning it in the center of the screen.
            adminModuleTarget.scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            });
        });
    }

    // Add functionality to the "Explore Modules" button
    if (exploreModulesBtn && modulesSectionTarget) {
        exploreModulesBtn.addEventListener('click', function(event) {
            // Prevent the default link behavior
            event.preventDefault();

            // Scroll the modules section into view with a smooth animation,
            // aligning its top with the top of the browser window.
            modulesSectionTarget.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        });
    }

});