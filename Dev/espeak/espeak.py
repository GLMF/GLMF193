import subprocess

def readText(text, lang='en', voice='m1', speed='160', amplitude='100', pitch='50'):
    options = {
        'voice' : '-v' + lang + '+' + voice,
        's' : '-s' + speed,
        'a' : '-a' + amplitude,
        'p' : '-p' + pitch,
    }
    subprocess.call(['espeak', text, options['voice'], options['s'], options['a'], options['p']])

if __name__ == '__main__':
    readText('Salut, je suis ton ordinateur', lang='fr', voice='f3', speed='150')
