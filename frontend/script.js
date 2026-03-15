async function analyzeEmail() {

    const email = document.getElementById("emailInput").value;

    const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email
        })
    });

    const data = await response.json();

    document.getElementById("finalScore").textContent = data.final_score;
    document.getElementById("heuristicScore").textContent = data.heuristic_score;
    document.getElementById("urlScore").textContent = data.url_score;
    document.getElementById("llmScore").textContent = data.llm_score;

    // format LLM explanation into bullet points
    const formatted = data.llm_analysis
        .split(". ")
        .map(sentence => `<li>${sentence.trim()}.</li>`)
        .join("");

    document.getElementById("llmAnalysis").innerHTML =
        `<ul class="list-disc ml-6">${formatted}</ul>`;

    document.getElementById("result").classList.remove("hidden");
}


document.getElementById("year").textContent = new Date().getFullYear();