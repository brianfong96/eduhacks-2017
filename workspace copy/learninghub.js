(function() {
    
    var curNotebook;
    var lastPage; 
    
    $(document).ready(function() {
        $('#gotomentor').click(function() {
            switchCurPage('#mentor'); 
        });
        $('#gotonotebook').click(function() {
            switchCurPage('#frontpage');
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
            if(lastPage != $('#me')) {
                switchCurPage('#aboutme');
            } else {
                switchCurPage(lastPage);
            }
        });
        
        $('.notebooks').click(function() {
            var num = $(this).attr('alt');
            if($('#notebookcontents').hasClass('hidden')) { //there is no active notebook is inactive 
                $(this).attr('src', 'images/Sub_' + num + '.png');
                $(this).addClass('active');
                curNotebook = num; 
                $('#notebookcontents').removeClass('hidden');
            } else if(!$(this).hasClass('active')) { //there is an active notebook, but you're switching
                $('#Sub_' + curNotebook).attr('src', 'images/Sub_' + curNotebook + '_Inactive.png');
                $('#Sub_' + curNotebook).removeClass('active');
                $(this).addClass('active');
                curNotebook = num;
            } else if(!$('#notebookcontents').hasClass('hidden')) { //close out of active notebook 
                $(this).removeClass('active');
                $(this).attr('src', 'images/Sub_' + num + '_Inactive.png');
                $('#notebookcontents').addClass('hidden'); 
            }
        }); 
    }); 
    
    $( window ).on( "load", function() {
        curNotebook = 0; 
    });
    
    function showNotebook() {
        if($('#notebookcontents').hasClass('hidden')) {
           $('#notebookcontents').removeClass('hidden'); 
        } else {
            $('#notebookcontents').addClass('hidden'); 
        }
    }
    
    
    function switchCurPage(page) {
        lastPage = $('.curpage');
        $('.curpage').addClass('hidden');
        $('.curpage').removeClass('curpage');
        $(page).removeClass('hidden');
        $(page).addClass('curpage');
    }
    
})(); 