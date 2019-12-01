import os, glob, time
def log(s):
    print('Fetch: {}'.format(s))

def dl(fname, day, year):
    import requests
    from secret import session
    jar = requests.cookies.RequestsCookieJar()
    jar.set('session', session)
    url = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
    r = requests.get(url, cookies=jar)
    if 'Puzzle inputs' in r.text:
        log('Session cookie expired?')
        return r.text
    if "Please don't repeatedly request this endpoint before it unlocks!" in r.text:
        log('Output not available yet')
        return r.text
    if r.status_code != 200:
        log('Not 200 as status code')
        return r.text
    with open(fname,'w') as f:
        f.write(r.text)
    return 0

def mkdirs(f):
    try:
        os.makedirs(f)
    except: pass


def fetch(year, day, log, force=False, wait_until=-1):
    filename = 'cache/{}-{}.in'.format(year, day)
    mkdirs('cache')
    exists = os.path.isfile(filename)
    if not exists or force:
        if wait_until != -1:
            to_sleep = wait_until - time.time()
            while to_sleep > 0:
                log.debug('Sleeping for {:.3f} s'.format(to_sleep))
                time.sleep(min(to_sleep, 1))
                to_sleep = wait_until - time.time()

        out = dl(filename, day, year)
        if out != 0:
            return out
    return open(filename, 'r').read().strip('\n')


def get_samples(year, day):
    d = 'samples/{}_{}'.format(year,day)
    mkdirs('samples')
    mkdirs(d)
    samples = []
    for fname in glob.glob('{}/*.in'.format(d)):
        inp = open(fname, 'r').read().strip('\n')
        samples.append((fname, inp))
    return samples

