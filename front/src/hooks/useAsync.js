import { useEffect } from 'react';

// A hook that wraps useEffect to perform an async call on state change and avoid memory leaks.
function useAsync(
  asyncFunc,
  onSuccess,
  watchables,
  onFailure
) {
  useEffect(() => {
    let isMounted = true;
    asyncFunc().then((data) => {
      if (isMounted && data !== null) {
        onSuccess(data);
      } else if (isMounted && onFailure) {
        onFailure();
      }
    });
    return () => { isMounted = false; };
  }, watchables);
}

export default useAsync;