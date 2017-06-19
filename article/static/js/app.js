$(document).ready(function() {
    $('#mainSlider').slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        prevArrow: $('#pressPrev'),
        nextArrow: $('#pressNext')
    });

    $('.popup-modal').magnificPopup({
        type: 'inline',
        removalDelay: 300,
        tClose: 'Закрыть (ESC)',
        mainClass: 'mfp-fade',
    });
});
