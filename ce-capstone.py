from app import app, freezer

if __name__ == "__main__":
    freezer.freeze() # Generates static HTML files
    app.run(port=5000) # Runs webserver locally for testing