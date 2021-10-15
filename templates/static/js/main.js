$(function(){
    $('.copy').click(function(){
        var text = $(this).parent().prev().children().val();
        var attribute = $(this).parent().prev().children().attr('name').split('-')[2];
        var target = $('input[name$="' + attribute + '"]');
        target.each(function(){
            $(this).val(text)
        });
    })
});
