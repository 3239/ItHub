module.exports = {
    darkMode: 'selector',
    content: [
        '../templates/**/*.html',
        './node_modules/flowbite/**/*.js'

    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('flowbite/plugin')
    ],
}