const API_ORIGIN = 'https://https://proyecto-inicial-backend-agk6kyxhfa-uc.a.run.app/'

async function sendData(data) {
  const endpoint = new URL('/api/send-data/', API_ORIGIN)

  const stringifiedData = JSON.stringify(data)

  const response = await fetch(endpoint, {
    method: 'POST',
    body: stringifiedData,
    headers: {
      'Content-Type': 'application/json',
    },
  })

  return await response.json()
}
