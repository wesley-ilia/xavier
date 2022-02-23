export default {
  get: (url) => Promise.resolve({ data: "a", json: () => Promise.resolve() }),
  post: (url) => Promise.resolve({ data: "a" }),
};
