from app import create_app
import os
app = create_app()

if __name__ == "__main__": 
  app.run(debug=False, port=os.getenv("PORT") or 3000)