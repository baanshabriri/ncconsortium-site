export default {
    content: [
        "./templates/**/*.html",
        "./pages/**/*.py",
        "./core/**/*.py"
    ],
    theme: {
        extend: {
            maxWidth: {
                text: "48ch",
            },
            colors: {
                brand: {
                    yellow: "#facc15",
                    orange: "#f97316",
                }
            }
        }
    },
    plugins: [],
}
