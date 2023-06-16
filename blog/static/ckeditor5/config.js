$(document).ready(function () {
    ClassicEditor
        .create(document.querySelector('#id_content'), {

    licenseKey: '',
            ckfinder: {
                uploadUrl: '/uploads/'
            },




})
    .then(editor => {
        window.editor = editor;




    })
    .catch(error => {
        console.error('Oops, something went wrong!');
        console.error('Please, report the following error on https://github.com/ckeditor/ckeditor5/issues with the build id and the error stack trace:');
        console.warn('Build id: 4fv8vet830vx-jr1tu2410lav');
        console.error(error);
        });
    })