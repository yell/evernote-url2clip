#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import yaml
import argparse
import selenium.common
import selenium.webdriver.support.ui as ui
import numpy as np
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


def send_keys(browser, keys):
    webdriver.ActionChains(browser).send_keys(keys).perform()


def main(urls, args):
    # load config
    with open('config.yml') as f:
        config = yaml.load(f)

    # add clipper extension
    chrome_options = Options()
    extensions = filter(lambda s: s.endswith('.crx'), os.listdir('.'))
    assert len(extensions) >= 1
    chrome_options.add_extension(extensions[0])
    
    # disable browser notifications
    prefs = {'profile.default_content_setting_values.notifications': 2}
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-alerts')
    desired_capabilities=dict(unexpectedAlertBehaviour='accept')
    
    # prepare and launch browser
    browser = webdriver.Chrome(chrome_options=chrome_options,
                               desired_capabilities=desired_capabilities)
    browser.set_window_size(800, 640)
    browser.set_window_position(50, 100)
    browser.implicitly_wait(3)

    # login page
    browser.get('https://www.evernote.com/Login.action')

    # close popped-up tab
    main_window = browser.current_window_handle
    while len(browser.window_handles) <= 1:
        time.sleep(0.1)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()
    browser.switch_to.window(main_window)

    # login
    elem = ui.WebDriverWait(browser, 15).until(lambda b: b.find_element_by_id('username'))
    elem.send_keys(config['username'])
    elem.send_keys(Keys.ENTER)
    time.sleep(0.5)
    elem = ui.WebDriverWait(browser, 15).until(lambda b: b.find_element_by_id('password'))
    elem.send_keys(config['password'])
    elem.send_keys(Keys.ENTER)

    # enable shortcuts (manually) -.-'
    browser.get('chrome://extensions')

    msg = '\nEnable shortcuts:\n'
    msg += 'Web Clipper extension > "Options" > "Keyboard shortcuts" > check "Enable keyboard shortcuts"\n\n'
    msg += 'Optionally you can also configure other things like to what notebook to store etc.\n\n'
    msg += 'once done Press Any key to continue ...\n'
    sys.stderr.write(msg)
    raw_input()

    # clip pages
    print "\n\nClipping ...\n"
    for i in tqdm(range(len(urls))):
        try:
            # return focus
            browser.switch_to.window(main_window)

            # load url
            url = urls[i]
            browser.get(url)

            # open clipper
            send_keys(browser, '`')

            # close alerts if they still pop-up
            was_alert = False
            for _ in xrange(10):
                try:
                    time.sleep(0.5)
                    browser.switch_to.alert.accept()
                    alert = Alert(browser)
                    alert.accept()
                except selenium.common.exceptions.UnexpectedAlertPresentException:
                    was_alert = True
                    browser.switch_to.alert.accept()
                    alert = Alert(browser)
                    alert.accept()
                except selenium.common.exceptions.NoAlertPresentException:
                    pass
                else:
                    if was_alert:
                        break

            time.sleep(1)

            # choose desired clip type
            send_keys(browser, args.clip_type.lower())
            time.sleep(0.25)

            # clip
            send_keys(browser, Keys.ENTER)

            # empirically discovered indicator that clipping is done :D
            # that works for 99% of pages, for others there is a timeout
            try:
                BUF_LEN = 16
                BUF_POS = 4
                DT = 0.1
                TIMEOUT = args.clip_timeout
                buf = [0]
                for _ in xrange(int(TIMEOUT / DT)):
                    time.sleep(DT)
                    buf.append(len(browser.page_source))
                    if len(buf) >= BUF_LEN:
                        buf = buf[1:]
                    diff_buf = np.diff(buf)
                    print diff_buf
                    if min(diff_buf) == 0 and max(diff_buf) == 1 and sum(diff_buf) == 1 and diff_buf[BUF_POS] == 1:
                        break
            except KeyboardInterrupt:
                pass           

            # confirm stuff
            send_keys(browser, Keys.ENTER)
        
        except selenium.common.exceptions.UnexpectedAlertPresentException:
            pass

        except Exception as e:
            print type(e)
            msg = '\nError with [{0}/{1}]:\n'.format(i + 1, len(urls))
            msg += str(e)
            print msg
    
    # close browser
    browser.quit()


if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('fpath', type=str, metavar='FILEPATH',
                        help='file path with urls')
    parser.add_argument('--clip-type', type=str, default='A', metavar='TYPE',
                        help="how to clip content: 'A' - article, 'B' - bookmark, " + \
                             "'C' - simplified article, 'E' - email, 'F' - full page, " + \
                             "'M' - screenshot, 'P' - pdf, ... [see extension for more]")
    parser.add_argument('--clip-timeout', type=float, default=120, metavar='SEC',
                        help='default timeout (in seconds) to clip pages')
    args = parser.parse_args()

    # load urls from file
    with open(args.fpath) as f:
        urls = f.readlines()
    urls = [s.strip() for s in urls]

    # run main
    main(urls, args)
