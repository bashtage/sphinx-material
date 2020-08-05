// Source repo: https://github.com/solodev/gdpr-banner
// Banner Trigger if Not Closed
if (!localStorage.bannerClosed) {
    $('.privacy-banner').css('display', 'inherit');
} else {
    $('.privacy-banner').css('display', 'none');
}
$('.privacy-banner button').click(function() {
    $('.privacy-banner').css('display', 'none');
    localStorage.bannerClosed = 'true';
});
$('.banner-accept').click(function() {
    $('.privacy-banner').css('display', 'none');
    localStorage.bannerClosed = 'true';
});
if (navigator.userAgent.match(/Opera|OPR\//)) {
    $('.privacy-banner').css('display', 'inherit');
}
