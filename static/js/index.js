function fileValidation(){
    var fileInput = document.getElementById('file');
    var filePath = fileInput.value;
    var allowedExtensions = /(\.txt)$/i;
    // if file is not selected disable the buttons
    
    if(!allowedExtensions.exec(filePath)){
        alert('Please upload file having extensions .txt only.');
        fileInput.value = '';
        document.getElementById("encrypt").disabled = true;
        document.getElementById("decrypt").disabled = true;
        return false;
    }else{
        //Image preview
        if (fileInput.files && fileInput.files[0]) {
            var reader = new FileReader();
            reader.onload = function(event) {
                
                let content = event.target.result.toString();
                let data = ""
                for (var i = 0; i < content.length; i ++)
                {
                    if (content[i] == "\n")
                        data += "<br>"
                    else
                        data += content[i]
                }
                
                document.getElementById('preview').textContent = content;
                document.getElementById("encrypt").disabled = false;
                document.getElementById("decrypt").disabled = false;


            };
            reader.readAsText(fileInput.files[0]);
        }
    }
}