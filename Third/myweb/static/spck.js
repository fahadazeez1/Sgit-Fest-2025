document.querySelectorAll('.faqbox').forEach(faqbox => {
    faqbox.addEventListener('click', () => {
        // Close all open FAQ boxes
        document.querySelectorAll('.faqbox').forEach(box => {
            if (box !== faqbox) {
                box.classList.remove('active');
            }
        });
        // Toggle the clicked FAQ box
        faqbox.classList.toggle('active');
    });
});
