import subprocess

def readText(text):
    subprocess.call(['picoTTS', text])

if __name__ == '__main__':
    readText('Salut, je suis ton ordinateur')
