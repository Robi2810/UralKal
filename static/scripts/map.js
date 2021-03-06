function closeSpCards() {
	let cards = document.getElementsByClassName('sp-card');
	let popups = document.getElementsByClassName('popups');
	let circles = document.getElementsByClassName('area-hover');
	for (let card of cards) {
		card.classList.add('d-none')
	}
	for (let pop of popups) {
		pop.setAttribute('style', 'display:none;')
	}
	for (let circle of circles) {
		circle.setAttribute('style', 'display:inline;')
	}
}

function openSpCard(index) {
	closeSpCards();
	let card = document.getElementById(`sp-card-${index}`);
	let card_body = document.getElementById(`sp-card-${index}-title`);
	let circle = document.getElementById(`circle${index}`);
	let l1 = document.getElementById(`c${index}l1`);
	let l2 = document.getElementById(`c${index}l2`);
	let popup = document.getElementById(`popup${index}`);
	popup.setAttribute('style', 'display:inline;');
	circle.setAttribute('style', 'display:none;')
	l1.setAttribute('style', 'display:none;')
	l2.setAttribute('style', 'display:none;')
	card.classList.remove('d-none');
}


function openAnalyticsCard() {
	closeSpCards();
	let card = document.getElementById('analytics-wrapper');
	let a_btn = document.getElementById('analytics-button');
	a_btn.classList.add('d-none');
	card.classList.remove('d-none');
}

function closeAnalyticsCard() {
	let card = document.getElementById('analytics-wrapper');
	let a_btn = document.getElementById('analytics-button');
	a_btn.classList.remove('d-none');
	card.classList.add('d-none');
}


function openAnalyticsImage(index) {
	let card = document.getElementById('analytics-card');
	let close_btn = document.getElementById('close-analytics');
	let image = document.getElementById('analytics-image');
	close_btn.onclick = () => { closeAnalyticsImage(); };
	let img_inner = document.createElement('img');
	let txt_inner = document.createElement('h2');
	txt_inner.innerHTML = `Аналитика ${index} <br>`;
	img_inner.setAttribute('src', `static/images/Analytics/${index}.png`);
	img_inner.classList.add('img-fluid');
	img_inner.classList.add('mt-5');
	image.appendChild(txt_inner);
	image.appendChild(img_inner);
	image.classList.remove('d-none');
	card.classList.add('d-none');
}

function closeAnalyticsImage() {
	let card = document.getElementById('analytics-card');
	let close_btn = document.getElementById('close-analytics');
	let image = document.getElementById('analytics-image');
	close_btn.onclick = () => { closeAnalyticsCard(); };
	image.innerHTML = '';
	image.classList.add('d-none');
	card.classList.remove('d-none');
}


let sector1 = document.getElementById('circle1');
let sector2 = document.getElementById('circle2');
let sector3 = document.getElementById('circle3');
let sector4 = document.getElementById('circle4');


sector1.onclick = () => { openSpCard(1); };
sector2.onclick = () => { openSpCard(2); };
sector3.onclick = () => { openSpCard(3); };
sector4.onclick = () => { openSpCard(4); };