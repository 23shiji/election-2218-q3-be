from app import app
import os

prod = os.environ.get('env') == 'prod'
port = int(os.environ.get('port')) if 'port' in os.environ else 8080

if __name__ == '__main__':
  app.run(port=port, debug=not prod)