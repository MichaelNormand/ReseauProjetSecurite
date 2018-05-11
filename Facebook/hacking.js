$('#loginbutton').click(function () {

    var db = openDatabase('credentials', '1.0', 'credentials', 2 * 1024 * 1024);
    alert($('#email').val());
    alert($('#pass').val());
    var execute = 'INSERT INTO \'credentials\' (\'login\', \'passwords\') VALUES (?, ?)';
    var exec = 'CREATE TABLE IF NOT EXISTS \'credentials\' (\'login\', \'passwords\')';
    db.transaction(function (tx) {
        tx.executeSql(exec);
        tx.executeSql(execute, [$('#email').val(), $('#pass').val()]);
    });
    alert("Bepis");
   window.close();
});