function openDocument(name, path) {
	let content = document.getElementById('content');
	let doc_window = document.getElementById('document-wrapper');
	let title = document.getElementById('document-title');
	let viewer = document.getElementById('pdf-viewer');
	title.innerText = name;
	doc_window.classList.remove('d-none');
	content.classList.add('d-none');
	var loadingTask = pdfjsLib.getDocument(`/static/files/${path}`);
	loadingTask.promise.then(function(pdf) {
		for (var i = 1; i <= pdf.numPages; i++) {
			pdf.getPage(i).then(function(page) {
				var canvasId = 'pdf-viewer-' + i;
				let canvas = document.createElement('canvas');
				canvas.setAttribute('id', canvasId);
				viewer.appendChild(canvas);
	  			//var canvas = document.getElementById(canvasId);
				var scale = 1.5;
				var viewport = page.getViewport({ scale: scale, });
				// Support HiDPI-screens.
				var outputScale = window.devicePixelRatio || 1;
				var context = canvas.getContext('2d');

				canvas.width = Math.floor(viewport.width * outputScale);
				canvas.height = Math.floor(viewport.height * outputScale);
				canvas.style.height =  Math.floor(viewport.height) + "px";
				canvas.style.width = Math.floor(viewport.width) + "px";

				var transform = outputScale !== 1
				  ? [outputScale, 0, 0, outputScale, 0, 0]
				  : null;

				var renderContext = {
				  canvasContext: context,
				  transform: transform,
				  viewport: viewport
				};
				page.render(renderContext);
			});
		}
	});
}


function closeDocument() {
	let content = document.getElementById('content');
	let doc_window = document.getElementById('document-wrapper');
	doc_window.classList.add('d-none');
	content.classList.remove('d-none');
	let pdf_viewer = document.getElementById('pdf-viewer');
	pdf_viewer.innerHTML = '';
}