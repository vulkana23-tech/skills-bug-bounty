# 🟨 Technical Reference: JS Reverse Engineering & AST Deobfuscation Guide

## 🛠️ Common Tools & Libraries
- **web-crack**: Unpack webpack & deobfuscate obfuscator.io scripts automatically.
- **Babel Toolchain**: `@babel/parser`, `@babel/traverse`, `@babel/generator`.

## 📜 Node.js AST String Decoder Snippet
```javascript
const parser = require('@babel/parser');
const traverse = require('@babel/traverse').default;
const generate = require('@babel/generator').default;

const code = `var _0x1234 = ['hello', 'world']; function greet() { return _0x1234[0]; }`;
const ast = parser.parse(code);

traverse(ast, {
    MemberExpression(path) {
        // Replace string lookup arrays with direct literals
    }
});

console.log(generate(ast).code);
```
