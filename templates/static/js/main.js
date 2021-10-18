$(function(){
    $('.copy').click(function(){
        var text = $(this).parent().prev().children().val();
        var fullNameElem = $(this).parent().prev().children().attr('name');
        var attribute = fullNameElem.split('-')[2];
        var rowNum = fullNameElem.split('-')[1];
        var targetInput = $('input[name$="' + attribute + '"]');
        var targetSelect = $('select[name$="' + attribute + '"]');
        for(var i = rowNum; i <= targetInput.length; i++){
            targetInput.eq(i).val(text);
        }
        for(var i = rowNum; i <= targetSelect.length; i++){
            targetSelect.eq(i).val(text)
        }
    })
});
