function POST(object) {
  return {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(object),
  };
}

const GET = {
  method: 'GET',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
};

// A path on which server is listening
const defaultPath = 'http://34.28.161.207';

// A hook that handles the communication with server and provides get and post methods.
function useServer(path) {
  // A function that sends the get method to server and returns
  // the response on success or null otherwise.
  function get(uid) {
    return fetch(`${defaultPath}${path}/${uid}`, {  ...GET })
      .then((response) => (response.status === 200 ? response.json() : null));
  }

  // A function that sends the post method to server and returns
  // the response with response status.
  function post(object, uid) {
    return fetch(`${defaultPath}${path}/${uid}`, {  ...POST(object) })
      .then((response) => ({ status: response.status, data: response.json() }));
  }

  return { get, post };
}

export default useServer;