document.querySelectorAll('.cards').forEach(function(card) {
    card.addEventListener('mouseover', function() {
        card.style.transform = 'translateY(-5px)';
        card.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.15)';
    });
    card.addEventListener('mouseout', function() {
        card.style.transform = 'translateY(0)';
        card.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.1)';
    });
});