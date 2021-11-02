const linksSection = document.getElementById('js-section');

function scrollToSection(event){
    event.preventDefault();
    const href = event.currentTarget.getAttribute('href');
    const section = document.querySelector(href);
    const positionInicialSection = section.offsetTop;
    console.log(href);
    console.log(positionInicialSection);
    window.scrollTo({
        top: positionInicialSection, // 128 corresponde ao tamanho do header que sera descontado (8rem * 16)
        behavior: 'smooth',
    })
}

linksSection.addEventListener('click', scrollToSection);