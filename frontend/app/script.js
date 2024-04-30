const button = document.querySelector('button')
const img = document.querySelector('img')
const input = document.querySelector('input')

button.addEventListener("click", async () => {
  const response = await fetch("http://127.0.0.1:8000/generate/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      prompt: input.value
    })
  })
  const blob = await response.blob();

  const obj_url = URL.createObjectURL(blob)
  img.src = obj_url;
})