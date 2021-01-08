export function join(tokens: string | string[], glue = ''): string {
  if (typeof tokens === 'string') {
      return tokens
  }
  else {
    return tokens.join(glue)
  }
}

console.log(join('Hello') == 'Hello');
console.log(join(['Hello', 'world!'], ' ') == 'Hello, world!');
