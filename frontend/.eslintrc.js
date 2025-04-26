
module.exports = {
    root: true,
    env: {
      node: true,
      es2021: true  // 👈 importante para que acepte ES6+
    },
    extends: [
      'plugin:vue/vue3-essential',
      'eslint:recommended'
    ],
    parserOptions: {
      ecmaVersion: 2021, // 👈 soporta ES6+ (incluye `const`)
        sourceType: 'module'
    },
    rules: {
      // tus reglas personalizadas
    }
}
