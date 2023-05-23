(function(isPanel) {

    function executeScript(){
        alert(456456);
}

    var script_name = 'SGwriteFromAE';

    var win = (isPanel instanceof Panel) ?
        isPanel :
        new Window('palette', script_name, undefined, {
            resizeable: true
        });

    win.alignChildren = ['fill', 'fill'];

    var Objgroup= win.add('group');
    Objgroup.alignChildren = ['fill', 'fill'];    
    Objgroup.orientation = 'row'    
    Objgroup.spacing=5; 
    var exeBtn= Objgroup.add('button',undefined,"write ShotGrid");
    
    exeBtn.onClick = executeScript;

    win.layout.layout();
    win.onResize = function() {
        win.layout.resize();
    }

    if (!(win instanceof Panel)) {
        win.center();
        win.show();
    }

}(this));