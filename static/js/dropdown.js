window.addEventListener('load', (event) => {
    $("#dimensiuneFereastra").hide();
    $("#dimensiuneUsa").hide();
    $("#dimensiuneBalcon").hide();
    $("#deschidereFereastra1").hide();
    $("#deschidereFereastra2").hide();
    $("#deschidereFereastra3").hide();
    $("#deschidereFereastra4").hide();
    $("#deschidereUsa1L").hide();
    $("#deschidereUsa2").hide();
    $("#deschidereUsa2L").hide();
    $("#profil").hide();
    $("#sticla1").hide();
    $("#sticla2").hide();
    $("#culoare").hide();
});

// tip produs
$("#radioFereastra").change (function () {
  $("#dimensiuneFereastra").show();
  $("#dimensiuneUsa").hide();
  $("#dimensiuneBalcon").hide();
  $("#deschidereFereastra1").hide();
  $("#deschidereFereastra2").hide();
  $("#deschidereFereastra3").hide();
  $("#deschidereFereastra4").hide();
  $("#deschidereUsa1L").hide();
  $("#deschidereUsa2").hide();
  $("#deschidereUsa2L").hide();
  $("#profil").hide();
  $("#sticla1").hide();
  $("#culoare").hide();
  $("#sticla2").hide();
});
$("#radioUsa").change (function () {
  $("#dimensiuneFereastra").hide();
  $("#dimensiuneUsa").show();
  $("#dimensiuneBalcon").hide();
  $("#deschidereFereastra1").hide();
  $("#deschidereFereastra2").hide();
  $("#deschidereFereastra3").hide();
  $("#deschidereFereastra4").hide();
  $("#deschidereUsa1L").hide();
  $("#deschidereUsa2").hide();
  $("#deschidereUsa2L").hide();
  $("#profil").hide();
  $("#sticla1").hide();
  $("#culoare").hide();
  $("#sticla2").hide();
});
$("#radioBalcon").change (function () {
  $("#dimensiuneFereastra").hide();
  $("#dimensiuneUsa").hide();
  $("#dimensiuneBalcon").show();
  $("#deschidereFereastra1").hide();
  $("#deschidereFereastra2").hide();
  $("#deschidereFereastra3").hide();
  $("#deschidereFereastra4").hide();
  $("#deschidereUsa1L").hide();
  $("#deschidereUsa2").hide();
  $("#deschidereUsa2L").hide();
  $("#profil").hide();
  $("#culoare").hide();
  $("#sticla1").hide();
  $("#sticla2").hide();
});




// fereastra radio dimensiuni
$("#radio500x500").change (function () {
  $("#deschidereFereastra1").show();
  $("#deschidereFereastra2").hide();
  $("#deschidereFereastra3").hide();
  $("#deschidereFereastra4").hide();
});
$("#radio800x1200").change (function () {
  $("#deschidereFereastra1").show();
  $("#deschidereFereastra2").hide();
  $("#deschidereFereastra3").hide();
  $("#deschidereFereastra4").hide();
});
$("#radio900x1500").change (function () {
  $("#deschidereFereastra1").show();
  $("#deschidereFereastra2").hide();
  $("#deschidereFereastra3").hide();
  $("#deschidereFereastra4").hide();
});
$("#radio1000x500").change (function () {
  $("#deschidereFereastra1").hide();
  $("#deschidereFereastra2").show();
  $("#deschidereFereastra3").hide();
  $("#deschidereFereastra4").hide();
});
$("#radio1400x1200").change (function () {
  $("#deschidereFereastra1").hide();
  $("#deschidereFereastra2").hide();
  $("#deschidereFereastra3").show();
  $("#deschidereFereastra4").hide();
});
$("#radio2200x1200").change (function () {
  $("#deschidereFereastra1").hide();
  $("#deschidereFereastra2").hide();
  $("#deschidereFereastra3").show();
  $("#deschidereFereastra4").hide();
});
$("#radio1500x1500").change (function () {
  $("#deschidereFereastra1").hide();
  $("#deschidereFereastra2").hide();
  $("#deschidereFereastra3").show();
  $("#deschidereFereastra4").hide();
});
$("#radio2000x1500").change (function () {
  $("#deschidereFereastra1").hide();
  $("#deschidereFereastra2").hide();
  $("#deschidereFereastra3").hide();
  $("#deschidereFereastra4").show();
});

// usa radio dimensiuni
$("#radio1000x2100").change (function () {
  $("#deschidereFereastra1").show();
  $("#deschidereUsa2").hide();
  $("#deschidereUsa1L").hide();
  $("#deschidereUsa2L").hide();
});
$("#radio1000x2500").change (function () {
  $("#deschidereUsa1L").show();
  $("#deschidereUsa2").hide();
  $("#deschidereFereastra1").hide();
  $("#deschidereUsa2L").hide();
});
$("#radio1200x2100").change (function () {
  $("#deschidereUsa1L").hide();
  $("#deschidereUsa2").show();
  $("#deschidereFereastra1").hide();
  $("#deschidereUsa2L").hide();
});
$("#radio1200x2500").change (function () {
  $("#deschidereUsa1L").hide();
  $("#deschidereUsa2").hide();
  $("#deschidereUsa2L").show();
  $("#deschidereFereastra1").hide();
});
$("#radio1500x2100").change (function () {
  $("#deschidereUsa1L").hide();
  $("#deschidereUsa2").show();
  $("#deschidereUsa2L").hide();
  $("#deschidereFereastra1").hide();
});
$("#radio1500x2500").change (function () {
  $("#deschidereUsa1L").hide();
  $("#deschidereUsa2").hide();
  $("#deschidereUsa2L").show();
  $("#deschidereFereastra1").hide();
});

// usa balcon radio dimensiuni
$("#radio800x2100").change (function () {
  $("#deschidereUsa2").hide();
  $("#deschidereFereastra1").show();
  $("#deschidereFereastra4").hide();
});
$("#radio1400x2100").change (function () {
  $("#deschidereUsa2").show();
  $("#deschidereFereastra1").hide();
  $("#deschidereFereastra4").hide();
});
$("#radio2400x2100").change (function () {
  $("#deschidereUsa2").hide();
  $("#deschidereFereastra1").hide();
  $("#deschidereFereastra4").show();
});


// deschidere > profile
$("#d1").change (function () {
  $("#profil").show();
});
$("#d2").change (function () {
  $("#profil").show();
});
$("#d3").change (function () {
  $("#profil").show();
});
$("#d4").change (function () {
  $("#profil").show();
});
$("#d5").change (function () {
  $("#profil").show();
});
$("#d6").change (function () {
  $("#profil").show();
});
$("#d7").change (function () {
  $("#profil").show();
});
$("#d8").change (function () {
  $("#profil").show();
});
$("#d9").change (function () {
  $("#profil").show();
});
$("#d10").change (function () {
  $("#profil").show();
});
$("#d11").change (function () {
  $("#profil").show();
});
$("#d12").change (function () {
  $("#profil").show();
});

// profil>sticla & culoare
$("#aluplast").change (function () {
  $("#sticla1").show();
  $("#sticla2").hide();
  $("#culoare").show();
});
$("#rehau").change (function () {
  $("#sticla1").show();
  $("#sticla2").hide();
  $("#culoare").show();
});
$("#synego").change (function () {
  $("#sticla1").hide();
  $("#sticla2").show();
  $("#culoare").show();
});
$("#geneo").change (function () {
  $("#sticla1").hide();
  $("#sticla2").show();
  $("#culoare").show();
});
