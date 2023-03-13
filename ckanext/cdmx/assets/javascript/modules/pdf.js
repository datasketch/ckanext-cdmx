ckan.module('pdf', function (jQuery) {
  return {
    initialize: function() {
      const doc = this.options.doc
      // Loaded via <script> tag, create shortcut to access PDF.js exports.
      const pdfjsLib = window['pdfjs-dist/build/pdf'];
      console.log(pdfjsLib);
      // The workerSrc property shall be specified.
      pdfjsLib.GlobalWorkerOptions.workerSrc = window.location.origin + '/js/pdf.worker.min.js'
      const loadingTask = pdfjsLib.getDocument(doc);
      const id = this.el.id
      console.log(id);

      loadingTask.promise.then(function (pdf) {
        pdf.getPage(1).then(function (page) {
          const scale = 1
          const viewport = page.getViewport({ scale })

          // Prepare canvas using PDF page dimensions
          const canvas = document.getElementById(id);
          const context = canvas.getContext('2d');
          canvas.height = viewport.height;
          canvas.width = viewport.width;

          const renderTask = page.render({
            canvasContext: context,
            viewport: viewport
          });
          renderTask.promise.then(function () {
            console.log('Page rendered');
          });
        })
      })
    }
  }
})