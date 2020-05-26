from configparser import ConfigParser

if __name__ == "__main__":
    cfg = ConfigParser()

    cfg['config'] = { 'WEBSITE_URL' : 'https://robinhood.com/login' }

    with open('config.pyc','w') as configfile:
        cfg.write(configfile)
