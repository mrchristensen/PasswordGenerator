import sys
import crypt

changed_days = "30"
min_days = "0"
max_days = "99999"
warn_days = "7"
user_id = "1000"
group_id = "1000"
user_info = "GECOS"


def generate_passwd(username):
    ret = username + ":x:" + user_id + ":" + group_id + ":" + user_info + ":directory:shell11"

    return ret


def generate_shadow(username, password):
    encrypted_password = crypt.crypt(password, crypt.METHOD_MD5)  # https://stackoverflow.com/questions/53416164/md5-hash-in-python

    ret = username + ":" + encrypted_password + ":" + changed_days + ":" + min_days + ":" + max_days + ":" + warn_days + ":::"

    return ret


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    print(generate_passwd(username))
    print(generate_shadow(username, password))
