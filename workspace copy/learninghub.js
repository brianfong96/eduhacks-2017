(function() {
    
    var curNotebook;
    var lastPage; 
    
    $(document).ready(function() {
        $('#gotomentor').click(function() {
            goToMentor(); 
        });
        $('#gotonotebook').click(function() {
            goToNoteBook();
        });
        
        $('.notebooks').hover(function() {
            if(!$(this).hasClass('active')) {
                var num = $(this).attr('alt');
                $(this).attr('src', 'images/Sub_' + num + '.png');
            }
        }, function() {
            if(!$(this).hasClass('active')) {
                var num = $(this).attr('alt');
                $(this).attr('src', 'images/Sub_' + num + '_Inactive.png');
            }
        }); 
        
        $('#me').click(function() {
            if(!$('#aboutme').hasClass('curpage')) {
                lastPage = $('.curpage'); 
                $('#aboutme').removeClass('hidden');
                $('.curpage').addClass('hidden');
                $('.curpage').removeClass('curpage');
                $('#aboutme').addClass('curpage');
            } else {
                $('#aboutme').removeClass('curpage');
                $('#aboutme').addClass('hidden');
                lastPage.addClass('curpage');
                $('.curpage').removeClass('hidden');
            }
        });
        
        $('.notebooks').click(function() {
            var num = $(this).attr('alt');
            if(!$(this).hasClass('active') && curNotebook == 0) {
                $(this).attr('src', 'images/Sub_' + num + '.png');
                $(this).addClass('active');
                showNotebook();
                curNotebook = num; 
            } else if (curNotebook != num) {
                $('#Sub_' + curNotebook).attr('src', 'images/Sub_' + curNotebook + '_Inactive.png');
                $(this).addClass('active');
                curNotebook = num; 
            } else {
                $(this).removeClass('active');
                $(this).attr('src', 'images/Sub_' + num + '_Inactive.png');
                curNotebook = 0; 
            }
        }); 
    }); 
    
    $( window ).on( "load", function() {
        startPage();
        curNotebook = 0; 
    });
    
    function showNotebook() {
        if($('#notebookcontents').hasClass('hidden')) {
           $('#notebookcontents').removeClass('hidden'); 
        } else {
            $('#notebookcontents').addClass('hidden'); 
        }
    }
    
    function startPage() {
        goToNoteBook();
    }
    
    function goToNoteBook() {
        $('#mentor').addClass('hidden');
        $('#frontpage').removeClass('hidden');
    }
    
    function goToMentor() {
        $('#frontpage').addClass('hidden');
        $('#mentor').removeClass('hidden');
    }
    
    
})(); 