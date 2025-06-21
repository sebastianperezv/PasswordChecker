import requests # allows us to make a request
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    # print(res) Response [400] means unauthorized, we want Response[200]
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def read_res(response):
    print(response.text) # we get all the hashes that macth the begining of our hash password

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes: # hashes are the tail of a hash
        if h == hash_to_check:
            return count # returns how many times the password has been leaked
    return 0

# check password if it existis in API response
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char) # returns all the hashes related with first5_char
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times...you sould change your password')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!'

# run this file only if it is the main file running from the command line
# noy if it is imported
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))