$(function () {

// The height of the content block when it's not expanded
    var adjustheight = 100;
// The "more" link text
    var moreText = "+  More";
// The "less" link text
    var lessText = "- Less";

// Sets the .more-block div to the specified height and hides any content that overflows
    $(".more-less .more-block").css('height', adjustheight).css('overflow', 'hidden');

// The section added to the bottom of the "more-less" div
    $(".more-less").append('<p class="continued"></p><a href="#" class="adjust"></a>');

    $("a.adjust").text(moreText);

    $(".adjust").toggle(function () {
        $(this).parents("div:first").find(".more-block").css('height', 'auto').css('overflow', 'visible');
        // Hide the [...] when expanded
        $(this).parents("div:first").find("p.continued").css('display', 'none');
        $(this).text(lessText);
    }, function () {
        $(this).parents("div:first").find(".more-block").css('height', adjustheight).css('overflow', 'hidden');
        $(this).parents("div:first").find("p.continued").css('display', 'block');
        $(this).text(moreText);
    });
});
