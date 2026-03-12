async function analyzeTask() {

    const prompt = document.getElementById("promptInput").value;

    console.log("Sending prompt:", prompt);

    const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            prompt: prompt
        })
    });

    const data = await response.json();

    console.log("Raw response:", data);

    console.log(document.getElementById("category"));
    let toolsHTML = "<h4>Recommended Tools:</h4>";

    data.tools.forEach(tool => {
        toolsHTML += `${tool.name} (Performance: ${tool.performance})<br>`;
    });

    document.getElementById("tools").innerHTML = toolsHTML;

    document.getElementById("response").innerText =
        data.ai_response;
}