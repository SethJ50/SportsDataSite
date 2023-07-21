from website import create_app

app = create_app()

if __name__ == '__main__': # only runs if you run this file directly
    app.run(debug=True)

