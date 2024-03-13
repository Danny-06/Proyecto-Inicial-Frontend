async function sendData(data) {
  const stringifiedData = JSON.stringify(data)

  const response = await fetch('/api/send-data', {
    method: 'POST',
    body: stringifiedData,
    headers: {
      'Content-Type': 'application/json',
    },
  })

  return await response.json()
}
