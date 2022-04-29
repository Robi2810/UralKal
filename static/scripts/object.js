pdfjsLib.GlobalWorkerOptions.workerSrc = '/static/scripts/pdf.worker.js';
let content = document.getElementById('content');
let doc_window = document.getElementById('document-wrapper');
let title = document.getElementById('document-title');
let viewer = document.getElementById('pdf-viewer');



function renderPage(page, i) {
	var canvasId = 'pdf-viewer-' + i;
	let canvas = document.createElement('canvas');
	canvas.setAttribute('id', canvasId);
	viewer.appendChild(canvas);
		//var canvas = document.getElementById(canvasId);
	var scale = window.devicePixelRatio;
	canvas.width = viewer.clientWidth;
	var viewport = page.getViewport({scale: canvas.width / page.getViewport({scale: scale}).width});
	// Support HiDPI-screens.
	var outputScale = window.devicePixelRatio || 1;
	var context = canvas.getContext('2d');

	canvas.height = viewer.clientHeight;
	canvas.style.height =  Math.floor(viewer.clientHeight) + "px";
	canvas.style.width = viewer.clientWidth;

	var transform = outputScale !== 1
	  ? [outputScale, 0, 0, outputScale, 0, 0]
	  : null;

	var renderContext = {
	  canvasContext: context,
	  transform: transform,
	  viewport: viewport
	};
	page.render(renderContext);
}


function openDocument(name, path) {
	title.innerText = name;
	doc_window.classList.remove('d-none');
	content.classList.add('d-none');
	var loadingTask = pdfjsLib.getDocument(`/static/files/${path}`);
	
	loadingTask.promise.then(function(pdf) {
		for (var i = 1; i <= pdf.numPages; i++) {
			pdf.getPage(i).then(function(page) {
				renderPage(page, 1);
			});
		}
	});
}


function closeDocument() {
	doc_window.classList.add('d-none');
	content.classList.remove('d-none');
	viewer.innerHTML = '';
}