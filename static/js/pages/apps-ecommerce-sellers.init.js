var dropzonePreviewNode=document.querySelector("#dropzone-preview-list2");if(dropzonePreviewNode){var previewTemplate=dropzonePreviewNode.parentNode.innerHTML;dropzonePreviewNode.parentNode.removeChild(dropzonePreviewNode);var dropzone=new Dropzone(".dropzone2",{url:"https://httpbin.org/post",method:"post",previewTemplate:previewTemplate,previewsContainer:"#dropzone-preview2"})}