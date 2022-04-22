function closeSpCards() {
	let cards = document.getElementsByClassName('sp-card');
	for (let card of cards) {
		card.classList.add('d-none')
	}
}

function openSpCard(index) {
	closeSpCards();
	let card = document.getElementById(`sp-card-${index}`);
	let card_body = document.getElementById(`sp-card-${index}-title`);
	
	
	card.classList.remove('d-none');
}


function openAnalyticsCard() {
	let card = document.getElementById('analytics-card');
	card.classList.remove('d-none');
}

function closeAnalyticsCard() {
	let card = document.getElementById('analytics-card');
	card.classList.add('d-none');
}


let sector1 = document.getElementById('circle14');
let sector2 = document.getElementById('circle20');
let sector3 = document.getElementById('circle2');
let sector4 = document.getElementById('circle8');


sector1.onclick = () => { openSpCard(1); };
sector2.onclick = () => { openSpCard(2); };
sector3.onclick = () => { openSpCard(3); };
sector4.onclick = () => { openSpCard(4); };