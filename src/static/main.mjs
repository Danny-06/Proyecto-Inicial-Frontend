const API_ORIGIN = 'https://proyecto-inicial-backend-agk6kyxhfa-uc.a.run.app/'

/**
 * @typedef FormData
 * @property {string} qr_string
 * @property {number} timestamp
 */

/**
 * 
 * @param {FormData} data 
 * @returns 
 */
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


/**@type {HTMLFormElement}*/
const form = document.querySelector('form')

form.addEventListener('submit', event => {
  event.preventDefault()

  const formData = Object.fromEntries(new FormData(form))

  /**@type {FormData}*/
  const resultData = {...formData, timestamp: Date.now()}

  console.log(resultData)

  sendData(resultData)
  .then(value => alert('Data uploaded successfuly.'))
  .catch(reason => {
    console.error(reason)
    alert('An error occurred after submiting the form.')
  })
})
