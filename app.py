from flask import Flask, render_template, request, redirect

app = Flask(__name__)

back_stack = []
forward_stack = []
current = None

@app.route("/", methods=["GET", "POST"])
def index():
    global current, back_stack, forward_stack

    if request.method == "POST":
        action = request.form.get("action")

        if action == "visit":
            url = request.form.get("url")

            if current:
                back_stack.append(current)

            current = url
            forward_stack.clear()

        elif action == "back":
            if back_stack:
                forward_stack.append(current)
                current = back_stack.pop()

        elif action == "next":
            if forward_stack:
                back_stack.append(current)
                current = forward_stack.pop()

        elif action == "reset":
            back_stack.clear()
            forward_stack.clear()
            current = None

    return render_template("index.html",
                           current=current,
                           back_stack=back_stack,
                           forward_stack=forward_stack)

if __name__ == "__main__":
    app.run(debug=True)