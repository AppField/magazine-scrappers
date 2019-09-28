import sys
import os

def main():    
    url = sys.stdin.readline()    
        
    path = os.path.dirname(os.path.abspath(__file__))
    
    filepath = os.path.join(path, 'article-urls.txt')

    file = open(filepath, 'a+')

    file.write(url)
    
    file.close()


if __name__ == "__main__":
    main()
