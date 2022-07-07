window.addEventListener('load', (event) => {
    $("#dim").hide();
    $("#des").hide();

  });
$("#Radio1").change (function () {
    $("#dim").show();
    $("#f_dim").show();
    $("#u_dim").hide();
    $("#ub_dim").hide();

    $("#des").show();
    $("#f_des").show();
    $("#u_des").hide();
    $("#ub_des").hide();
});
$("#Radio2").change (function () {
    $("#dim").show();
    $("#f_dim").hide();
    $("#u_dim").show();
    $("#ub_dim").hide();

    $("#des").show();
    $("#f_des").hide();
    $("#u_des").show();
    $("#ub_des").hide();
});
$("#Radio3").change (function () {
    $("#dim").show();
    $("#f_dim").hide();
    $("#u_dim").hide();
    $("#ub_dim").show();

    $("#des").show();
    $("#f_des").hide();
    $("#u_des").hide();
    $("#ub_des").show();
});
