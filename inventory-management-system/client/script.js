async function askQuestion() {

    const question = document.getElementById(
        "question"
    ).value;


    const responseBox = document.getElementById(
        "response"
    );


    if (!question) {

        responseBox.innerHTML =
            "Please enter a question.";

        return;
    }


    responseBox.innerHTML =
        "Loading...";


    try {

        const response = await fetch(
            "http://127.0.0.1:7000/query",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    question: question
                })
            }
        );


        const data = await response.json();


        responseBox.innerHTML =
            data.answer;


    } catch (error) {

        responseBox.innerHTML =
            "Error: Failed to fetch";

    }
}