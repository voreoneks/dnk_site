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

    let politicsBlock = document.getElementsByClassName('release-footer')[0];
    let addVideoNo = document.getElementsByName('add_video')[0];
    let addVideoYes = document.getElementsByName('add_video')[1];
    
    if(addVideoYes){
        addVideoYes.addEventListener('input', function(){
            if (addVideoYes.checked){
                politicsBlock.style.display = 'none';
            }
        });
    };

    if(addVideoNo){
        addVideoNo.addEventListener('input', function(){
            if (addVideoNo.checked){
                politicsBlock.style.display = 'block';
            }
        });
    };

    let submitBtn = document.getElementById('send');
    let loadingBtn = document.getElementById('loading');
    
    
    submitBtn.addEventListener('click', function(){
        submitBtn.setAttribute('hidden', true);
        loadingBtn.removeAttribute('hidden')
        setTimeout(() => {
            submitBtn.removeAttribute('hidden');
            loadingBtn.setAttribute('hidden', true);
        }, 20000);
    });

    // $('button[type=submit]').click(function(){
    //     $('form').submit();
    //     $(this).attr('disabled', 'disabled');
    //     $(this).fadeOut('1000', function(){
    //         $('#loading').removeAttr('hidden');
    //     })
    // })
    
});


var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
return new bootstrap.Tooltip(tooltipTriggerEl);
})
