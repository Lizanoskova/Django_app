$(document).ready(function(){

   function updateComments(){
        $('.commentsdiv').each(function() {
                $(this).load($(this).data('url'));
        })
   }

   setInterval(updateComments, 2000);
   updateComments();


    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
            }
        }
    });

    $('select').chosen();

    $('.postLike').on('click', '.postLikeLink', function(e) {
        e.preventDefault();
        var link = $(this).parent().find('.postLikeCounter');
        $.ajax({url: $(this).attr('href'), method: 'post'}).done(function(data, state, response) {
            if (state == 'success') {
                link.text(data);
            }
        });
    });

    function openDialog() {
        $('.modal').modal('show');
    }

    function closeDialog() {
        dialogElement = document.getElementById('mainDialog');
        dialogElement.style.display = 'none';
    }
    $(document).on('click', '.editLink', function(event) {
        openDialog();
        $.get(this.href, function(data) {
            $('#dialogBody').html(data);
        });
        event.preventDefault();
    });

    $(document).on('submit', '[data-formtype="ajaxForm"]', function(event){
        var form = this;
        $.post(this.action, $(this).serialize(), function(data){
            if(data == "OK") document.location.reload();
            else ('#'+$(form).data('success-container-id')).html(data);
        });
        event.preventDefault();

    })

});

