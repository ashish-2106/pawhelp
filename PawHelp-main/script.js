function cursorFollow() {
    let page1Content = document.querySelector(".page1-content")
    let cursor = document.querySelector(".cursor")

    page1Content.addEventListener("mousemove", function (dets) {
        gsap.to(cursor, {
            x: dets.x,
            y: dets.y
        })
    })

    page1Content.addEventListener("mouseenter", function () {
        gsap.to(cursor, {
            scale: 1
        })
    })

    page1Content.addEventListener("mouseleave", function () {
        gsap.to(cursor, {
            scale: 0
        })
    })
}
cursorFollow()


function swiperKaKamal() {
    var swiper = new Swiper(".mySwiper", {
        slidesPerView: 1,
        spaceBetween: 30,
        loop: true,
        autoplay: {
            delay: 2500,
            disableOnInteraction: true,
        }
    });
}
swiperKaKamal()

let time = gsap.timeline()

time.from(".preloader h3", {
    x: 50,
    opacity: 0,
    duration: 1,
    stagger: 0.1
})

time.to(".preloader h3", {
    opacity: 0,
    x: -10,
    duration: 1,
    stagger: 0.1
})

time.to(".preloader", {
    opacity: 0
})
//  main ka text animation hai yaha

time.from(".page1-content h1 span", {
    y: 100,
    opacity: 0,
    duration: 0.5,
    stagger: 0.1,
    delay: -0.5
})
time.to(".preloader", {
    display: "none"
})

time.from(".footer .footer-text h1 span", {
    y: 100,
    opacity: 0,
    duration: 0.5,
    stagger: 0.1,
    delay: 2
})

