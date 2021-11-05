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

    $('button[type=submit]').click(function(){
        $('form').submit();
        $(this).attr('disabled', 'disabled');
        $(this).fadeOut('1000', function(){
            $('#loading').removeAttr('hidden');
        })
    })
});
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
return new bootstrap.Tooltip(tooltipTriggerEl)
})
