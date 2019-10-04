import sys
import os
from datetime import datetime

def main():    
    url = sys.stdin.readline()    
        
    path = os.path.dirname(os.path.abspath(__file__))
    
    date = datetime.now().strftime("%Y-%m-%d")

    filename = "urls/{0}-article-urls.txt".format(date)

    filepath = os.path.join(path, filename)

    file = open(filepath, 'a+')

    file.write(url)
    
    file.close()


if __name__ == "__main__":
    main()
