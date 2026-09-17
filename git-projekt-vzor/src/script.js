const citaty = [
  "Kachna, která nesnáší vodu, je jen tučný holub.",
  "Kdo maže, ten jede. Kdo nemaže, ten uklízí.",
  "Ponožky se neztrácejí, jen se rozhodly pro jiný životní styl.",
  "Pondělí je jen sobota s horší reklamou.",
  "Nikdy nevěř počítači, který se tváří rychleji, než umí.",
  "Ticho před bouří je jen wifi, co se připojuje.",
  "Kávovar je jediný kolega, který tě nikdy nezklame.",
  "Git je jako paměť slona, jen s víc konflikty.",
];

const citatEl = document.getElementById("citat");
const btn = document.getElementById("btn");

function novyCitat() {
  const index = Math.floor(Math.random() * citaty.length);
  citatEl.textContent = citaty[index];
}

btn.addEventListener("click", novyCitat);
