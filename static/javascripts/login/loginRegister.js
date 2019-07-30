    $("#loginID").click(function(){
      $("#loginID").addClass('is-selected');
      $("#registerID").removeClass('is-selected');
      $("#loginForm").show();
      $("#registerForm").hide();
    });

    $("#registerID").click(function(){
        $("#loginID").removeClass('is-selected');
        $("#registerID").addClass('is-selected');
        $("#loginForm").hide();
        $("#registerForm").show();
    });
