const observer = new IntersectionObserver((entries) => {
    entries.forEach((Entry) => {
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        }
        else{
            entry.target.classList.remove('show');
        }
    });
}); 


const hiddenElements = document.querySelectorAll('.img1');
hiddenElements.forEach((el) => observer.observe(el));